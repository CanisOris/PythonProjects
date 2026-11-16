def calculate_utilization(used_capacity, total_capacity):
    """Calculates the percentage of storage or memory used."""
    
    # Prevent division by zero errors
    if total_capacity == 0:
        return 0.0
        
    # Perform the calculation
    percentage = (used_capacity / total_capacity) * 100
    
    # rount the percentage to 2 decimal places
    return round(percentage, 2)


main_server_usage = calculate_utilization(450, 500)

print(f"Main server is at {main_server_usage}% capacity.")
backup_usage = calculate_utilization(used_capacity=120, total_capacity=1000)
print(f"Backup drive is at {backup_usage}% capacity.")


# function challenge 2
def getSum(num1, num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

getSum(5, 7)

myAdd = getSum 
myAdd(10, 15)
