"""
Civic Remediation Team - Intelligent Agent Coordination.
The team leader coordinates all agents and delegates tasks intelligently.
"""
from agno.agent import Agent
from agno.team import Team
from agno.models.google import Gemini

from app.memory import get_shared_db
from app.knowledge import get_civic_knowledge
from app.agents.sentinel import SentinelAgent, Pitfall
from app.agents.analyst import AnalystAgent, RootCauseAnalysis
from app.agents.engineer import EngineerAgent, VendorList
from app.agents.strategist import StrategistAgent, RankedStrategy
from app.agents.liaison import LiaisonAgent, ProposalDraft


def create_civic_team(user_id: str = "civic-system") -> Team:
    """
    Create a coordinated team of civic remediation agents.
    The team leader intelligently delegates tasks and synthesizes results.
    """
    # Create individual agents
    sentinel = SentinelAgent(user_id).agent
    analyst = AnalystAgent(user_id).agent
    engineer = EngineerAgent(user_id).agent
    strategist = StrategistAgent(user_id).agent
    liaison = LiaisonAgent(user_id).agent
    
    # Create team coordinator
    coordinator = Agent(
        name="Civic Remediation Coordinator",
        model=Gemini(id="gemini-2.0-flash"),
        reasoning=True,
        db=get_shared_db(),
        update_memory_on_run=True,
        knowledge=get_civic_knowledge(),
        search_knowledge=True,
        instructions=[
            "You coordinate a team of specialists for civic infrastructure remediation.",
            "Delegate tasks to the appropriate team member based on their expertise:",
            "- Sentinel: Identifies systemic failures and pitfalls",
            "- Analyst: Performs root cause analysis",
            "- Engineer: Finds vendor solutions",
            "- Strategist: Ranks solutions using MCDM",
            "- Liaison: Drafts partnership proposals",
            "Synthesize results from all agents into a comprehensive response.",
        ],
        user_id=user_id,
    )
    
    # Create the team
    team = Team(
        name="Civic Remediation Team",
        leader=coordinator,
        members=[sentinel, analyst, engineer, strategist, liaison],
        add_team_history_to_members=True,  # Shared context
    )
    
    return team
