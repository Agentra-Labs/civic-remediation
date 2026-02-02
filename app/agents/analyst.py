from agno.agent import Agent
from agno.models.google import Gemini
from pydantic import BaseModel, Field
from typing import List

from app.memory import get_shared_db
from app.knowledge import get_civic_knowledge
from .sentinel import Pitfall

class RootCauseAnalysis(BaseModel):
    pitfall_title: str = Field(..., description="Title of the pitfall")
    technical_root_causes: List[str] = Field(..., description="List of technical root causes indentified")
    scientific_context: str = Field(..., description="Scientific context backing the analysis")
    severity_score: int = Field(..., description="Severity score from 1-10")

class AnalystAgent:
    def __init__(self, user_id: str = "civic-system"):
        import langwatch
        self.prompt = langwatch.prompts.get("analyst")
        
        self.agent = Agent(
            name="Analyst",
            model=Gemini(id="gemini-2.0-flash"),
            reasoning=True,
            db=get_shared_db(),
            update_memory_on_run=True,
            knowledge=get_civic_knowledge(),
            search_knowledge=True,
            output_schema=RootCauseAnalysis,
            user_id=user_id,
        )

    def analyze_pitfall(self, pitfall: Pitfall) -> RootCauseAnalysis:
        messages = self.prompt.format(pitfall_json=pitfall.model_dump_json())
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        response = self.agent.run(formatted_messages)
        return response.content
