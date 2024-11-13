import json
"""
WITHOUT THE USE OF AI

1. Load the data
2. Loop through the list of customers
    - for each customer:
        print their name
        print a report header
        - for each product order
            print 
            Item Purchased, Selling Price, Unit Cost, 
            Profit per Unit, Quantity, Total Item Profit
            Total Item Price 
        -after printing all product orders:
            print Subtotal Tax (6% of subtotal) Shipping, and Order Total

3. After all customers were processed, print:
        -Total items sold on the day
        -Total profit processed

"""


def get_data():
    """Collects data from the orders file"""
    with open("orders.json", "r") as file:
        data = json.load(file)
    return data


def customer_loop(data):
    """Loop for processing orders and displaying information"""
    total_items = 0
    total_profit = 0
    for customer in range(len(data)):
        subtotal = 0
        order_total = 0
        tax = 0
        total_item_profit = 0
        total_item_price = 0
        print(f"Customer: {data[customer]["cust_name"]}")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{"Product".rjust(26, " ")}|{"Price".rjust(26, " ")}|{"Cost to produce".rjust(26, " ")}|{
              "Quantity".rjust(26, " ")}|{"Total item profit".rjust(26, " ")}|{"Total item price".rjust(26, " ")}|")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for order in data[customer]["orders"]:
            total_item_profit = order["selling_price"] - \
                order["cost_to_produce"]
            total_item_profit *= order["qty"]
            total_item_price = order["qty"] * order["selling_price"]
            subtotal += order["selling_price"] * order["qty"]
            print(f"|{order["product"].rjust(26, " ")}|{str(order["selling_price"]).rjust(26, " ")}|{
                  str(order["cost_to_produce"]).rjust(26, " ")}|{str(order["qty"]).rjust(26, " ")}|{f"{total_item_profit:.2f}".rjust(26, " ")}|{f"{total_item_price:.2f}".rjust(26, " ")}|")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            total_profit += total_item_profit
            total_items += order["qty"]
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Shipping cost: {data[customer]["shipping"]}")
        tax = subtotal * 0.06
        order_total = tax + subtotal + data[customer]["shipping"]
        print(f"Tax: {tax:.2f}")
        print(f"Order total {order_total:.2f}")

    print("--------------------------------------------")
    print(f"total items: {total_items}")
    print(f"total profit: {total_profit:.2f}")


def main():
    """Calls data and customer_loop"""
    data = get_data()
    customer_loop(data)


if __name__ == "__main__":
    main()
