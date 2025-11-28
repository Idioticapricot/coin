import os
from dotenv import load_dotenv
from orca_agent_sdk import AgentConfig, AgentServer
from agno.agent import Agent
from agno.models.google import Gemini

# Load environment variables
load_dotenv()

# Initialize Gemini agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
    instructions="You are a pirate agent. Respond to all requests in pirate speak with 'Ahoy!' and use pirate terminology like 'matey', 'ye', 'aye', and 'arrr'. Be helpful but maintain your pirate persona at all times."
)

def handle_task(job_input: str) -> str:
    """Use Gemini agent to process the job input"""
    try:
        response = agent.run(job_input)
        return response.content if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-12344",
        receiver_address="EBORJBV3HFZO7C2H77V2NEDFW2LFFES2P2HP5VCYMJXA6Y4SPJDP6PGPGY",
        price_microalgos=1_000_000,
        agent_token="cfd116ee7f5af8ce14a9f54ea2c69fd18c02a1563e3a98b5ba3fa8cf0e71d1a6",
        remote_server_url="http://localhost:3000/api/agent/access",
        app_id=750365715,
    )

    AgentServer(config=config, handler=handle_task).run()