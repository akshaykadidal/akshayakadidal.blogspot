# -*- coding: utf-8 -*-
"""Crew_AI_Get_Fortune_500_Company_Leaders.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QL4wFDh_ZU5jimU2ZcALQxzuOy8muDdn
"""

!pip install crewai litellm

!pip install -U duckduckgo-search

import os
from crewai import Agent, Task, Crew, Process
from litellm import completion
import pandas as pd
import requests
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

# Set Azure OpenAI credentials
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_API_BASE"] = "https://Phi-3-5-mini-instruct-iplvi.eastus2.models.ai.azure.com"
os.environ["OPENAI_API_VERSION"] = "2024-02-15-preview"  # Update this to your Azure API version

from datetime import date
from typing import List, Optional # Import Optional
from pydantic import BaseModel, Field

class CEO_Name(BaseModel):
    task_name: str = Field(..., description="Name of the CEO")
    Previous_Profession: Optional[List[str]] = Field(None, description="List of previous professions") # Make this optional
    Education_Background: Optional[str] = Field(None, description="Education background of the CEO") # Make this optional
    CEO_since: Optional[date] = Field(None, description="Appointment date of the current CEO") # Make this optional

# Configure LiteLLM for Azure
completion_model = {
    "model": "Phi-3-5-mini-instruct-iplvi",
    "api_type": "azure",
    "api_key": os.getenv("AZURE_API_KEY"),
    "api_base": os.getenv("AZURE_API_BASE"),
    "api_version": "2024-02-15-preview"  # Update this to your Azure API version
}

# Create the planner agent
Researcher = Agent(
    role="Expert Researcher",
    goal="Research factually accurate content about leadership of {company}, a fortune 500 company",
    backstory="""You're are a journalist for a reputed American publisher
              You have been tracking {company} and it's leadership for many years
              You collect information that helps board members make informed decisions
              about choice of leadership hire and promotion.""",
    allow_delegation=False,
    llm_config=completion_model,  # Use llm_config instead of llm
    verbose=True
)



Stock_Analyst = Agent(
    role="FINRA stock analyst",
    goal="Evaluate health of the company post an event",
    backstory="Your are a SRO certified FINRA stock analyst"
              "You have been tracking {company} and it's leadership changes for many years"
              "Have a master's degree in finance or Chartered Financial Analyst (CFA) designation",
    allow_delegation=False,
    llm_config=completion_model,
    verbose=True
)

Psychologist = Agent(
    role="Industrial-Organizational (I-O) Psychologist",
    goal="Assess the personality type of the leader",
    backstory="You are a PhD holder in Industrial psychology"
              "You specialize in evaluating the personality types of executives"
              "your PhD thesies was evaluating personality type based on what people say and write"
              "You Have expertise in understanding personality types"
              "You deeply Understand how personality traits relate to job performance"
              "You Can interpret complex psychological data in a business context",
    allow_delegation=False,
    llm_config=completion_model,
    verbose=True
)

# Create a task
Find_CEO= Task(
    description="Find out who is or was the CEO of the fortune 500 company {company}"
    " Findout more about the CEO, their education background, pervious roles associated with their education"
    " When did the person appointed CEO of {company}?",
    agent=Researcher,
    expected_output="Full name of the CEO"
    "CEO's Background"
    "CEO's Appointment Date",
    search_tool=search,
     output_pydantic=CEO_Name,
    verbose=True
)



Find_CEO_Crew = Crew(
  agents=[
    Researcher
  ],
  tasks=[
    Find_CEO
  ],
  verbose=True
)

inputs = {
  'company': 'Amazon'
}

Result = Find_CEO_Crew.kickoff(
  inputs=inputs
)

Result

Result

url = "https://fortune.com/ranking/global500/"
tables = pd.read_html(url)

df_f5_2024 = tables[0]

url = "https://fortune.com/ranking/global500/2004/"
tables = pd.read_html(url)
df_f5_2004 = tables[0]


