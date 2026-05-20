"""API routes for Minecraft Skin AI Generator"""
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
import logging

from core.generator import SkinGenerator
from core.config import Config

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["api"])

# Global generator instance
generator = None

def get_generator():
    """Get or create generator instance"""
    global generator
    if generator is None:
        generator = SkinGenerator()
    return generator


# Request/Response models
class GenerateRequest(BaseModel):
    """Request model for skin generation"""
    prompt: str
    style: Optional[str] = "fantasy"


class EditRequest(BaseModel):
    """Request model for skin editing"""
    modification: str


class SkinResponse(BaseModel):
    """Response model for skin"""
    id: str
    prompt: str
    style: str


# Routes
@router.post("/generate")
async def generate_skin(request: GenerateRequest):
    """Generate a new Minecraft skin"""
    try:
        gen = get_generator()
        skin = gen.generate(request.prompt, request.style)
        skin.save()
        return {"success": True, "skin": skin.to_dict()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Generation error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate skin")


@router.post("/edit/{skin_id}")
async def edit_skin(skin_id: str, request: EditRequest):
    """Edit existing skin"""
    try:
        gen = get_generator()
        skin = gen.edit(skin_id, request.modification)
        skin.save()
        return {"success": True, "skin": skin.to_dict()}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Edit error: {e}")
        raise HTTPException(status_code=500, detail="Failed to edit skin")


@router.post("/random")
async def random_skin(style: Optional[str] = None):
    """Generate random skin"""
    try:
        gen = get_generator()
        skin = gen.random_generate(style)
        skin.save()
        return {"success": True, "skin": skin.to_dict()}
    except Exception as e:
        logger.error(f"Random generation error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate random skin")


@router.get("/skins")
async def list_skins() -> List[SkinResponse]:
    """List all generated skins"""
    gen = get_generator()
    return gen.list_skins()


@router.get("/skins/{skin_id}")
async def get_skin(skin_id: str):
    """Get specific skin"""
    gen = get_generator()
    skin = gen.get_skin(skin_id)
    if not skin:
        raise HTTPException(status_code=404, detail="Skin not found")
    return skin.to_dict()


@router.delete("/skins/{skin_id}")
async def delete_skin(skin_id: str):
    """Delete skin"""
    gen = get_generator()
    gen.delete_skin(skin_id)
    return {"success": True, "message": f"Skin {skin_id} deleted"}


@router.get("/styles")
async def list_styles():
    """Get available styles"""
    return {
        "styles": list(Config.STYLES.keys()),
        "descriptions": Config.STYLES
    }
