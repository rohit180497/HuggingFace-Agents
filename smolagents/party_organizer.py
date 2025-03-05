from huggingface_hub import login
from huggingface_hub import whoami
# print(whoami())
from smolagents import CodeAgent,tool, DuckDuckGoSearchTool, HfApiModel

# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

# agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")