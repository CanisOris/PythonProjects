# array
tickets = ['network_down', 'password_reset', 'blue_screen', 'password_reset', 'network_down', 'network_down']

# get item count
outage_count = tickets.count('network_down')
print(f"Total network outages reported: {outage_count}\n")

# sort the array alphabetically
tickets.sort()
print("Tickets sorted alphabetically for processing:")

# loop through the array and process each ticket
for ticket in tickets:
    print(f" - Processing ticket type: {ticket}")