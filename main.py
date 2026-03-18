customer_name = str(input("Enter your name: "));
product_name = str(input("Enter product name: "));
price = float(input("Enter price per unit in KZT: "));
quantity = int(input("Enter quantity: "));
subtotal = price * quantity;
discount = 0.10 * subtotal if subtotal > 5000 else 0;
total = subtotal - discount;
print("=" * 30)
print(" " * 8 + "SHOP RECEIPT")
print("=" * 30)
print(f"Customer: {customer_name}")
print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Discount: {discount}")
print(f"Total: {total}")
print("=" * 30)
print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)