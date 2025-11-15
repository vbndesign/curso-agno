from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto"
)

agent.print_response("Qual a cotação atual da Apple e da Tesla?", stream=True)