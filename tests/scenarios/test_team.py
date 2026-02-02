import pytest
import scenario
import warnings
# Suppress Pydantic user warnings about Shadowing
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from app.main import run_team

# Configure default model for Scenario simulations
scenario.configure(default_model="gemini/gemini-2.0-flash")

class TeamSystemAdapter(scenario.AgentAdapter):
    async def call(self, input: scenario.AgentInput) -> str:
        try:
            # The input.text is the user query
            result = run_team(input.text)
            return result
        except Exception as e:
            return f"Error running team: {str(e)}"

@pytest.mark.asyncio
async def test_civic_remediation_team():
    result = await scenario.run(
        name="Team Coordination Test",
        description="Verify that the Team coordinator delegates tasks and produces a result.",
        agents=[
            TeamSystemAdapter(),
            scenario.UserSimulatorAgent(model="gemini/gemini-2.0-flash"),
            scenario.JudgeAgent(criteria=[
                "The system must produce a final response addressing the user query.",
                "The response should indicate that multiple agents (Sentinel, Analyst, etc.) were involved either explicitly or implicitly by the depth of the answer.",
                "The output must include a proposal or solution strategy."
            ])
        ],
        script=[
            scenario.user("The city's garbage collection system is failing in Sector 7."),
            scenario.proceed(), 
        ]
    )
    assert result.success
