from app.agents.base import SimpleAgent
from agno.tools.parallel import ParallelTools
from app.models import SelectedSolution


class EngineerAgent(SimpleAgent):
    """Designs technical solutions."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__(
            "Engineer", 
            "engineer", 
            SelectedSolution,
            tools=[ParallelTools(enable_search=True, enable_extract=True)],
            user_id=user_id
        )
    
    def find_solutions(self, investigator_json: str) -> SelectedSolution:
        return self._run(investigator_json=investigator_json)
