def analyze_temperatures(temperatures):
    """
    Analyzes weekly temperature data to find:
    1. Hottest day (highest average temperature)
    2. Coldest day (lowest average temperature)
    3. Average temperature for each day

    Parameters:
    temperatures: A 2D list with 7 sublists (one per day), each containing 24 float values.

    Returns:
    A tuple: (index of hottest day, index of coldest day, list of daily averages)
    """
    daily_averages = []

    for day in temperatures:
        total = 0
        for temp in day:
            total += temp
        average = total / 24
        daily_averages.append(average)

    hottest_day = 0
    coldest_day = 0

    for i in range(1, len(daily_averages)):
        if daily_averages[i] > daily_averages[hottest_day]:
            hottest_day = i
        if daily_averages[i] < daily_averages[coldest_day]:
            coldest_day = i

    return hottest_day, coldest_day, daily_averages

temperatures = [
    [22.0] * 24,  # Day 0
    [25.0] * 24,  # Day 1
    [18.0] * 24,  # Day 2
    [21.0] * 24,  # Day 3
    [24.0] * 24,  # Day 4
    [23.0] * 24,  # Day 5
    [20.0] * 24   # Day 6
]

hottest, coldest, averages = analyze_temperatures(temperatures)

print("Hottest Day Index:", hottest)
print("Coldest Day Index:", coldest)
print("Average Temperatures for Each Day:", averages)
