def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price


original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percentage)

if final_price < original_price:
    print(f" Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Final price: {original_price:.2f}")
