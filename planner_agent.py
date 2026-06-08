from pydantic import BaseModel,Field
from agents import Agent,OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os 

load_dotenv(override=True)

groq_api_key = os.getenv('GROQ_API_KEY')
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
llama_scout = OpenAIChatCompletionsModel(model="meta-llama/llama-4-scout-17b-16e-instruct", openai_client=groq_client)


HOW_MANY_SEARCHES=3

INSTRUCTIONS=f"You are a helpful research assitant. Given a query, come up with the of web searches \
to perform to best answer the query.Output {HOW_MANY_SEARCHES} terms to query for"

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")

    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")


planner_agent=Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model=llama_scout,
    output_type=WebSearchPlan,
)