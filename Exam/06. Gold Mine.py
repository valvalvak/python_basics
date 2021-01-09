locations = int(input())

for location in range(locations):
    average_gold_counter = 0
    expected_average_gold = float(input())
    locations_expectation = expected_average_gold
    gold_digging_days = int(input())
    for current_gold in range(gold_digging_days):
        got_god_today = float(input())
        average_gold_counter += got_god_today
    if average_gold_counter/gold_digging_days >= locations_expectation:
        print(f"Good job! Average gold per day: {average_gold_counter/gold_digging_days:.2f}.")
    if locations_expectation > average_gold_counter/gold_digging_days:
        print(f"You need {abs(locations_expectation - average_gold_counter/gold_digging_days):.2f} gold.")
