from pydantic import BaseModel,Field
from agents import Agent,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)


groq_api_key = os.getenv('GROQ_API_KEY')
openrouter_api_key= os.getenv("OPENROUTER_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPEN_ROUTER_URL="https://openrouter.ai/api/v1"
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
openrouter_client=AsyncOpenAI(base_url=OPEN_ROUTER_URL,api_key=openrouter_api_key)
llama_scout = OpenAIChatCompletionsModel(model="meta-llama/llama-4-scout-17b-16e-instruct", openai_client=groq_client)
gemma=OpenAIChatCompletionsModel(model="google/gemma-4-26b-a4b-it:free",openai_client=openrouter_client)

writer_instructions = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 2-4 pages of content, at least 1000 words."
)

class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final report")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="WriterAgent",
    instructions=writer_instructions,
    model=gemma,
    output_type=ReportData,
)