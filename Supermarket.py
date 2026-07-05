# Supermarket Billing System
#products = {
 #   "Rice": 50,
  #  "Milk": 30,
   # "Bread": 25,
    #"Eggs": 6,
    #"Apple": 100
#}
#cart = {}
#print("=================================")
#print("     SINDHU SUPERMARKET")
#print("      West Godavari")
#print("=================================")
#customer = input("Enter Customer Name: ")
#print("\nAvailable Products:")
#for item, price in products.items():
 #   print(item, "-", price)
#while True:
 #   product = input("\nEnter product name (or 'exit' to finish): ")
  #  if product.lower() == "exit":
   #     break
    #if product in products:
     #   quantity = int(input("Enter quantity: "))
      #  cart[product] = quantity
    #else:
    #    print("Product not available!")
#print("\n========== RECEIPT ==========")
#print("Customer Name:", customer)
#print("-----------------------------")
#print("Item\tQty\tPrice\tTotal")
#subtotal = 0
#for item, qty in cart.items():
 #   price = products[item]
  #  total = price * qty
   # subtotal += total
    #print(item, "\t", qty, "\t", price, "\t", total)
#tax = subtotal * 0.12
#grand_total = subtotal + tax
#print("-----------------------------")
#print("Subtotal :", subtotal)
#print("Tax (12%):", round(tax, 2))
#print("Grand Total:", round(grand_total, 2))
#print("=============================")
#print("Thank You For Shopping!")
#print("=============================")