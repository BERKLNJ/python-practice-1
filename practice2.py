customer_name = input("Enter your name: ")
subtotal = 0.0
counter = 0

while True:
    product_name = input("Enter product name: ")
    if product_name.lower() == "done":
        break

    price = float(input("Enter product price: "))
    counter +=1
    subtotal += price

print(f"Customer name: {customer_name}")
print(f"Total price: {subtotal} KZT")
print(f"Total number:{counter}")

print("-" * 30)
if subtotal < 3000:
    discount = 0
    print("Discount tier : No discount (0%)")
    print(f"Discount {discount} KZT")
    print(f"Total price: {subtotal} KZT")
elif subtotal >= 3000 and subtotal < 7000:
    discount = subtotal * 0.05
    final_total = subtotal - discount
    print(f"Discount tier : 5% discount")
    print(f"Discount {discount} KZT")
    print(f"Total price: {final_total} KZT")
else:
    discount = subtotal * 0.15
    final_total = subtotal - discount
    print(f"Discount tier : 15% discount")
    print(f"Discount {discount} KZT")
    print(f"Total price: {final_total} KZT")

print("-" * 30)
print("Name uppercase:" + customer_name.upper())
print("Name lowercase:" + customer_name.lower())

length = len(customer_name)
print(f"Total number of characters: {length}")
if length > 5:
    print("Long name")
else:
    print("Short name")