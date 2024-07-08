#from crewai_tools import XMLSearchTool
from crewai_tools import CSVSearchTool


customer = CSVSearchTool(csv='C:\Users\ASUS\OneDrive\Desktop\New folder\customer_data 1 - Copy.csv')
product = CSVSearchTool(csv='C:\Users\ASUS\OneDrive\Desktop\New folder\Products_List.csv')


#product = XMLSearchTool(xml='C:\Users\ASUS\OneDrive\Desktop\New folder\Products_List.xml')

#customer = XMLSearchTool(xml='C:\Users\ASUS\OneDrive\Desktop\New folder\customer_data  - Copy.xml')