print("---------------------------------------------------------------------------------------")

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.50,
        "lemonade":4.25}

cart = []
total = 0

print("--------------- OUR MENU: ---------------")

for key, value in menu.items():
  print(f"{key:10}: {value:.2f}DT")
print()

print("-----------------------------------------")

while True:
  cart_item = input("Select an item to buy (q to quit!): ").lower()
  if cart_item == "q":
    break
  elif menu.get(cart_item) is not None:
    cart.append(cart_item)


print("--------------- YOUR ORDER: ---------------")

for cart_item in cart:
  total += menu.get(cart_item)

print(cart)
print(f"The Total to pay is: {total:.2f}DT.")  


print("-------------------------------------------")




print("---------------------------------------------------------------------------------------")
