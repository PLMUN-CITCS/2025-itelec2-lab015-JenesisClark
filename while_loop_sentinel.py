# Filename: while_loop_sentinel.py

# Initialize the sum variable
total_sum = 0

# Start an indefinite while loop
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    # Check if the user entered the sentinel value 'stop'
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    # Convert the input to a number and add it to the total sum with error handling
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        # Handle invalid input (non-numeric)
        print("Invalid input. Please enter a numeric value or 'stop'.")
    
# Print the final total sum after the loop ends
print("The total sum is:", total_sum)