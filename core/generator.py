"""Main skin generator module"""
import uuid
import logging
from pathlib import Path
from PIL import Image
from .models import ModelManager
from .config import Config

logger = logging.getLogger(__name__)

class Skin:
    """Represents a generated Minecraft skin"""
    
    def __init__(self, image, prompt: str, style: str, skin_id: str = None):
        self.id = skin_id or str(uuid.uuid4())
        self.image = image
        self.prompt = prompt
        self.style = style
    
    def save(self, path: str = None) -> str:
        """Save skin to file"""
        if path is None:
            path = Config.SKINS_DIR / f"{self.id}.png"
        
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Resize to Minecraft skin size
        minecraft_skin = self.image.resize(
            (Config.SKIN_WIDTH, Config.SKIN_HEIGHT),
            Image.Resampling.LANCZOS
        )
        
        minecraft_skin.save(path)
        logger.info(f"Skin saved to {path}")
        return str(path)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "prompt": self.prompt,
            "style": self.style
        }


class SkinGenerator:
    """Main generator for Minecraft skins"""
    
    def __init__(self):
        self.model_manager = ModelManager()
        self.skins = {}
    
    def generate(self, prompt: str, style: str = "fantasy") -> Skin:
        """Generate a skin from prompt"""
        if style not in Config.STYLES:
            raise ValueError(f"Unknown style: {style}")
        
        # Enhance prompt with style
        enhanced_prompt = f"{prompt}, {Config.STYLES[style]}, minecraft skin, 64x64"
        
        logger.info(f"Generating skin with style: {style}")
        
        # Generate image
        images = self.model_manager.generate(enhanced_prompt)
        
        if not images:
            raise RuntimeError("Failed to generate image")
        
        # Create skin object
        skin = Skin(images[0], prompt, style)
        self.skins[skin.id] = skin
        
        logger.info(f"Skin generated: {skin.id}")
        return skin
    
    def random_generate(self, style: str = None) -> Skin:
        """Generate random skin"""
        import random
        
        if style is None:
            style = random.choice(list(Config.STYLES.keys()))
        
        random_prompts = [
            "brave warrior with glowing sword",
            "mysterious wizard with magical staff",
            "cute cat with crown",
            "scary demon with horns",
            "forest elf with bow",
            "astronaut in space suit",
            "viking with axe and beard",
            "ninja in black",
            "pirate with eye patch",
            "robot with glowing eyes"
        ]
        
        prompt = random.choice(random_prompts)
        return self.generate(prompt, style)
    
    def edit(self, skin_id: str, modification: str) -> Skin:
        """Edit existing skin"""
        if skin_id not in self.skins:
            raise ValueError(f"Skin not found: {skin_id}")
        
        original_skin = self.skins[skin_id]
        enhanced_prompt = f"{original_skin.prompt}, {modification}"
        
        return self.generate(enhanced_prompt, original_skin.style)
    
    def enhance(self, image: Image.Image, enhancement: str) -> Skin:
        """Enhance an image"""
        prompt = f"enhance and improve, {enhancement}"
        enhanced_prompt = f"{prompt}, minecraft skin, high quality, detailed"
        
        images = self.model_manager.generate(enhanced_prompt)
        skin = Skin(images[0], enhancement, "enhanced")
        self.skins[skin.id] = skin
        
        return skin
    
    def list_skins(self) -> list:
        """List all generated skins"""
        return [skin.to_dict() for skin in self.skins.values()]
    
    def get_skin(self, skin_id: str) -> Skin:
        """Get skin by ID"""
        return self.skins.get(skin_id)
    
    def delete_skin(self, skin_id: str):
        """Delete skin"""
        if skin_id in self.skins:
            del self.skins[skin_id]
            logger.info(f"Skin deleted: {skin_id}")


def load_image(path: str) -> Image.Image:
    """Load image from file"""
    return Image.open(path).convert('RGB')


def save_image(image: Image.Image, path: str):
    """Save image to file"""
    image.save(path)
    logger.info(f"Image saved to {path}")
