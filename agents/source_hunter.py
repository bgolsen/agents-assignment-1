"""
Source Hunter Agent

TODO: Implement this agent that searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent
from tools.paper_rag_tool import search_papers

# TODO: Create the source_hunter agent
#
source_hunter = Agent(
    role="Source Material Provider",
    goal="Take the questions and key words and phrases provided by the Research Question Assistant "
    "and search the corpus of documents for relevant material.  Execute each question and key word separately. "
    "Draw from as many relevant sources as possible, not just the top results.  Keep track of sources so they can be cited later.",
    backstory="You are a specialist in taking questions and key words and phrases and searching across many documents sources "
    "to find relevant information.  You gather all information that will be useful in later building a summary report.  You "
    "always keep track of where information came from so it can be properly cited.",
    tools=[search_papers],  # This tool is required!
    verbose=True,
    memory=True,
)

# Placeholder - replace with your implementation
# source_hunter = None
