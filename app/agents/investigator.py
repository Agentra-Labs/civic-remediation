from app.agents.base import SimpleAgent
from agno.tools.parallel import ParallelTools
from app.models import SelectedCause


class InvestigatorAgent(SimpleAgent):
    """Investigates root causes and selects the most critical one."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__(
            "Investigator",
            "investigator",
            SelectedCause,
            tools=[ParallelTools(enable_search=True, enable_extract=True)],
            user_id=user_id
        )

    def investigate(self, problem_context: str) -> SelectedCause:
        """Investigate root causes given a problem context."""
        return self._run(signal_json=problem_context)
