
# Read input values
grand_prix_name = input()
lap_distance_km = float(input())
average_lap_time_min = float(input())

# Calculate the number of laps to exceed 305 kilometers
min_laps_to_exceed_305_km = int(305 / lap_distance_km) + 1

# Calculate the number of laps based on the two-hour time limit (120 minutes)
max_laps_for_two_hours = int(120 / average_lap_time_min) + 1

# Determine the final number of laps, considering the exceptions
if grand_prix_name == "Monaco":
    total_laps = 78
elif max_laps_for_two_hours < min_laps_to_exceed_305_km:
    total_laps = max_laps_for_two_hours
else:
    total_laps = min_laps_to_exceed_305_km

# Calculate the total distance
total_distance_km = total_laps * lap_distance_km

# Print the result
print(f"The Grand Prix of {grand_prix_name} runs over {total_laps} laps ({total_distance_km} km).")


