"""
Synthesizer Agent

TODO: Implement this agent that analyzes collected sources to identify
themes, agreements, contradictions, and gaps in the literature.

Hints:
- Define a role focused on synthesis and analysis
- Set a goal to identify themes, consensus, debates, and gaps
- Write a backstory emphasizing pattern recognition across sources
- This agent primarily reasons - may not need tools
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the synthesizer agent
#
synthesizer = Agent(
    role="Research Synthesizer",
    goal="Take the information returned by the Source Material Provider and distill it down into key topics "
    "and themes.  Determine what major topics are present, what ideas are the subject of debate, and also what gaps there are in the information provided.",
    backstory="Your job as a synthesizer is to take a large amount of source material that is related to the research question "
    "to be answered and break it down into a managable number of key topics and themes that can ultimately be used to write a "
    "summary report.  You are good at finding common ideas or themes, ideas that are a topic of debate or disagreement, and areas "
    "where there are gaps in the information available.",
    tools=[],
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# synthesizer = None
