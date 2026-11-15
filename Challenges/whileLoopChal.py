

power_level = 1

while power_level <= 5:
    print(f"Charging system... Level {power_level}")
    
    if power_level == 3:
        print("System overload detected! Halting charge.")
        break  # Exits the loop immediately
        
    power_level += 1
    
process_id = 0

while process_id < 5:
    process_id += 1
    
    # if even skip print
    if process_id % 2 == 0:
        continue 
        
    print(f"Processing odd ID: {process_id}")
    

target_value = 99
current_check = 1

while current_check <= 3:
    print(f"Checking {current_check}...")
    
    if current_check == target_value:
        print("Target found! Stopping search.")
        break
        
    current_check += 1
    
else:   
    print("Search exhausted. The target value was not found.")
    
