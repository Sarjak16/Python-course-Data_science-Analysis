
# To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.


# Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.

# Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.

# Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.\
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 =  uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1- uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - \
                        uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)


# stimulating wait times.............................................................................
# \Set the random seed to 334.
# Set random seed to 334
np.random.seed(334)
# Import uniform from scipy.stats.

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as wait_times.
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, 1000)
print(wait_times)

#Create a histogram of the simulated wait times and show the plot.
\# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()
