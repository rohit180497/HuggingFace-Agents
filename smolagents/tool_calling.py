from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, HfApiModel
from langchain.agents import load_tools


agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")