# Example: Fitness Tracker Comparisons
# Let's compare various fitness metrics

# Daily step counts
steps_today = 8452
steps_yesterday = 7895
recommended_steps = 10000

# Calorie intake
calories_consumed = 1850
calorie_budget = 2000

# Heart rate measurements
resting_heart_rate = 62
current_heart_rate = 112
max_heart_rate = 185

# Step count comparisons
met_goal = steps_today >= recommended_steps             # Greater than or equal to
more_than_yesterday = steps_today > steps_yesterday     # Greater than
less_than_goal = steps_today < recommended_steps        # Less than

# Calorie comparisons
under_budget = calories_consumed <= calorie_budget      # Less than or equal to
exact_budget = calories_consumed == calorie_budget       # Equal to
not_equal_budget = calories_consumed != calorie_budget   # Not equal to

# Heart rate zone check (moderate intensity zone is 64-76% of max)
in_moderate_zone = (current_heart_rate >= 0.64 * max_heart_rate) and (current_heart_rate <= 0.76 * max_heart_rate)

print(f"Did you meet the step goal today? {met_goal}")
print(f"Did you walk more than yesterday? {more_than_yesterday}")
print(f"Are you under your step goal? {less_than_goal}")
print(f"Are you under calorie budget? {under_budget}")
print(f"Did you hit exact calorie budget? {exact_budget}")
print(f"Did you deviate from calorie budget? {not_equal_budget}")
print(f"Are you in moderate heart rate zone? {in_moderate_zone}")