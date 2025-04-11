# we utilize lists  cause the tuple are unchangeable and  sets not ordered and doesn't accept duplication
foods = []
prices = []
total = 0

print("---------------------------------------------------------------------------------------")

while True:
  food = input("Enter the food to buy (press q to quit!): ")
  if food.lower() == "q":
    break
  
  else:
    foods.append(food)
    price = float(input(f"Enter the price of the {food}: $"))
    prices.append(price)


print("----------- YOUR CART ITEMS :-----------------")

for food in foods:
  print(food, end=" ")
print()

print("----------- TOTAL :-----------------")
for price in prices:
  total += price
print(f"Your total to pay is: ${total:.2f}")







print("---------------------------------------------------------------------------------------")
