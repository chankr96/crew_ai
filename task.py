from crewai import Task
from Agent import Chief_Promotional_Director, product_specialist,profiler
from Tools import product,customer

select_3_products_task = Task(
    description='''You're creating a targeted marketing campaign
tailored to what we know about our customers.
For each customer, we have to choose exactly three products to promot
in the next campaign. Make sure the selection is the best possible and
aligned with the customer. Review, approve, ask clarifying question or
delegate follow up work if necessary to make decisions. When delegating
work send the full draft as part of the information.
This is the list of all the products participating in the campaign: {product}.
This is all we know so far from the customer: {customer}.
To start this campaign we will need to build first an understanding of our
customer. Once we have a profile about the customers interests, lifestyle and
means and needs, we have to select exactly three products that have the
highest chance to be bought by them.
 ''',
    
    agent= Chief_Promotional_Director,
    tools=[product,customer], 
    expected_output = '''Your final answer MUST be exactly 3 products from the list, each with a short description why it matches with this customer.'''
)