def ft_count_harvest_recursive():
    days = int(input("Days remaining until harvest: "))
    _count_days(days)
    print("Time to harvest!")


# Auxiliary function
# Must not take parameters directly (total = int(input(...)) happens above)
# Base case is defined below
# Printing after the recursive call gives ascending order 1, 2, 3...


def _count_days(days):
    # Base case
    if days < 1:
        return
    # Recursive case
    _count_days(days - 1)
    # Prints in ascending order 1, 2, 3...
    print(f"Day {days}")
