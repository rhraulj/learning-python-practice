#  Take the price of an item and a discount percentage, calculate the final price.

price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
final_price = price - (price * discount_percentage / 100)
print(f"The final price is: {final_price}")