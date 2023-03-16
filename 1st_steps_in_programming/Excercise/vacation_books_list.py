number_of_pages = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())

hours_needed = number_of_pages // pages_per_hour
days_needed = hours_needed // days_to_finish

print(days_needed)
