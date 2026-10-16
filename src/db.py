from loguru import logger
from agno.db.sqlite import SqliteDb
from src.config import AGENT_DB


def init_agent_db() -> SqliteDb:
    """
    Inicializa a persistência local das sessões e memórias usando SQLite.
    Salva diretamente em C:\\Users\\vitor\\Desktop\\aa\\databases\\kallia-agent.db.
    """
    logger.info(f"[BANCO] Persistência 100% local SQLite em: {AGENT_DB}")
    return SqliteDb(
        db_file=str(AGENT_DB),
        session_table="KaLLia_agents_sessions",
        memory_table="KaLLia_agents_memories",
    )


# Instância central de banco de dados compartilhada pelo agente
DB = init_agent_db()

