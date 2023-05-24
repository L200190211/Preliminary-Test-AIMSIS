## Solve this:
##“In Hogwarts the currency is made up of galleon (G) and Sickle (s),
##and there are seven coins in general circulation:
##
##1s, 5s, 10s, 25s, 50s, G1(100s), and G2(200s)
##
##It's possible to make G3.5 in the following way:
##
##1xG2 +1xG1 + 4x10s +1x5s + 5x1s
##
##How many different ways can G3.5 be made using any number of coins?”

coins = [200, 100, 50, 25, 10, 5, 1]  # Coin values in Sickles
target = 350  # Target value in Sickles

def count_combinations(coins, target):
    if target == 0:
        return 1  # Found a valid combination

    if target < 0 or len(coins) == 0:
        return 0  # Invalid combination or no more coins left

    # Count combinations including the current coin and excluding it
    return count_combinations(coins, target - coins[0]) + count_combinations(coins[1:], target)

# Count the combinations
num_combinations = count_combinations(coins, target)

# Print the result
print ("Number of different ways to make G3.5: ", num_combinations)
