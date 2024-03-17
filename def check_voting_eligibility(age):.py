def check_voting_eligibility(age):
    """
    This function checks if a person is eligible to vote based on their age.

    Args:
        age: The age of the person.

    Returns:
        A string indicating whether the person is eligible to vote or not.
    """
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."


def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence.append(0)
        return fibonacci_sequence
    elif n == 2:
        fibonacci_sequence.extend([0, 1])
        return fibonacci_sequence
    else:
        fibonacci_sequence.extend([0, 1])
        a, b = 0, 1
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)
            a, b = b, c
        return fibonacci_sequence


# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check voting eligibility
voting_eligibility_message = check_voting_eligibility(age)
print(voting_eligibility_message)

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
