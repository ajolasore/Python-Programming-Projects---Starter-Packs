# Read input values
mother_age_difference = int(input())
years_from_now = int(input())
age_ratio = int(input())


# Calculate the mother's age in years
mother_age_years = ((years_from_now * (age_ratio -1)) - (age_ratio * mother_age_difference))/(1 - age_ratio)
# Calculate the mother's age in months
mother_age_months = mother_age_years*12

# Calculate the son's age in years
son_age_years = mother_age_years - mother_age_difference
# Calculate the son's age in months
son_age_months = son_age_years*12

# Print the result
print(f"The mother is {round(mother_age_months)} months old and her son {round(son_age_months)} months.")

