world_record = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())
slowdown = (distance_in_meters // 15) * 12.5
iv_dist_time = distance_in_meters * time_in_seconds_per_meter + slowdown
difference = world_record - iv_dist_time
if iv_dist_time < world_record:
    print(f" Yes, he succeeded! The new world record is {iv_dist_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")
