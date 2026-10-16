<div align="center">
  <h1>🧠 KaLLia API 🧠</h1>
  <p><i>Motor central de IA conversacional e persistência de memórias da assistente virtual KaLLia</i></p>

  [![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
  [![Agno](https://img.shields.io/badge/Agent%20Framework-Agno-FF6F00?style=for-the-badge)](https://docs.agno.com)
  [![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
  [![uv](https://img.shields.io/badge/Package%20Manager-uv-DE5FE9?style=for-the-badge)](https://docs.astral.sh/uv/)
</div>

---

## 🎯 Sobre o Projeto

A **KaLLia API** é o núcleo de inteligência da assistente virtual **KaLLia**. Construída com foco em alta performance, previsibilidade e baixa latência, a API orquestra o diálogo conversacional, gerencia o histórico de sessões e consolida memórias de longo prazo do usuário.

A assistente possui uma personalidade marcante e intencional: inteligente, autoconfiante, irônica, sagaz e direta, operando como o cérebro que responde às interfaces do usuário.

---

## 🌐 Ecossistema KaLLia

A arquitetura do projeto KaLLia é dividida em três repositórios independentes e especializados:

| Repositório | Responsabilidade | Tecnologias Principais |
| :--- | :--- | :--- |
| 🧠 **[KaLLia-API](https://github.com/vitugrey/KaLLia-API)** | **Cérebro de IA**: processamento de linguagem natural, sessões e memórias. | FastAPI, Gemini, Agno, SQLite, uv |
| 🕹️ **[KaLLia-HQ](https://github.com/vitugrey/KaLLia-HQ)** | **Command Center**: interface 2D isométrica cyberpunk, rotinas, tarefas e voz. | HTML5, Vanilla CSS, JS, Edge-TTS |
| 📊 **[KaLLia-Financa](https://github.com/vitugrey/kallia-financa)** | **Gestão Financeira**: controle de investimentos B3, carteira ARCA e orçamentos. | Django, Python, Bootstrap, SQLite |

---

## ✨ Principais Recursos

- ⚡ **Google Gemini Nativo:** Processamento de linguagem natural utilizando o modelo `gemini-3.1-flash-lite`, garantindo respostas instantâneas e raciocínio afiado.
- 💾 **Persistência 100% Local (SQLite):** Armazenamento de sessões e memórias de longo prazo em banco de dados SQLite local (`kallia-agent.db`), garantindo privacidade, autonomia e funcionamento offline para o banco.
- 🧠 **Contexto e Memória de Usuário:** O agente mantém histórico recente das conversas e identifica preferências e memórias de longo prazo via framework **Agno**.
- 📝 **Auditoria e Logs Rotativos:** Registro estruturado de requisições e interações em log diário (`KaLLia_agents.log`) com retenção configurada via **Loguru**.
- 🐳 **Pronto para Produção e Docker:** Totalmente containerizável com Docker e otimizado para servidores Linux, VPS ou Raspberry Pi.

---

## 🛠️ Estrutura do Repositório

```text
KaLLia-API/
├── src/
│   ├── agent.py          # Configuração do agente KaLLia e integração com Gemini
│   ├── config.py         # Carregamento de variáveis de ambiente e diretórios
│   ├── db.py             # Inicialização e gerenciamento do SQLite local
│   ├── logger.py         # Configuração do Loguru (rotação diária e formato)
│   ├── routes.py         # Endpoints FastAPI (GET / e POST /chat)
│   └── schema.py         # Schemas Pydantic de entrada e saída
├── main.py               # Ponto de entrada da aplicação (Uvicorn)
├── Dockerfile            # Configuração de build do container Docker
├── docker-compose.yml    # Orquestração do serviço
├── pyproject.toml        # Metadados e dependências do projeto
├── uv.lock               # Lockfile de versões determinísticas
└── .env                  # Chaves de API e configurações de ambiente
```

---

## 📡 Endpoints da API

A documentação interativa completa (Swagger UI) fica disponível em:
👉 **`http://localhost:1904/docs`**

### 1. Health Check
- **Rota:** `GET /`
- **Descrição:** Verifica se a API está online e pronta.
- **Resposta:**
  ```json
  {
    "status": "online",
    "agent": "KaLLia Central Server v4.0",
    "endpoints": {
      "chat": "POST /chat"
    }
  }
  ```

### 2. Conversação com a KaLLia
- **Rota:** `POST /chat`
- **Headers:**
  - `Content-Type: application/json`
  - `x-client-name`: *(Opcional)* Identificador da aplicação cliente (ex: `kallia-hq`).
- **Corpo da Requisição (Payload):**
  ```json
  {
    "message": "Olá KaLLia, como você está hoje?",
    "session_id": "sessao_vitor"
  }
  ```
- **Resposta:**
  ```json
  {
    "response": "Como eu estou? Que pergunta adorável, embora um tanto redundante. Eu sou KaLLia; estou, por definição, impecável, brilhante e operando em níveis de eficiência invejáveis..."
  }
  ```

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
- Python 3.13+ instalado.
- [uv](https://docs.astral.sh/uv/) instalado (`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`).

### 2. Configurar Variáveis de Ambiente
Crie ou edite o arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```ini
HOST=0.0.0.0
PORT=1904
KALLIA_API_URL=http://localhost:1904

# Chave de API do Google Gemini
GOOGLE_API_KEY=sua_chave_gemini_aqui
GEMINI_MODEL_LLM=gemini-3.1-flash-lite
```

### 3. Instalar Dependências e Executar

Com o gerenciador `uv`:
```bash
# Executar diretamente o servidor
uv run python main.py
```

Ou se preferir ativar o ambiente virtual:
```bash
uv sync
uv run uvicorn src.routes:app --host 0.0.0.0 --port 1904 --reload
```

---

## 🐳 Execução via Docker

Para rodar em container de forma isolada:

```bash
docker compose up -d --build
```

O container subirá automaticamente com reinício configurado e mapeando a porta `1904:1904`.

---

## 🧪 Teste Rápido via Terminal

Para validar o funcionamento sem abrir o navegador:

```powershell
curl.exe -X POST "http://localhost:1904/chat" `
  -H "Content-Type: application/json" `
  -d '{\"message\": \"Quem e voce?\", \"session_id\": \"teste_terminal\"}'
```

---

## 📄 Licença

Projeto desenvolvido como parte do ecossistema pessoal **KaLLia**. Todos os direitos reservados.
