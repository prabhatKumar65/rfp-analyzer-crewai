import fitz  # PyMuPDF
from crewai import Crew, Process
from tasks import create_tasks
from agents import research_agent, summary_agent, risk_agent
import os
os.environ["OTEL_SDK_DISABLED"] = "true"

def extract_text_from_pdf(pdf_path):
    print(f"Reading PDF from: {pdf_path}")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

if __name__ == "__main__":
    print("Starting RFP Analysis Workflow...")
    
    # 1. Read the PDF document
    pdf_file = "sample_rfp.pdf"
    rfp_text = extract_text_from_pdf(pdf_file)
    
    # 2. Get tasks configured with the extracted text
    tasks = create_tasks(rfp_text)
    
    # 3. Create the Crew to run sequentially
    rfp_crew = Crew(
        agents=[research_agent, summary_agent, risk_agent],
        tasks=tasks,
        process=Process.sequential, # Agents run one after another
        verbose=True
    )
    
    # 4. Execute the workflow
    print("\nExecuting AI Agents...")
    result = rfp_crew.kickoff()
    
    # 5. Print final output
    print("\n==================================================")
    print("FINAL RFP ANALYSIS REPORT")
    print("==================================================")
    print(result)