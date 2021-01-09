length = float(input())                         # in meters
width = float(input()) -1                       # in meters
desk_columns = width // 0.7
desk_rows = length // 1.2
place_count = desk_rows*desk_columns-3
print(int(place_count))
