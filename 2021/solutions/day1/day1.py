import time

# Puzzle 1: Count the number of times a depth measurement increases from the previous measurement

def process_data():
    # Read in the data from the file
    with open("../../data/day1_puzzle_input.txt") as f:
        
        # Read in the data into a list
        file_data = f.readlines()

        # Convert each value in the list to an integer
        file_data = [int(l) for l in file_data]

    return file_data


def number_increase_counter(file_data):
    """Count the number of times a number increased compared to the previous value
    
    Args:

    Returns:
        counter (int): The number of times the value of the number has increased compared to the previous value

    """

    start_time = time.time()
    # # Read in the data from the file
    # with open("../../data/day1_puzzle_input.txt") as f:
        
    #     # Read in the data into a list
    #     file_data = f.readlines()

    #     # Convert each value in the list to an integer
    #     file_data = [int(l) for l in file_data]

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

file_data = process_data()
print(number_increase_counter(file_data=file_data))

# Part 2
sliding_window_sum_list = []
for i, num in enumerate(file_data):
    if i < 2:
        pass
    else:
        sliding_window_sum = sum(file_data[i-2:i+1])
        sliding_window_sum_list.append(sliding_window_sum)

# print(sliding_window_sum_list)
print(number_increase_counter(file_data=sliding_window_sum_list))

# print(file_data[:3])
# print(sliding_window_sum_list)

# print()