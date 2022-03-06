#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult_total_fare = no_of_adults * 37550
    child_total_fare = no_of_children * 37550/3
    service_tax = 0.07*(adult_total_fare+child_total_fare)
    sub_total = adult_total_fare + child_total_fare + service_tax
    total_ticket_cost = 0.9 * sub_total

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)