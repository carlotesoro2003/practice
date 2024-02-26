price = float(50.0)
discount = float(input("Enter discount: "))

def compute_discount(price, discount):
    discount_amount = price * (discount / 100)
    amount = price - discount_amount
    return amount

def compute_change(payment, price):
    change  = payment - price
    return change


discounted_price = compute_discount(price,discount)

print("Original price: ", price)
print("Discount: ", discount)
print("Discounted price: ",discounted_price)

pay = float(input("Enter payment: "))

print("Change: " , compute_change(pay, discounted_price))
