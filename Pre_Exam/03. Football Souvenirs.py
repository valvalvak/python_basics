team = str(input())
souvenir = str(input())
amount_souvenir = int(input())

if team != "Argentina" and team != "Brazil" and team != "Croatia" and team != "Denmark":
    print("Invalid country!")
    sys: exit(0)

if souvenir != "flags" and souvenir != "caps" and souvenir != "posters" and souvenir != "stickers":
    print("Invalid stock!")
    sys: exit(0)

total_sum = 0

if team == "Argentina":
    if souvenir == "flags":
        total_sum = amount_souvenir * 3.25
    elif souvenir == "caps":
        total_sum = amount_souvenir * 7.20
    elif souvenir == "posters":
        total_sum = amount_souvenir * 5.10
    elif souvenir == "stickers":
        total_sum = amount_souvenir * 1.25
elif team == "Brazil":
    if souvenir == "flags":
        total_sum = amount_souvenir * 4.20
    elif souvenir == "caps":
        total_sum = amount_souvenir * 8.50
    elif souvenir == "posters":
        total_sum = amount_souvenir * 5.35
    elif souvenir == "stickers":
        total_sum = amount_souvenir * 1.20
elif team == "Croatia":
    if souvenir == "flags":
        total_sum = amount_souvenir * 2.75
    elif souvenir == "caps":
        total_sum = amount_souvenir * 6.90
    elif souvenir == "posters":
        total_sum = amount_souvenir * 4.95
    elif souvenir == "stickers":
        total_sum = amount_souvenir * 1.10
elif team == "Denmark":
    if souvenir == "flags":
        total_sum = amount_souvenir * 3.10
    elif souvenir == "caps":
        total_sum = amount_souvenir * 6.50
    elif souvenir == "posters":
        total_sum = amount_souvenir * 4.80
    elif souvenir == "stickers":
        total_sum = amount_souvenir * 0.90
print(f"Pepi bought {amount_souvenir} {souvenir} of {team} for {total_sum:.2f} lv.")
