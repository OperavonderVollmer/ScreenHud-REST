from REST.REST import app
from dotenv import load_dotenv
import os

load_dotenv()

HUD_HOST = str(os.getenv("HUD_HOST", "127.0.0.1"))
HUD_PORT = int(os.getenv("HUD_PORT", 56000))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=HUD_HOST, port=HUD_PORT)