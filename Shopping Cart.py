#Shopping cart program

items = {"Pizza" : 10.99, "Meat" : 5.99, "Vegetables" : 7.99, "Fish" : 4.99, "Bread" : 1.99}

cart = []

print("------------FOODS------------")
for key, value in items.items():
    print(f"{key:<15} {value:>12.2f}")
print("-----------------------------")
print()

while True:
    shop_list = input("What items do you want to buy? (Enter Q to quit): ")
    shop_list = shop_list.capitalize()
    cart.append(shop_list)
    if "Q" in shop_list:
        cart.remove("Q")
        break

def result():
    result = 0
    total = 0
    total = [items[item] for item in cart if item in items]
    for x in total:
        result += x
    return result

print(result())

print("--------YOUR CART--------")
print(f"Your cart is: {cart}")
print()
print(f"Your total is: {result():.2f}")