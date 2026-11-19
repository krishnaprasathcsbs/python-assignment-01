# Q3: Online Shopping Discount Eligibility

# 1. Accept order amount and membership status
order_amount = float(input("Enter order amount (in Rs.): "))
membership = input("Are you a member? (yes/no): ")

# 2. Handle membership input without case sensitivity (and ignore extra spaces)
membership = membership.strip().lower()

# 3. Validate: amount must be between 0 and 1,00,000 (inclusive)
valid_amount = order_amount >= 0 and order_amount <= 100000
valid_membership = membership == "yes" or membership == "no"

if not valid_amount:
    print("Invalid order amount. It must be between Rs.0 and Rs.1,00,000.")
elif not valid_membership:
    print("Invalid membership status. Please enter 'yes' or 'no'.")
else:
    # 4. Determine the discount percentage
    if order_amount >= 5000:
        discount_percent = 15
        status = "Eligible: 15% discount for orders of Rs.5,000 or more"
    elif membership == "yes" and order_amount >= 2000:
        # Reaching here means the amount is >= 2000 and < 5000
        discount_percent = 10
        status = "Eligible: 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for a discount"

    # 5. Calculate and display results
    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    print("Original amount :", order_amount)
    print("Discount amount :", discount_amount)
    print("Final payable   :", final_amount)
    print("Status          :", status)
