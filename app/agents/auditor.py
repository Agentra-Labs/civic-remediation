from app.agents.base import SimpleAgent
from agno.tools.parallel import ParallelTools
from pydantic import BaseModel, Field
from typing import List


class FinancialAudit(BaseModel):
    budget_allocated: str = Field(..., description="Amount allocated in official budgets")
    utilization_ratio: str = Field(..., description="Percentage of released funds actually utilized")
    stuck_funds_location: str = Field(..., description="Where the money is currently held/stuck")
    spending_gaps: List[str] = Field(..., description="Identified gaps in financial flow")


class AuditorAgent(SimpleAgent):
    """Audits financial flows and budget utilization."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__(
            "Auditor",
            "auditor",
            FinancialAudit,
            tools=[ParallelTools(enable_search=True)],
            user_id=user_id
        )
    
    def audit_finances(self, bureaucratic_json: str) -> FinancialAudit:
        return self._run(bureaucratic_json=bureaucratic_json)
