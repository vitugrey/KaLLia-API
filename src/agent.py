# ============ Importação ============= #
from typing import Optional
from loguru import logger

from agno.agent import Agent
from agno.run.agent import RunStatus
from agno.models.google import Gemini

# Importações locais de configuração e banco
from src.config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL_LLM,
    PERSONALITY,
)
from src.db import DB


# ============ Inicialização do Agente Único ============ #
def get_kallia_agent() -> Agent:
    """
    Instancia e configura o agente único KaLLia usando diretamente o Google Gemini.
    """
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY não configurada no servidor.")

    model = Gemini(id=GEMINI_MODEL_LLM, api_key=GOOGLE_API_KEY)

    return Agent(
        name="KaLLia",
        model=model,
        tools=[],
        instructions=[PERSONALITY],
        db=DB,
        add_history_to_context=True,
        num_history_runs=5,
        enable_user_memories=True,
        add_memories_to_context=True,
        add_datetime_to_context=True,
        add_location_to_context=True,
        add_name_to_context=True,
        debug_mode=True,
    )


# ============ Função de Execução Principal ============ #
def generate_response(prompt: str, session_id: str = "main_session") -> str:
    """
    Executa o agente único KaLLia com personalidade centralizada, histórico e persistência.
    Processa entrada de texto mantendo logs detalhados de cada interação.
    """
    if not prompt or not prompt.strip():
        return ""

    # Log de entrada da conversa
    logger.info("=" * 60)
    logger.info(f"[CONVERSA] Session_id: {session_id}")
    logger.info(f"[PROMPT] {prompt}")

    try:
        agent = get_kallia_agent()
        response = agent.run(
            input=prompt,
            session_id=session_id,
            user_id="Vitor Grey",
        )

        is_error = (
            getattr(response, "status", None) == RunStatus.error
            or not response.content
            or (isinstance(response.content, str) and '"error":' in response.content and '"code":' in response.content)
        )
        if is_error:
            raise RuntimeError(f"Gemini retornou erro de execução: {response.content}")

        logger.info(f"[RESPOSTA] {response.content}")
        logger.info("=" * 60)
        return response.content
    except Exception as e:
        logger.error(f"Erro no processamento da resposta: {e}")
        logger.info("=" * 60)
        return "Desculpe, ocorreu um erro ao processar a resposta no momento."


# ============= Execução (Teste) ============== #
if __name__ == "__main__":
    response = generate_response("Olá KaLLia, como você está hoje?")
    print(response)
