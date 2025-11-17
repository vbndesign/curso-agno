from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

import os
load_dotenv()

# Setup SQLite database
db = SqliteDb(db_file="tmp/data.db")

agent = Agent(
    name="Analista Financeiro",
    model=OpenAIChat(id="gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[YFinanceTools()],
    instructions="Você é um analista e tem diferentes clientes. Lembre-se de cada clieente, suas informações e preferências.",
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    enable_user_memories=True,
    enable_agentic_memory=True
)

# agent.print_response("Olá, prefiro as respostas em formato de tabelas, gosto de poucas informações.", session_id="petrobras_session_1", user_id="analista_petrobras")
# agent.print_response("Olá, prefiro as respostas em formato de texto, gosto de bastante detalhes.", session_id="vale_session_1", user_id="analista_vale")

agent.print_response("Qual a cotação atual da Petrobras?", session_id="petrobras_session_2", user_id="analista_petrobras")
agent.print_response("Qual a cotação atual da Vale?", session_id="vale_session_2", user_id="analista_vale")
