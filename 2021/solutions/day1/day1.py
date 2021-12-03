import time

# Puzzle 1: Count the number of times a depth measurement increases from the previous measurement

def number_increase_counter():
    """Count the number of times a number increased compared to the previous value
    
    Args:

    Returns:
        counter (int): The number of times the value of the number has increased compared to the previous value

    """

    start_time = time.time()
    # Read in the data from the file
    with open("../../data/day1_puzzle_input.txt") as f:
        
        # Read in the data into a list
        file_data = f.readlines()

        # Convert each value in the list to an integer
        file_data = [int(l) for l in file_data]

        # Start a counter
        counter = 0
        # Iterate through each item in the list
        for i, num in enumerate(file_data):
            # Skip the first value
            if i == 0:
                pass
            else:
                # Check if the current number is greater then the previous value in the list
                if num > file_data[i-1]:
                    # print(num, file_data[i-1])
                    counter += 1

    end_time = time.time()
    total_time = end_time - start_time
    return f"Number of value increases: {counter}\nTotal time to execute: {total_time}"

print(number_increase_counter())
