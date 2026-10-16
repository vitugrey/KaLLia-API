import os
import uvicorn
# pyrefly: ignore [missing-import]
from src.config import HOST, PORT
# pyrefly: ignore [missing-import]
from src.logger import setup_logger

# Inicializa o logger com arquivo antes de tudo
setup_logger()

if __name__ == "__main__":
    print(f"Iniciando o servidor da KaLLia em http://{HOST}:{PORT}")
    reload = os.getenv("UVICORN_RELOAD", "false").lower() in ("1", "true")
    uvicorn.run("src.routes:app", host=HOST, port=PORT, reload=reload, reload_dirs=["src"] if reload else None)

