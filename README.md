# AI RFP Analyzer (CrewAI + Ollama)

This project is a multi-agent AI workflow built with CrewAI and Python. It reads an Request for Proposal (RFP) document (PDF) and uses sequential AI agents to extract key information, generate a summary, and perform risk analysis.

## Technologies Used
- Python 3.x
- CrewAI Framework
- Ollama (Local LLM - `mistral` model)
- PyMuPDF (for document extraction)

## Setup Instructions

1. **Install Ollama & Download Model:**
   Ensure Ollama is installed on your system. Open a terminal and pull the Mistral model:
   `ollama run mistral`

2. **Set up the Python Environment:**
   Create a virtual environment (optional but recommended) and install the dependencies:
   `pip install -r requirements.txt`

3. **Add the Input File:**
   Ensure the `sample_rfp.pdf` file is placed in the root directory of this project.

## How to Run the Program

To execute the multi-agent workflow, simply run the main script:
`python main.py`

The system will sequentially trigger the Research Agent, Summary Agent, and Risk Analysis Agent. The final structured report will be printed in the terminal.
