from typing import List, Optional
from agno.tools.parallel import ParallelTools
from pydantic import BaseModel, Field

from app.agents.base import SimpleAgent


class FundingSource(BaseModel):
    """A specific funding opportunity for civic projects."""
    source_name: str = Field(..., description="Name of the funding program/grant/foundation")
    source_type: str = Field(..., description="Type: nonprofit grant, government program, philanthropic foundation, etc.")
    funding_amount: str = Field(..., description="Amount available (range or specific)")
    eligibility: str = Field(..., description="Key eligibility requirements")
    application_url: str = Field(..., description="URL to apply or learn more")
    deadline: Optional[str] = Field(None, description="Application deadline if available")


class FundingPlan(BaseModel):
    """Comprehensive funding plan for a civic remediation project."""
    project_cost_estimate: str = Field(..., description="Estimated total cost of the project")
    funding_sources: List[FundingSource] = Field(..., description="List of potential funding sources")
    funding_strategy: str = Field(..., description="Strategy for securing funding (phased approach, partnerships, etc.)")
    timeline_estimate: str = Field(..., description="Estimated timeline for funding acquisition")


class LiaisonAgent(SimpleAgent):
    """
    Funding Coordinator Agent - Finds funding opportunities and estimates costs
    for civic remediation projects. Uses Parallel Tools for comprehensive research.
    """
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__(
            "Liaison",
            "liaison",
            FundingPlan,
            tools=[ParallelTools(enable_search=True, enable_extract=True)],
            user_id=user_id
        )

    def create_funding_plan(self, project_description: str, location: str = "") -> FundingPlan:
        """
        Create a funding plan for a civic remediation project.
        
        Args:
            project_description: Description of the project needing funding
            location: Geographic location for targeted funding search
        """
        return self._run(project_description=project_description, location=location)
