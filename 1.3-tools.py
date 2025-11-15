from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
# from agno.models.groq import Groq

load_dotenv()

def celsius_to_fh(temperatura_celsius: float):
    """
    Converte uma temperatura de graus Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura em graus Fahrenheit.
    """
    return (temperatura_celsius * 9/5) + 32

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        TavilyTools(),
        celsius_to_fh
        ],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura, em Fahrenheit, de hoje em Vila Velha, ES.")