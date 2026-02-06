from app.agents.base import SimpleAgent
from agno.tools.parallel import ParallelTools
from app.knowledge import persist_agent_findings
from app.models import SelectedProblem


class SentinelAgent(SimpleAgent):
    """Scans for civic problems and selects the most critical one."""
    
    def __init__(self, user_id: str = "civic-system"):
        super().__init__(
            "Sentinel",
            "sentinel",
            SelectedProblem,
            tools=[ParallelTools(enable_search=True)],
            user_id=user_id
        )

    def search_for_problems(self, query: str, persist_to_kb: bool = True) -> SelectedProblem:
        """
        Search for civic problems and SELECT the ONE most critical.
        
        Args:
            query: The region or topic to scan (e.g., "Bihar infrastructure")
            persist_to_kb: If True, automatically save findings to KB for other agents
        """
        result = self._run(query=query)
        
        # Auto-persist to KB so other agents can reference these findings
        if persist_to_kb and result:
            try:
                persist_agent_findings(result, "Sentinel", query)
            except Exception as e:
                print(f"[KB] Warning: Failed to persist findings: {e}")
        
        return result
