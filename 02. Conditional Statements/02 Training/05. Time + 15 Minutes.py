hour = int(input())
minutes_input = int(input())
all_time_in_minutes = hour * 60 + minutes_input + 15
hours = all_time_in_minutes // 60
minutes = all_time_in_minutes % 60
if hours == 24:
    hours = 0
if minutes == 60:
    minutes = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes:}")
