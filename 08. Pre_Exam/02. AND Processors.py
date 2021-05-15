cpu_target = int(input())
workers = int(input())
workdays = int(input())

work_time = workers * workdays * 8
job_done = int(work_time / 3)
difference = abs(cpu_target - job_done) * 110.10

if job_done >= cpu_target:
    print(f"Profit: -> {difference:.2f} BGN")
else:
    print(f"Losses: -> {difference:.2f} BGN")
