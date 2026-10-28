rainfall_data = {
    "2019": [78, 64, 85, 92, 104, 112, 98, 105, 97, 83, 76, 88],
    "2020": [80, 60, 88, 95, 100, 110, 102, 108, 99, 85, 78, 90],
    "2021": [82, 66, 90, 97, 105, 115, 100, 110, 101, 87, 79, 92],
    "2022": [75, 62, 86, 93, 102, 108, 96, 103, 98, 84, 77, 89],
    "2023": [79, 65, 87, 94, 101, 113, 99, 107, 100, 86, 80, 91]
}

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

averages = {}

for year in rainfall_data:
    data = rainfall_data[year]
    total = sum(data)
    average = total / len(data)
    averages[year] = average

    ordered = sorted(data)
    middle = len(ordered) // 2
    median = ordered[middle]

    wettest = months[data.index(max(data))]
    driest = months[data.index(min(data))]

    print("Year " + year)
    print("  Total rainfall: " + str(total) + " mm")
    print("  Average month:  " + str(round(average, 1)) + " mm")
    print("  Median month:   " + str(median) + " mm")
    print("  Wettest month:  " + wettest + " (" + str(max(data)) + " mm)")
    print("  Driest month:   " + driest + " (" + str(min(data)) + " mm)")
    print()

# Sort the years by average rainfall, highest first, using a lambda
sortedYears = sorted(averages, key=lambda year: averages[year], reverse=True)
print("Years from wettest to driest (by average): " + str(sortedYears))
print("Wettest year: " + sortedYears[0])
print("Driest year: " + sortedYears[-1])
