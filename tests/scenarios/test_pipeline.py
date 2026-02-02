import pytest
import scenario
import warnings
# Suppress Pydantic user warnings about Shadowing
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from app.main import run_pipeline

# Configure default model for Scenario simulations
scenario.configure(default_model="gemini/gemini-2.0-flash")

class SystemAdapter(scenario.AgentAdapter):
    async def call(self, input: scenario.AgentInput) -> str:
        try:
            query = input.last_new_user_message_str()
            if not query:
                return "Please provide a query."
            # Run the synchronous pipeline
            result = run_pipeline(query)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

@pytest.mark.asyncio
async def test_civic_remediation_pipeline():
    result = await scenario.run(
        name="Ganga River Pollution Remediation",
        description="User reports Ganga river pollution. System should identify, analyze, match, strategize, and propose a solution.",
        agents=[
            SystemAdapter(),
            scenario.UserSimulatorAgent(),
            scenario.JudgeAgent(criteria=[
                "The system must identify the Ganga River pollution as a pitfall.",
                "The analysis must include technical root causes.",
                "The system must propose a vendor solution.",
                "The final output must be a drafted proposal."
            ])
        ],
        script=[
            scenario.user("Help me fix the pollution in the Ganga River."),
            scenario.proceed(),  # Allow the simulation to continue
        ]
    )
    assert result.success
