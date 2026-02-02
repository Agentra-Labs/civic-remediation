from dotenv import load_dotenv
import sys

# Import agents (legacy pipeline)
from app.agents.sentinel import SentinelAgent
from app.agents.analyst import AnalystAgent
from app.agents.engineer import EngineerAgent
from app.agents.strategist import StrategistAgent
from app.agents.liaison import LiaisonAgent

# Import team (intelligent delegation)
from app.team import create_civic_team

load_dotenv()


def run_pipeline(query: str = "Pollution of the Ganga River") -> str:
    """
    Legacy sequential pipeline for backward compatibility.
    Each agent runs in sequence, passing structured outputs.
    """
    print(f"--- Starting Civic Remediation Pipeline for: {query} ---")
    
    # 1. Ingestion
    print("\n[Sentinel] Scanning for pitfalls...")
    sentinel = SentinelAgent()
    pitfall = sentinel.search_for_pitfalls(query)
    print(f"  Identified pitfall: {pitfall.title}")
    
    # 2. Analysis
    print("\n[Analyst] Analyzing root causes...")
    analyst = AnalystAgent()
    analysis = analyst.analyze_pitfall(pitfall)
    print(f"  Identified {len(analysis.technical_root_causes)} root causes")
    
    # 3. Matching
    print("\n[Engineer] Searching for vendors...")
    engineer = EngineerAgent()
    vendors = engineer.find_solutions(analysis)
    print(f"  Found {len(vendors.vendors)} vendors")
    
    # 4. Strategy
    print("\n[Strategist] Developing strategy...")
    strategist = StrategistAgent()
    strategy = strategist.develop_strategy(vendors)
    print(f"  Strategy selected: {strategy.selected_strategy[:50]}...")
    
    # 5. Execution
    print("\n[Liaison] Drafting proposal...")
    liaison = LiaisonAgent()
    proposal = liaison.create_proposal(strategy)
    
    return f"Proposal for {proposal.vendor_name}:\n{proposal.proposal_title}\n{proposal.email_draft}"


def run_team(query: str = "Pollution of the Ganga River") -> str:
    """
    Team-based intelligent delegation mode.
    The coordinator decides which agents to invoke and synthesizes results.
    """
    print(f"--- Starting Civic Remediation Team for: {query} ---")
    
    team = create_civic_team()
    response = team.run(query)
    
    return response.content


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "Pollution of the Ganga River"
    mode = sys.argv[2] if len(sys.argv) > 2 else "pipeline"
    
    if mode == "team":
        print("Using Team mode (intelligent delegation)")
        result = run_team(query)
    else:
        print("Using Pipeline mode (sequential)")
        result = run_pipeline(query)
    
    print("\n--- Final Result ---")
    print(result)
