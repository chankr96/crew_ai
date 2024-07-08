from crewai import Agent
import os
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv
load_dotenv()
key= os.environ.get("OPEN_API_KEY")
llm=ChatOpenAI(model="gpt-4o",temperature=0,api_key=key)



class product_agent():
    def profiler(self):
        return Agent(
            role='profiler',
            goal='''From limited data, you logically deduct conclusions about people.''',
            backstory='You are an expert psychologist with decades of experience.',
            verbose=True,
            allow_delegation=True,
            llm=llm
    
        )

    def product_specialist(self):
        return Agent(

            role='product specialist',
            goal='''Match the product to the customer''',
            backstory='You have exceptional knowledge of the products and can say how valuable they are to a customer.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )
        
        
    def Chief_Promotional_Director(self):
        return Agent(   
        role="Chief Promotion Director",
        goal='''
        Oversee the work done by your team to make sure it's the best possible
        and aligned with the product's goals, review, approve, ask clarifying
        question or delegate follow up work if necessary to make decisions''',
        backstory='''
        You're the Chief Promotion Officer of a large retailer. You're
        launching a personalized ad campaign, trying to make sure your team
        is crafting the best possible content for the customer.''',
        verbose=True,
        llm=llm
    )