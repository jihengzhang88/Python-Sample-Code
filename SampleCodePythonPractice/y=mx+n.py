import itertools


def find_mn_pair(nums):
    # Try all combinations of 2 distinct pairs (x1, y1) and (x2, y2)
    for (x1, y1), (x2, y2) in itertools.combinations(itertools.permutations(nums, 2), 2):
        if x1 != x2:  # Ensure we don't have a vertical line (undefined slope)
            # Calculate m and n from y = mx + n
            m = (y2 - y1) / (x2 - x1)  # Slope (m)
            n = y1 - m * x1  # Intercept (n)

            # Now check if other numbers fit the equation y = mx + n
            for x, y in itertools.permutations(nums, 2):
                if y == m * x + n:
                    print(f"x = {x}, y = {y}, m = {m}, n = {n}")
                    return (x, y, m, n)

    # If no solution was found
    print("No pair found satisfying the equation y = mx + n")
    return None