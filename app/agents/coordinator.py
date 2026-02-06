from app.agents.base import SimpleAgent
from pydantic import BaseModel, Field
from typing import List


class CoordinationPlan(BaseModel):
    task_force_structure: str = Field(..., description="Proposed Joint Task Force or structure")
    priority_remedies: List[str] = Field(..., description="List of administrative/systemic fixes with priority")
    timeline: str = Field(..., description="Phased timeline for intervention")
    ngo_engagement: str = Field(..., description="Specific role for NGOs/partners")


class CoordinatorAgent(SimpleAgent):
    """Designs inter-departmental coordination plans."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__("Coordinator", "coordinator", CoordinationPlan, user_id=user_id)
    
    def design_coordination(self, findings_json: str) -> CoordinationPlan:
        return self._run(findings_json=findings_json)
