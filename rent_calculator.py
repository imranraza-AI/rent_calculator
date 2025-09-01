## Inputs we need from the user
## Total rent
## Total food orders for snacking
## Electricity  Uits spend
## Charge per units
## person livivng in room

## Output
## Total amount you've to pay

rent = int(input("Enter your hostal/flat rent ="))
food = int(input("Enter the amount of food ordered ="))
electricity_spent = int(input("Enter the total spent on electricity ="))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of person living in person"))

total_bill = electricity_spent * charge_per_unit

total_amount = (rent + food + total_bill)/persons
print("Each person will pay = ", total_amount)