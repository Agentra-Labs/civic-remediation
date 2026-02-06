from app.agents.base import create_agent
from agno.tools.parallel import ParallelTools
from app.utils import get_agent_prompt

from app.models import SelectedCause


class InvestigatorAgent:
    """Investigates root causes and selects the most critical one."""
    
    def __init__(self, user_id: str = "civic-system"):
        self.prompt = get_agent_prompt("investigator")
        self.user_id = user_id
        
        self.agent = create_agent(
            name="Investigator",
            slug="investigator",
            tools=[ParallelTools(enable_search=True, enable_extract=True)],
            output_schema=SelectedCause,
            user_id=user_id
        )

    def investigate(self, problem_context: str) -> SelectedCause:
        """Investigate root causes given a problem context."""
        messages = self.prompt.format(signal_json=problem_context)
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        response = self.agent.run(formatted_messages)
        return response.content
