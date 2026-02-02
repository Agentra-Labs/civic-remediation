from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.parallel import ParallelTools
from pydantic import BaseModel, Field

from app.memory import get_shared_db
from app.knowledge import get_civic_knowledge

class Pitfall(BaseModel):
    title: str = Field(..., description="Title of the systemic failure")
    description: str = Field(..., description="Detailed description of the issue")
    metrics: str = Field(..., description="Hard metrics describing the scale (e.g., '12B liters waste')")
    source_url: str = Field(..., description="URL of the source news/report")

class SentinelAgent:
    def __init__(self, user_id: str = "civic-system"):
        from app.utils import get_agent_prompt
        self.prompt = get_agent_prompt("sentinel")
        
        self.agent = Agent(
            name="Sentinel",
            model=MistralChat(id="mistral-large-latest"),
            tools=[ParallelTools(enable_search=True)],
            reasoning=True,  # Enable chain-of-thought reasoning
            db=get_shared_db(),
            update_memory_on_run=True,
            knowledge=get_civic_knowledge(),
            search_knowledge=True,
            output_schema=Pitfall,
            user_id=user_id,
        )

    def search_for_pitfalls(self, query: str) -> Pitfall:
        messages = self.prompt.format(query=query)
        # Convert to list of dicts for Agno
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        
        response = self.agent.run(formatted_messages)
        return response.content
