customer_name = "  Nadjat "
film_name = "Wrong turn Movie"
ticket_price = 6.77
number_of_tickets = 2
customer_balance = 56
customer_age = 18
cinema_membership = True

cleaned_customer_name = customer_name.upper().strip()
print(cleaned_customer_name)
ticket_subtotal = ticket_price * number_of_tickets
print(ticket_subtotal)

discount = 0.85
if cinema_membership :
   final_cost = ticket_subtotal * discount
else:
   final_cost = ticket_subtotal
    

print(film_name.replace("Movie", "Film"))
print(len(cleaned_customer_name))
print(f"£{final_cost:.2f}")

if customer_age < 18:
       print("Too young")
elif customer_age >= 18 and customer_balance >= final_cost:
       print("Success")
else:
       print("Insufficient funds")

