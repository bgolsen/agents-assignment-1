"""
Task Definitions for Research Crew

TODO: Define the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from agents import query_expander, report_writer, source_hunter, synthesizer
from crewai import Task


def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    TODO: Implement the four tasks below
    """

    # =========================================
    # Task 1: Query Expansion
    # =========================================
    # TODO: Create a task that breaks down the research question
    # into sub-questions, keywords, and search angles
    #
    expand_task = Task(
        description=f"Take the following question and break it down into several sub-questions and key "
        f"words and phrases that will help with searchng for relevant information in a set of documents \n\n"
        f"Research Question:  {research_question} \n\n"
        f"Generate 5-10 specific questions related to the research question provided. "
        f"Generate a list of key words and phrases related to the research question and include synonmyms "
        f"and alternate ways of phrases key topics and subjects",
        agent=query_expander,
        expected_output="A numbered list of questions and a list of key words and phrases",
    )

    # =========================================
    # Task 2: Source Hunting
    # =========================================
    # TODO: Create a task that searches the paper corpus
    # Hint: Use context=[expand_task] to pass the query strategy
    #
    search_task = Task(
        description="Using the sub-questions and search keywords and phrases provided by the query expansion step, "
        "search the paper corpus to retrieve the most relevant passages. Use the search_papers "
        "tool to run searches for each sub-question and keyword set, covering all the angles "
        "identified. Run each question and key word search separately.  Make sure to gather relevant information from "
        "many sources, not just the top results.  Gather enough passages to thoroughly address the research question.  "
        "For every passage you retrieve, capture its source so that it can be cited later.",
        agent=source_hunter,
        context=[expand_task],
        expected_output="An organized collection of passages from the corpus of documents, each one "
        "with a source citation.",
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    # TODO: Create a task that synthesizes findings into themes
    # Hint: Use context=[expand_task, search_task] for full context
    #
    synthesis_task = Task(
        description="Take the sub-questions from expand_task and the passages from search_task and organize and synthesize "
        "the information into a set of topics, themes, areas of debate, and gaps in information.  Think of these as sections "
        "for the full report to be created later.  Citations must be included.",
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output="A series of paragraphs each representing a distinct idea, theme, or subject, that include "
        "areas of debate, or gaps in the available information.  Citations must be included.",
    )

    # =========================================
    # Task 4: Report Writing
    # =========================================
    # TODO: Create a task that writes the final literature review
    # Hint: Use context=[expand_task, search_task, synthesis_task]
    #
    report_task = Task(
        description=f"Write a structured literature review that answers the original research question:\n"
        f"RESEARCH QUESTION: {research_question}\n\n"
        f"Use the selection ideas and themes from the synthesis step as your organizing structure, and "
        f"draw on the retrieved passages and their sources for supporting evidence. Organize the "
        f"review by theme rather than by paper. Cover the major themes, present the points of "
        f"debate or disagreement between sources, and note the gaps or open questions the "
        f"literature leaves unresolved.\n\n"
        f"Cite sources throughout using source identifiers. Every "
        f"substantive claim should be attributed to the paper(s) it came from. Write in clear, "
        f"academic prose with an introduction, a body organized into thematic sections, and a "
        f"conclusion that summarizes the state of the field and what remains open.",
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output="A complete, well-structured literature review, organized by theme. "
        "It should include an introduction that frames the research question, body sections each "
        "covering a major theme (with debates and gaps integrated), and a conclusion. Every "
        "substantive claim must be supported by an inline citation to the source paper(s), drawn "
        "from the source identifiers.",
    )

    # TODO: Return your tasks in order
    return [expand_task, search_task, synthesis_task, report_task]

    # Placeholder - replace with your implementation
    raise NotImplementedError(
        "TODO: Implement create_research_tasks() in tasks/task_definitions.py"
    )
