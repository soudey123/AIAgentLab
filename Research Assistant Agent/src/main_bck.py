from dotenv import load_dotenv
from pathlib import Path
from src.crew import build_crew
from src.tools import write_file

ROOT = Path(__file__).resolve().parents[1]  # project root (folder above src)
load_dotenv(ROOT / ".env")

load_dotenv()

def run(topic: str):
    crew = build_crew(topic)
    result = crew.kickoff()
    path = write_file("output/report.md", str(result))
    print(f"\n✅ Report saved to: {path}\n")

if __name__ == "__main__":
    topic = "Competitive analysis: AI agent platforms for research + summarization"
    run(topic)
