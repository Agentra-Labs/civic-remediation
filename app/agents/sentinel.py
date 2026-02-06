from app.agents.base import create_agent
from agno.tools.parallel import ParallelTools
from app.utils import get_agent_prompt

from app.knowledge import persist_agent_findings
from app.models import SelectedProblem


class SentinelAgent:
    """Scans for civic problems and selects the most critical one."""
    
    def __init__(self, user_id: str = "civic-system"):
        self.prompt = get_agent_prompt("sentinel")
        self.user_id = user_id
        
        self.agent = create_agent(
            name="Sentinel",
            slug="sentinel",
            tools=[ParallelTools(enable_search=True)],
            output_schema=SelectedProblem,
            user_id=user_id
        )

    def search_for_problems(self, query: str, persist_to_kb: bool = True) -> SelectedProblem:
        """
        Search for civic problems and SELECT the ONE most critical.
        
        Args:
            query: The region or topic to scan (e.g., "Bihar infrastructure")
            persist_to_kb: If True, automatically save findings to KB for other agents
        """
        messages = self.prompt.format(query=query)
        formatted_messages = [{"role": m.role, "content": m.content} for m in messages]
        
        response = self.agent.run(formatted_messages)
        result = response.content
        
        # Auto-persist to KB so other agents can reference these findings
        if persist_to_kb and result:
            try:
                persist_agent_findings(result, "Sentinel", query)
            except Exception as e:
                print(f"[KB] Warning: Failed to persist findings: {e}")
        
        return result

