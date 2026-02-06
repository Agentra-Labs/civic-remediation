from app.agents.base import SimpleAgent
from app.models import SelectedDepartment


class BureaucratAgent(SimpleAgent):
    """Maps responsible government departments."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__("Bureaucrat", "bureaucrat", SelectedDepartment, user_id=user_id)
    
    def map_bureaucracy(self, investigation_json: str) -> SelectedDepartment:
        return self._run(investigation_json=investigation_json)
