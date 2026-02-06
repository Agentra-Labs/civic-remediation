"""
Singleton Pipeline Workflow - Converging Civic Remediation.

Implements the "one thing at a time" principle:
Problem → Cause → Department → Solution → Funding → Project Launch

Each stage receives the previous output and MUST select exactly ONE item,
creating a converging flow toward a cohesive remediation blueprint.
"""
from typing import Optional
from agno.workflow import Workflow, Step, StepInput, StepOutput

from app.models import (
    SelectedProblem,
    SelectedCause,
    SelectedDepartment,
    SelectedSolution,
    SelectedFunding,
    RemediationBlueprint,
    PipelineContext,
)
from app.agents.base import create_agent, POLLINATIONS_BASE_URL, DEFAULT_MODEL
from app.knowledge import get_shared_db


# =============================================================================
# Stage Configuration (KISS: Data-driven instead of repetitive functions)
# =============================================================================
STAGES = [
    ("1. Select ONE Problem", "Problem Selector", "sentinel", SelectedProblem, 
     "Analyze civic problems and SELECT the SINGLE most critical one to address."),
    ("2. Identify ONE Cause", "Cause Identifier", "investigator", SelectedCause,
     "Investigate root causes and SELECT the SINGLE most critical factor."),
    ("3. Map ONE Department", "Department Mapper", "bureaucrat", SelectedDepartment,
     "Map government bodies and SELECT the ONE most responsible department."),
    ("4. Design ONE Solution", "Solution Designer", "engineer", SelectedSolution,
     "Evaluate interventions and SELECT the SINGLE most effective solution."),
    ("5. Match ONE Funding", "Funding Matcher", "liaison", SelectedFunding,
     "Search funding sources and SELECT the ONE best-matched programme."),
]


def _create_stage_step(name: str, agent_name: str, slug: str, schema, description: str) -> Step:
    """Create a pipeline stage step from config."""
    agent = create_agent(
        name=agent_name,
        slug=slug,
        output_schema=schema,
        enable_reasoning_tools=False,
    )
    return Step(name=name, agent=agent, description=description)


# =============================================================================
# Stage 6: Blueprint Synthesis
# =============================================================================
def synthesize_blueprint(step_input: StepInput) -> StepOutput:
    """
    Final synthesis step: Combine all singleton selections into a
    cohesive RemediationBlueprint for project launch.
    
    This is a custom function that aggregates the pipeline outputs.
    """
    # Get outputs from previous steps
    previous_outputs = step_input.previous_outputs or []
    
    # Extract singleton selections from each stage
    problem: Optional[SelectedProblem] = None
    cause: Optional[SelectedCause] = None
    department: Optional[SelectedDepartment] = None
    solution: Optional[SelectedSolution] = None
    funding: Optional[SelectedFunding] = None
    
    for output in previous_outputs:
        content = output.content
        if isinstance(content, SelectedProblem):
            problem = content
        elif isinstance(content, SelectedCause):
            cause = content
        elif isinstance(content, SelectedDepartment):
            department = content
        elif isinstance(content, SelectedSolution):
            solution = content
        elif isinstance(content, SelectedFunding):
            funding = content
    
    # Synthesize the final blueprint
    if all([problem, cause, department, solution, funding]):
        blueprint = RemediationBlueprint(
            problem=problem,
            cause=cause,
            department=department,
            solution=solution,
            funding=funding,
            project_title=f"{solution.solution_title} for {problem.title}",
            executive_summary=(
                f"This project addresses {problem.title} in {problem.location} "
                f"by tackling the root cause of {cause.cause_title}. "
                f"The {solution.solution_title} approach will be implemented by {department.name} "
                f"with funding from {funding.programme_name}."
            ),
            total_budget_estimate=solution.estimated_cost_tier,
            pilot_phase_scope=f"Initial pilot in {problem.location}",
            key_stakeholders=f"{department.name}, {funding.organization}",
            next_steps=(
                f"1. Engage {department.name} for formal partnership. "
                f"2. Submit application to {funding.programme_name}. "
                f"3. Prepare pilot scope for {problem.location}."
            ),
        )
        return StepOutput(content=blueprint)
    else:
        return StepOutput(content="Error: Missing outputs from previous stages")


# =============================================================================
# Main Pipeline Factory
# =============================================================================
def create_singleton_pipeline() -> Workflow:
    """
    Create the converging singleton pipeline for civic remediation.
    
    Each stage receives the previous output and MUST select exactly ONE item.
    """
    # Generate steps from STAGES config
    steps = [_create_stage_step(*stage) for stage in STAGES]
    
    # Add final synthesis step
    steps.append(Step(
        name="6. Synthesize Blueprint",
        executor=synthesize_blueprint,
        description="Combine all singleton selections into final project blueprint.",
    ))
    
    return Workflow(
        name="Civic Remediation Singleton Pipeline",
        description=(
            "Converging pipeline: ONE problem → ONE cause → ONE department → "
            "ONE solution → ONE funding → focused project launch."
        ),
        steps=steps,
    )


__all__ = ['create_singleton_pipeline', 'RemediationBlueprint']
