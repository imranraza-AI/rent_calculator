## 🏠 Shared Rent & Expense Splitter
### 📌 Overview
This Python script helps people living together (in a hostel, flat, or shared accommodation) calculate how much each person needs to pay for shared monthly expenses.

It takes into account:
<br>• 	Rent
<br>• 	Food/snacks orders
<br>• 	Electricity usage and rate
<br>• 	Number of people sharing

### ⚙️ How It Works
1. 	User inputs:
<br>• 	Total rent for the month
<br>• 	Total food/snacks cost
<br>• 	Electricity units consumed
<br>• 	Charge per electricity unit
<br>• 	Number of people sharing the expenses
2. 	Script calculates:
<br>• 	Total electricity bill = 
<br>• 	Total shared cost = 
<br>• 	Per person cost = 
3. 	Output:
<br>• 	Displays the amount each person should pay.

### 🖥️ Example Usage
```
Enter your hostel/flat rent = 12000
Enter the amount of food ordered = 3000
Enter the total spent on electricity = 150
Enter the charge per unit = 8
Enter the number of person living in person = 3
Each person will pay =  5666.666666666667
```

### 📄 Code
```
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spent = int(input("Enter the total electricity units used = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of people living in the room = "))

total_bill = electricity_spent * charge_per_unit
total_amount = (rent + food + total_bill) / persons

print("Each person will pay = ", total_amount)
```

### End of project
