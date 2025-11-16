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
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto",
    db=db,
    add_history_to_context=True,
    num_history_runs=3
)

agent.print_response("Qual a cotação atual da Petrobras?", session_id="petrobras_session", user_id="analista_petrobras")
agent.print_response("Qual a cotação atual da Vale?", session_id="vale_session", user_id="analista_vale")
agent.print_response("Quais empresas já consultamos a contação?", session_id="petrobras_session", user_id="analista_empresas")