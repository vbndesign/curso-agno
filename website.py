from agno.agent import Agent
from agno.tools.website import WebsiteTools

agent = Agent(
    tools=[WebsiteTools()],
        markdown=True,
)
agent.print_response("Extract the main content from https://espacoaruna.com/")