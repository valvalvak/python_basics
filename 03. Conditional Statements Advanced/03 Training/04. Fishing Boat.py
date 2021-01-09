# #   Цената за наема на кораба зависи от сезона и броя рибари
# #   В зависимост от сезона:
# #   •	Цената за наем на кораба през пролетта е  3000 лв.;
# #   •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# #   •	Цената за наем на кораба през зимата е  2600 лв.
# #   В зависимост от броя на групата има различна отстъпка:
# #   •	Ако групата е до 6 човека включително  –  отстъпка от 10%;
# #   •	Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
# #   •	Ако групата е от 12 нагоре  –  отстъпка от 25%.
# #   Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен -
# #   тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# #   Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# #   От конзолата се четат три реда:
# # •	Бюджет на групата – цяло число;
# # •	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# # •	Брой рибари – цяло число.
# #   ZADNICI
# budget = int(input())
# season = input()
# fishmen = int(input())
# boat_rent = 0
# if season == "Spring":
#     if fishmen <= 6:
#         boat_rent = 3000 * 0.90
#     elif 7 <= fishmen <= 11:
#         boat_rent = 3000 * 0.85
#     elif fishmen > 12:
#         boat_rent = 3000 * 0.75
# if season == "Summer" or season == "Autumn":
#     if fishmen <= 6:
#         boat_rent = 4200 * 0.90
#     elif 7 <= fishmen <= 11:
#         boat_rent = 4200 * 0.85
#     elif fishmen > 12:
#         boat_rent = 4200 * 0.75
# if season == "Winter":
#     if fishmen <= 6:
#         boat_rent = 2600 * 0.90
#     elif 7 <= fishmen <= 11:
#         boat_rent = 2600 * 0.85
#     elif fishmen > 12:
#         boat_rent = 2600 * 0.75
# if fishmen % 2 == 0 and season != "Autumn":
#     boat_rent *= 0.95
# if budget >= boat_rent:
#     print(f"Yes! You have {abs(budget - boat_rent):.2f} leva left.")
# elif budget < boat_rent:
#     print(f"Not enough money! You need {abs(budget - boat_rent):.2f} leva.")
budget = int(input())
season = input()
fishers = int(input())
boat_rent_price = 0
if season == "Spring" and fishers <= 6:
    boat_rent_price = 3000 * 0.90
elif season == "Spring" and 7 <= fishers <= 11:
    boat_rent_price = 3000 * 0.85
elif season == "Spring" and fishers > 12:
    boat_rent_price = 3000 * 0.75
elif (season == "Summer" or season == "Autumn") and fishers <= 6:
    boat_rent_price = 4200 * 0.90
elif (season == "Summer" or season == "Autumn") and 7 <= fishers <= 11:
    boat_rent_price = 4200 * 0.85
elif (season == "Summer" or season == "Autumn") and fishers > 12:
    boat_rent_price = 4200 * 0.75
elif season == "Winter" and fishers <= 6:
    boat_rent_price = 2600 * 0.90
elif season == "Winter" and 7 <= fishers <= 11:
    boat_rent_price = 2600 * 0.85
elif season == "Winter" and fishers > 12:
    boat_rent_price = 2600 * 0.75
if fishers % 2 == 0 and season != "Autumn":
    boat_rent_price *= 0.95
if budget >= boat_rent_price:
    print(f"Yes! You have {abs(budget - boat_rent_price):.2f} leva left.")
elif budget < boat_rent_price:
    print(f"Not enough money! You need {abs(budget - boat_rent_price):.2f} leva.")
