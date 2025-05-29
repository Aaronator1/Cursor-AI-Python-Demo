from colorama import init, Fore, Style
import time

def main():
    # Initialize colorama
    init()

    # Basic arithmetic
    print(f"{Fore.CYAN}Demonstrating basic arithmetic:{Style.RESET_ALL}")
    a, b = 10, 5
    print(f"Numbers: {a} and {b}")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print()

    # String manipulation
    print(f"{Fore.GREEN}Demonstrating string manipulation:{Style.RESET_ALL}")
    name = "Python"
    print(f"Original string: {name}")
    print(f"Uppercase: {name.upper()}")
    print(f"Lowercase: {name.lower()}")
    print(f"Length: {len(name)}")
    print()

    # List operations
    print(f"{Fore.YELLOW}Demonstrating list operations:{Style.RESET_ALL}")
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    numbers.append(6)
    print(f"After append: {numbers}")
    numbers.reverse()
    print(f"After reverse: {numbers}")
    print(f"Sum of list: {sum(numbers)}")
    print()

    # Simple function demonstration
    print(f"{Fore.MAGENTA}Demonstrating functions:{Style.RESET_ALL}")
    for i in range(5):
        print(f"Countdown: {5 - i}")
        time.sleep(0.5)
    print("Done!")

if __name__ == "__main__":
    main() 