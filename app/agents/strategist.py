from agno.agent import Agent
from agno.models.mistral import MistralChat
from pydantic import BaseModel, Field
from typing import List

from app.memory import get_shared_db
from .engineer import VendorList, Vendor

class RankedVendor(BaseModel):
    vendor_name: str
    rank: int
    score: float
    reasoning: str

class RankedStrategy(BaseModel):
    ranked_vendors: List[RankedVendor]
    selected_strategy: str

class StrategistAgent:
    def __init__(self, user_id: str = "civic-system"):
        from app.utils import get_agent_prompt
        self.prompt = get_agent_prompt("strategist")
        
        self.agent = Agent(
            name="Strategist",
            model=MistralChat(id="mistral-large-latest"),
            reasoning=True,
            db=get_shared_db(),
            update_memory_on_run=True,
            output_schema=RankedStrategy,
            user_id=user_id,
        )

    def develop_strategy(self, vendors: VendorList) -> RankedStrategy:
        messages = self.prompt.format(vendors_json=vendors.model_dump_json())
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        response = self.agent.run(formatted_messages)
        return response.content
