from agents import Agent,WebSearchTool,trace,Runner,gen_trace_id,function_tool,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import resend
from typing import Dict
import os

NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL")

resend.api_key = os.getenv("RESEND_API_KEY")

import os
from dotenv import load_dotenv

load_dotenv(override=True)


groq_api_key = os.getenv('GROQ_API_KEY')
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
groq_client = AsyncOpenAI(base_url=GROQ_BASE_URL, api_key=groq_api_key)
gpt_oss = OpenAIChatCompletionsModel(model="openai/gpt-oss-120b", openai_client=groq_client)
llama_scout = OpenAIChatCompletionsModel(model="meta-llama/llama-4-scout-17b-16e-instruct", openai_client=groq_client)

@function_tool
def send_email(subject:str,html_body: str)->Dict[str,str]:
    """
    Send out an email with the given subject and HTML body to all sales prospects.
    """
    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",  
            "to": NOTIFICATION_EMAIL,         
            "subject": subject,
            "html": html_body
        })

        print("Resend response:", response)
        return {"status": "success"}

    except Exception as e:
        print("Resend error:", e)
        return {
            "status": "error",
            "message": str(e)
        }
    
email_instructions=""" You are able to send a nicely formated HTML email based on a deatiled report.
You will be provided with a detailed report. You should use your tool to send one email, providing the report converted
into clean , well presnted HTML with an appropriate subject line ."""

email_agent=Agent(
    name="Email Agent",
    instructions=email_instructions,
    tools=[send_email],
    model=gpt_oss,
)