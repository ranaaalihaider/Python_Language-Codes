water = int(input("Enter Amount : "))
final_amount = 0

if water < 1000:
    final_amount = 15
elif water < 20001:
    final_amount = final_amount + 15
    remaining_water = water - 1000
    result = remaining_water * 0.0175
    final_amount = final_amount + result
elif water < 30001:
    final_amount = final_amount + 15  # Adding 15 once
    final_amount = final_amount + 17.5  # Adding 17.5 without overwriting the previous value
    remaining_water = water - 2000
    result = remaining_water * 0.02
    final_amount = final_amount + result
else:
    final_amount = 70

print(final_amount)
