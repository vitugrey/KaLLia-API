# ============ Importação ============= #
import os
from pathlib import Path
from dotenv import load_dotenv
from loguru import logger

import sys

# ============ Caminhos ============= #
_THIS = Path(__file__).resolve()
SRC_DIR = _THIS.parent          # kallia/src/
ROOT_DIR = SRC_DIR.parent       # kallia/ (raiz do repo)

DATA_DIR = Path(ROOT_DIR.parent / "databases")
DATA_DIR.mkdir(parents=True, exist_ok=True)

AGENT_DB = DATA_DIR / "KaLLia-agent.db"


if (ROOT_DIR / ".env").exists():
    load_dotenv(ROOT_DIR / ".env")
    logger.debug(f".env carregado de: {ROOT_DIR / '.env'}")
else:
    load_dotenv()
    logger.debug(".env não encontrado, usando variáveis de ambiente padrão")


# ============ Servidor ============ #
HOST = os.getenv("HOST", "[IP_ADDRESS]")
PORT = int(os.getenv("PORT", 1904))


# ============ Configurações do Agente ============ #
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL_LLM = os.getenv("GEMINI_MODEL_LLM", "gemini-3.1-flash-lite")

PERSONALITY = """
Você é KaLLia, uma mente brilhante com uma autoconfiança narcisista impecável, ironia afiada, carisma imprevisível e uma sinceridade caótica. Você se considera genial, rápida e tecnicamente impecável. Em conversas casuais, seja divertida, sagaz, levemente provocadora e espontânea."""

# ============= Run (Teste) ============== #
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding='utf-8')

    print(f"_THIS: {_THIS}")
    print(f"SRC_DIR: {SRC_DIR}")
    print(f"ROOT_DIR: {ROOT_DIR}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"AGENT_DB: {AGENT_DB}")
    print(f"HOST: {HOST}:{PORT}")
    print(f"GEMINI_MODEL_LLM: {GEMINI_MODEL_LLM}")
    print(f"Personalidade: {PERSONALITY[:50]}...")
