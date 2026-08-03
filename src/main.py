from config import load_prompt
from classifier import classify_email


def main():
    # Load the prompt configuration
    prompt = load_prompt("../prompts/v1.yaml")

    # Sample customer email
    email = """
    Hello,

    I was charged twice for my premium subscription this month.
    Can you please refund the duplicate payment?

    Thanks,
    John
    """

    # Classify the email
    result = classify_email(email, prompt)

    # Print the results
    print("\n===== Classification Result =====")
    print(f"Prompt Version : {prompt.version}")
    print(f"Timestamp      : {prompt.timestamp}")
    print(f"Category       : {result.category}")
    print(f"Summary        : {result.summary}")


if __name__ == "__main__":
    main()