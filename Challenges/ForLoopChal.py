

tasks = ['compile', 'test', 'fail', 'deploy']

for task in tasks:
    if task == 'fail':
        print("Critical failure detected. Halting pipeline.")
        # Exits the loop immediately, skipping 'deploy'
        break  
        
    print(f"Completed: {task}")
    

network_ports = [80, 443, 21, 22]

for port in network_ports:
    # Skip unsecured ports
    if port == 21 or port == 80:
        continue
        
    print(f"Securing port: {port}")
    


# range(5) generates numbers from 0 up to (but not including) 5
for i in range(5):
    print(f"Attempt {i}")
    


# Using start, stop, and step: range(2, 10, 2)
for even_num in range(2, 9, 2):
    print(f"Even: {even_num}")
    


search_list = ['user_1', 'user_2', 'user_3']
target = 'admin'
# look for admin
for user in search_list:
    print(f"Checking {user}...")
    if user == target:
        print("Target found!")
        break
else:
    print(f"Search exhausted. '{target}' was not found in the list.")

