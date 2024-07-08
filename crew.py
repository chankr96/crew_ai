from crewai import Crew,Process
from Agent import *
from agents.Agent import Chief_Promotional_Director
from task import select_3_products_task
from Tools import product,customer

Chief_Promotional_Director=product_agent.Chief_Promotional_Director
profiler= product_agent.profiler
product_specialist=product_agent.product_specialist
my_crew = Crew(
   agent =[Chief_Promotional_Director,profiler,product_specialist],
   task = [select_3_products_task],
   process=Process.sequential,
    full_output=True,
    verbose=True,
    max_rpm = 100,
    memory = True
)

result =  my_crew.kickoff(agents=[Chief_Promotional_Director], task=[select_3_products_task])
print(result)