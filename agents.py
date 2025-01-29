import os 
import smolagents
from smolagents import CodeAgent, HfApiModel
from dotenv import load_dotenv
import openai 
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)


hf_api_key = os.getenv("HF_TOKEN")




model = HfApiModel()

agent =CodeAgent(tools=[],model=model)

print(agent.run("who won the BGT 2024"))






