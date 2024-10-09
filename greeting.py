# Simple Python program that greets the user
def greet_user():
    # Ask for user's name
    name = input("What is your name? ")
    
    # Generate a greeting message
    greeting = f"Hello, {name}! Welcome to your Python script."
    
    # Print the greeting
    print(greeting)

# Run the function to greet the user
if __name__ == "__main__":
    greet_user()
