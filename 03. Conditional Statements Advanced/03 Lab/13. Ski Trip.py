days = int(input())
room = input()
rating = input()
bedroom = 18
studio = 25
apartment = 35
price = 0
if room == "room for one person":
    price = bedroom
elif room == "apartment":
    if days < 10:
        price = studio * 0.70
    elif 10 <= days <= 15:
        price = studio * 0.65
    elif days >= 15:
        price = studio * 0.50
elif room == "president apartment":
    if days < 10:
        price = apartment * 0.90
    elif 10 <= days <= 15:
        price = apartment * 0.85
    elif days > 15:
        price = apartment * 0.80
if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.90
# if days > 1:
# days -= 1
print(f"{(days - 1) * price:.2f}")
