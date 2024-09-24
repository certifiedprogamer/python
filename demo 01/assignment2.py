# Kerry Sowers
coffee = input("Select your coffee (Espresso, Latte, or Cappuccino): ")
coffee = coffee.lower()
selection = ["espresso", "latte", "cappuccino"]
if coffee in selection:
    print(f"Preparing your {coffee.title()}...")
else:
    print("Invalid selection.")
