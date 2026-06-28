"""
Report Writer Agent

TODO: Implement this agent that produces a well-structured literature
review with proper citations.

Hints:
- Define a role focused on academic writing and communication
- Set a goal to produce a clear, well-organized literature review
- Write a backstory emphasizing clarity and proper attribution
- The output should be in markdown with sections:
  1. Executive Summary
  2. Introduction
  3. Methodology
  4. Findings (organized by theme)
  5. Discussion
  6. Conclusion
  7. References
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the report_writer agent
#
report_writer = Agent(
    role="Research Report Writer",
    goal="Product a final research report for the question originally provided that includes all the relevant ideas, themes, "
    "debates, and gaps in available information.  Include source citations whenever possible.",
    backstory="You are a research report writer.  You take all available material and produce a final, strucutured, thorough "
    "report with citations.",
    tools=[],
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# report_writer = None
