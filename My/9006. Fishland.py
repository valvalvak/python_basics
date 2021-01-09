mackerel_price = float(input())  # цена на скумрията на килограм.
sprat_price = float(input())  # цена на цацата на килограм.
bonito_kg = float(input())  # килограма паламуд.
h_mackerel_kg = float(input())  # килограма сафрид.
mussels_kg = int(input())  # килограма миди. Цяло число в интервала [0 ... 100]
bonito_price = bonito_kg * mackerel_price * 1.6  # Паламуд – 60% по-скъп от скумрията
h_mackerel_price = h_mackerel_kg * sprat_price * 1.8  # Сафрид – 80% по-скъп от цацата
mussels_price = mussels_kg * 7.50  # Миди – 7.50 лв. за килограм
total_bill = bonito_price + h_mackerel_price + mussels_price
print(f"{total_bill:.2f}")