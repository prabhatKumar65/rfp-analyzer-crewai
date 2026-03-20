from crewai import Task
from agents import research_agent, summary_agent, risk_agent

def create_tasks(rfp_text):
    
    # Task 1 for Research Agent
    research_task = Task(
        description=f"""Analyze the following RFP document text and extract key information. 
        RFP TEXT:
        {rfp_text}
        
        You must identify and extract exactly:
        1. Agency / organization name
        2. Submission deadline
        3. Budget (if available)
        4. Required skills
        5. Deliverables""",
        expected_output="""A structured list containing:
        Agency: [Name]
        Deadline: [Date]
        Budget: [Amount]
        Required Skills: [Comma separated list]
        Deliverables: [Comma separated list]""",
        agent=research_agent
    )

    # Task 2 for Summary Agent
    summary_task = Task(
        description="""Based on the information extracted by the Research Agent, create a short summary of the RFP.""",
        expected_output="""A summary containing exactly these three sections:
        Executive Summary: [Short description]
        Key Requirements: [Short description]
        Suggested Approach: [Short description]""",
        agent=summary_agent
    )

    # Task 3 for Risk Analysis Agent
    risk_task = Task(
        description="""Review the original RFP text and the summaries provided. Identify any project risks, aggressive timelines, or missing information.""",
        expected_output="""A risk report containing exactly these three sections:
        Risks: [List of risks]
        Missing Information: [List of missing details]
        Questions to Ask Client: [List of questions to clarify scope]""",
        agent=risk_agent
    )
    
    return [research_task, summary_task, risk_task]