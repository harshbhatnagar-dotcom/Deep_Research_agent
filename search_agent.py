from agents import Agent,function_tool,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os
from tavily import TavilyClient
from agents.model_settings import ModelSettings
from dotenv import load_dotenv

load_dotenv(override=True)

tavili_api_key=os.getenv("TAVILY_API")
groq_api_key = os.getenv('GROQ_API_KEY')
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
gpt_oss = OpenAIChatCompletionsModel(model="openai/gpt-oss-120b", openai_client=groq_client)
llama_scout = OpenAIChatCompletionsModel(model="meta-llama/llama-4-scout-17b-16e-instruct", openai_client=groq_client)

@function_tool
def websearch(query:str):
    """ Search the web for the given query """
    tavily_client = TavilyClient(tavili_api_key)
    response = tavily_client.search(query)
    
    return response

INSTRUCTIONS="You are a search assitant.Given a search term, you search the web for that term and \
produce a concise summary of the results. Summary must have 2-3 paragraphs and less than 300 \
words. Capture the main points . Write succintly , no need to have complete sentences or good\
grammar. This will be consumed by someone synthesizing a report , so its vital you capture the \
essence and ignore any fluff. Do not include any additional commentry other than summary itself.\
use websearch tool for searching the web"

search_agent=Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[websearch],
    model=gpt_oss,
    model_settings=ModelSettings(tool_choice="required")
)