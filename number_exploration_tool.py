
# Number Exploration Tool

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def number_exploration_tool():
    # Get user name
    name = input("Enter your name: ")

    # Get three favorite numbers
    print("Enter your three favorite numbers:")
    numbers = []
    for i in range(1, 4):
        while True:
            try:
                num = int(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid integer.")

    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Check if numbers are even or odd
    even_odd_info = []
    for num in numbers:
        even_odd_info.append((num, "even" if num % 2 == 0 else "odd"))

    for num, parity in even_odd_info:
        print(f"The number {num} is {parity}.")

    # Calculate and display squares of numbers
    print("\nHere are your numbers and their squares:")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")

    # Calculate the sum of numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"The sum {total_sum} is not a prime number.")

# Run the tool
if __name__ == "__main__":
    number_exploration_tool()
