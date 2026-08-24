def ft_water_reminder():
    days = input("Days since watering: ")
    days = int(days)
    if days > 2:
        print("Water the plants!")
    else:
        print("The plants are fine")
