#!/usr/bin/env python
"""Main entry point for Minecraft Skin AI Generator"""

import uvicorn
from core.config import Config

if __name__ == "__main__":
    print("\n🎨 Starting Minecraft Skin AI Generator")
    print(f"📡 Server: http://{Config.HOST}:{Config.PORT}")
    print("💡 Press Ctrl+C to stop\n")
    
    uvicorn.run(
        "web.app:app",
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.DEBUG
    )
