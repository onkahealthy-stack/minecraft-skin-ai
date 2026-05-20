"""AI Models for skin generation"""
import torch
from diffusers import StableDiffusionPipeline
from .config import Config
import logging

logger = logging.getLogger(__name__)

class ModelManager:
    """Manages AI models for generation"""
    
    def __init__(self):
        self.device = Config.DEVICE
        self.pipeline = None
        self._load_model()
    
    def _load_model(self):
        """Load Stable Diffusion model"""
        logger.info(f"Loading model: {Config.MODEL_NAME}")
        
        try:
            if self.device == "cuda" and not torch.cuda.is_available():
                logger.warning("CUDA not available, falling back to CPU")
                self.device = "cpu"
            
            self.pipeline = StableDiffusionPipeline.from_pretrained(
                Config.MODEL_NAME,
                torch_dtype=torch.float16 if Config.USE_FP16 else torch.float32,
                safety_checker=None
            )
            
            self.pipeline = self.pipeline.to(self.device)
            
            if Config.USE_FP16 and self.device == "cuda":
                self.pipeline.enable_attention_slicing()
            
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def generate(self, prompt: str, num_inference_steps: int = None, 
                guidance_scale: float = None) -> list:
        """Generate images from prompt"""
        if not self.pipeline:
            raise RuntimeError("Model not loaded")
        
        steps = num_inference_steps or Config.INFERENCE_STEPS
        scale = guidance_scale or Config.GUIDANCE_SCALE
        
        logger.info(f"Generating with prompt: {prompt}")
        
        try:
            with torch.no_grad():
                result = self.pipeline(
                    prompt,
                    height=Config.HEIGHT,
                    width=Config.WIDTH,
                    num_inference_steps=steps,
                    guidance_scale=scale,
                    negative_prompt="blurry, low quality, distorted"
                )
            
            return result.images
        except Exception as e:
            logger.error(f"Generation error: {e}")
            raise
    
    def unload(self):
        """Unload model to free memory"""
        if self.pipeline is not None:
            del self.pipeline
            torch.cuda.empty_cache()
            logger.info("Model unloaded")
