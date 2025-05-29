import os
from openai import OpenAI
from dotenv import load_dotenv
from colorama import init, Fore, Style

def setup_openai():
    """Initialize OpenAI client with API key from environment."""
    load_dotenv()  # Load API key from .env file
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError(
            f"{Fore.RED}Error: OPENAI_API_KEY not found in environment variables. "
            f"Please create a .env file with your API key.{Style.RESET_ALL}"
        )
    client = OpenAI()  # The API key will be read from environment variable
    return client

def ask_chatgpt(question, model="gpt-3.5-turbo"):
    """Send a query to ChatGPT and get the response."""
    try:
        client = setup_openai()
        
        # Create the chat completion
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    
    except Exception as e:
        return f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}"

def main():
    """Main function to handle user interaction."""
    init()  # Initialize colorama
    
    print(f"{Fore.CYAN}Welcome to ChatGPT Query Tool!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'quit' to exit{Style.RESET_ALL}\n")
    
    while True:
        try:
            # Get user input
            question = input(f"{Fore.GREEN}Your question: {Style.RESET_ALL}")
            
            # Check if user wants to quit
            if question.lower() in ['quit', 'exit', 'q']:
                print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
                break
            
            # Get and print the response
            print(f"\n{Fore.BLUE}ChatGPT's response:{Style.RESET_ALL}")
            response = ask_chatgpt(question)
            print(f"{response}\n")
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main() 