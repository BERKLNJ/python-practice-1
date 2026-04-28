# Task A1
store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 000 0000")
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("=" * 30) # Border line [cite: 30]
# Task A2
names = []
prices = []

while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    price = float(input("Enter price: "))
    names.append(name)
    prices.append(price)

print(f"\nYour cart ({len(names)} items):")
for i in range(len(names)):
    print(f"{names[i]} {prices[i]} KZT")
# Task A3
weekly_products = set()

while True:
    product = input("Enter product name for uniqueness check (or 'done' to finish): ")
    if product.lower() == 'done':
        break
    weekly_products.add(product)

print(f"Unique products: {len(weekly_products)}")
print(weekly_products)

# Task A4
customer_name = input("Enter customer name: ")
subtotal = sum(prices)

# Tiered discount logic [cite: 85, 86, 87]
if subtotal >= 7000:
    discount_rate = 0.15
    discount_name = "Premium discount"
elif subtotal >= 3000:
    discount_rate = 0.05
    discount_name = "Standard discount"
else:
    discount_rate = 0.0
    discount_name = "No discount"

discount_amount = subtotal * discount_rate
total_price = subtotal - discount_amount

# Storing in dictionary [cite: 88, 89, 90]
receipt = {
    "customer": customer_name,
    "discount": discount_amount,
    "discount_text": discount_name,
    "items": len(names),
    "subtotal": subtotal,
    "total": total_price
}

# Final Output using dictionary access [cite: 92]
print("\n" + "=" * 30)
print("RECEIPT")
print(store_info[0])
print(f"Customer: {receipt['customer']}")
print(f"Items: {receipt['items']}")

for i in range(len(names)):
    print(f"{names[i]} {prices[i]} KZT")

print(f"Subtotal: {receipt['subtotal']} KZT")
print(f"Discount {receipt['discount']} KZT ({receipt['discount_text']})")
print(f"Total: {receipt['total']} KZT")