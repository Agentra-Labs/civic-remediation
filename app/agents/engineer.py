from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from pydantic import BaseModel, Field
from typing import List

from app.memory import get_shared_db
from .analyst import RootCauseAnalysis

class Vendor(BaseModel):
    name: str = Field(..., description="Name of the vendor/startup")
    solution: str = Field(..., description="Description of their technical solution")
    website: str = Field(..., description="Website URL if available")
    relevance_score: int = Field(..., description="Relevance to the problem 1-10")

class VendorList(BaseModel):
    vendors: List[Vendor] = Field(..., description="List of potential vendors")

class EngineerAgent:
    def __init__(self, user_id: str = "civic-system"):
        import langwatch
        self.prompt = langwatch.prompts.get("engineer")
        
        self.agent = Agent(
            name="Engineer",
            model=Gemini(id="gemini-2.0-flash"),
            reasoning=True,
            db=get_shared_db(),
            update_memory_on_run=True,
            tools=[DuckDuckGoTools()],
            output_schema=VendorList,
            user_id=user_id,
        )

    def find_solutions(self, analysis: RootCauseAnalysis) -> VendorList:
        messages = self.prompt.format(root_causes=str(analysis.technical_root_causes))
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        response = self.agent.run(formatted_messages)
        return response.content
