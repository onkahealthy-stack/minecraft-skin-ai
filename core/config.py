"""Configuration for Minecraft Skin AI Generator"""
import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
SKINS_DIR = BASE_DIR / "skins"
MODELS_DIR = BASE_DIR / "models"

# Create directories
SKINS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

class Config:
    """Application configuration"""
    
    # Model settings
    MODEL_NAME = "runwayml/stable-diffusion-v1-5"
    DEVICE = "cuda"  # or "cpu"
    USE_FP16 = True  # Use half precision for faster inference
    
    # Generation parameters
    INFERENCE_STEPS = 50
    GUIDANCE_SCALE = 7.5
    HEIGHT = 512
    WIDTH = 512
    
    # Minecraft skin size (always 64x64 for standard skins)
    SKIN_HEIGHT = 64
    SKIN_WIDTH = 64
    
    # Styles
    STYLES = {
        "fantasy": "A fantasy character, magical, dragons, wizards, knights, medieval",
        "cyberpunk": "Cyberpunk character, neon colors, futuristic, high-tech, sci-fi",
        "pixel": "Pixel art character, retro, 8-bit, blocky, classic",
        "minimalist": "Minimalist character, simple shapes, clean lines, modern",
        "steampunk": "Steampunk character, gears, mechanical, brass, steam-powered",
        "anime": "Anime character, Japanese style, big eyes, colorful, manga",
        "horror": "Horror character, scary, dark, creepy, spooky, monstrous",
        "nature": "Nature character, animals, plants, forest, organic, earth tones"
    }
    
    # Server
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "False") == "True"
    
    # API
    API_TITLE = "Minecraft Skin AI Generator"
    API_DESCRIPTION = "Advanced AI-powered Minecraft skin generator"
    API_VERSION = "1.0.0"
