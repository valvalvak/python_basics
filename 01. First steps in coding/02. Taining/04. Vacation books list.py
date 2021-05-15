book_pages = int(input())
pages_per_hour = int(input())
days_count_per_book = int(input())
read_speed = book_pages / pages_per_hour
estimated_time = read_speed / days_count_per_book
print(estimated_time)
