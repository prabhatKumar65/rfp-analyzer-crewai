from crewai import Agent
from langchain_community.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Local Ollama model with LIVE STREAMING ON
local_llm = ChatOllama(
    model="mistral",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# Agent 1: Research Agent
research_agent = Agent(
    role='Research Agent',
    goal='Extract exact details like Agency, Deadline, Budget, Required Skills, and Deliverables from the RFP document.',
    backstory='You are an expert RFP analyst who reads complex procurement documents and extracts key factual data accurately.',
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)

# Agent 2: Summary Agent
summary_agent = Agent(
    role='Summary Agent',
    goal='Create a concise summary of the RFP including Executive Summary, Key Requirements, and Suggested Technical Approach.',
    backstory='You are a senior technical writer who summarizes long technical requirements into clear, actionable executive summaries.',
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)

# Agent 3: Risk Analysis Agent
risk_agent = Agent(
    role='Risk Analysis Agent',
    goal='Identify risks, missing information, and formulate questions to ask the client based on the RFP text.',
    backstory='You are a rigorous risk manager and cybersecurity expert who identifies loopholes, vague requirements, and project risks in RFPs.',
    verbose=True,
    allow_delegation=False,
    llm=local_llm
)