total_price = int(input("合計金額を教えてね（円）:"))
print(total_price)

number_of_people = int(input("人数を教えてね（人）:"))

print(number_of_people)

print(f"1人あたり{total_price//number_of_people}円,端数:{total_price % number_of_people}円")
