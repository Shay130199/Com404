# Read current amount from user 
print("Please enter current amount (£)")
current_amount = float( input() )

# Read interest rate from user 
print("Please enter interest rate (%)")
interest_rate = float( input() )

# Calculate new amount
interest_amount = (interest_rate / 100) * current_amount
new_amount = current_amount + interest_amount

# Display the result 
print("The new amount is £" + str(new_amount) )
