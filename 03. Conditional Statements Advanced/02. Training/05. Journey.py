budget = float(input())
season = input()
destination = ""
variant = ""
if budget <= 100:
    if season == "summer":
        budget *= 0.3
        destination = "Bulgaria"
        variant = "Camp"
        print(f"Somewhere in {destination}\n{variant} - {budget:.2f}")
    elif season == "winter":
        budget *= 0.7
        destination = "Bulgaria"
        variant = "Hotel"
        print(f"Somewhere in {destination}\n{variant} - {budget:.2f}")
elif 100 < budget <= 1000:
    if season == "summer":
        budget *= 0.4
        destination = "Balkans"
        variant = "Camp"
        print(f"Somewhere in {destination}\n{variant} - {budget:.2f}")
    elif season == "winter":
        budget *= 0.8
        destination = "Balkans"
        variant = "Hotel"
        print(f"Somewhere in {destination}\n{variant} - {budget:.2f}")
elif budget > 1000:
    budget *= 0.9
    destination = "Europe"
    variant = "Hotel"
    print(f"Somewhere in {destination}\n{variant} - {budget:.2f}")
