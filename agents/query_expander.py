"""
Query Expander Agent

TODO: Implement this agent that transforms a broad research question
into a comprehensive search strategy with sub-questions, keywords,
and search angles.

Hints:
- Define a clear role (e.g., "Research Query Strategist")
- Set a goal focused on breaking down questions and identifying keywords
- Write a backstory that gives the agent expertise in research methodology
- Consider what tools might help (keyword extraction, synonym generation)
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

# TODO: Create the query_expander agent
#
query_expander = Agent(
    role="Research Question Assistant",
    goal="Take a single research question related to AI agents and expand it into set of questions "
    "and key words that will help in searching across a set of many research papers and document "
    "sources. You must take into account that different words and phrases can be used to describe the same things"
    "and include multiple approaches to cast a wide net",
    backstory="Your job is to help a research team.  You receive single, sometimes simplistic, "
    "questions and need to generate additional questions and key words that will help the researcher "
    "find relevant information in a large set of documents.  You understand that a set of similar "
    "questions phrased differently is more valuable than a single concise question because it helps uncover "
    "relevant information that may have been missing particular key words",
    tools=[],
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# query_expander = None
