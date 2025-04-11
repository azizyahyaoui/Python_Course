print("---------------------------------------------------------------------------------------")

weight = float(input("Plz Enter the weight to convert: "))
unit = input("Plz chose the unit to convert from, for Kilograms or Pound? (K or L): ")

if unit == "K" or unit == "k" :
  weight *= 2.205
  unit = "Lbs."
  print(f"Your weight is: {round(weight, 1)}{unit}")
elif unit == "L" or unit == "l" :
  weight /= 2.205
  unit = "Kgs."
  print(f"Your weight is: {round(weight, 1)}{unit}")
else:
  print(f"{unit} was not a valid unit, try again using (K or L)")



print("---------------------------------------------------------------------------------------")
