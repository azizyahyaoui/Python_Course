import math

print("---------------------------------------------------------------------------------------")

"""
Interest Calculator:
  A= P(1 + (r/n))^t

A= final amount
P= initial principle balance
r= interest rate
t= number of time periods elapsed (in years)

"""

principle = 0
rate = 0
time = 0

while principle <= 0 :
  principle= float(input("Enter the principle amount: "))
  if principle <= 0:
    print("Principle can't be less than or equal to zero!")

while rate <= 0 :
  rate= float(input("Enter the interest rate: "))
  if principle <= 0:
    print("interest rate can't be less than or equal to zero!")

while time <= 0 :
  time= int(input("Enter the number of years: "))
  if principle <= 0:
    print("The number of years can't be less than or equal to zero!")

total_amount = principle * pow((1 + rate /100), time)

print(f"Balance amount after {time} years/s: ${total_amount:.2f}")


print("---------------------------------------------------------------------------------------")
