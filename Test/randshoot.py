import time

# Defines random number function
def rand_num(minimum, maximum):
    now = str(time.perf_counter())
    rnd = int(now[::-1][:3:])/1000
    return(round(minimum + rnd*(maximum-minimum)))

# Assigns a range in which numbers can be generated
# Note: if 1 or 9, it counts as the same value because it's based on rounding
# For example, as numbers from 1.5 to 2.5 get rounded to 2, meaning that both
# 1 and 9 will only have a 0.5 range of values that will round to it.
# Hence, using both the min and max value to correspond to a single value balances it out.
min = 0
max = 10

# Generates random coordinates of the shot
shootX = int(rand_num(min, max))
shootY = int(rand_num(min, max))

# Temporary, to check if working
print(shootX, shootY)