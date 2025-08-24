from statsmodels.stats.power import TTestIndPower

# Define parameters
effect_size = 0.5  # medium difference
alpha = 0.05       # significance level
power = 0.80       # desired power

# Create power analysis object
analysis = TTestIndPower()

# Calculate sample size per group
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')
print(f"Sample size per group: {int(sample_size)}")