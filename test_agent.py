from agent import ask_agent

TEST_QUESTIONS = [
    "How many institutions are in Dhaka district?",
    "How many health facilities are in Dhaka district?",
    "Show me 5 highly rated restaurants with addresses containing Dhaka.",
    "What is the role of DGHS in Bangladesh?",
]


def main():
    print("\nBANGLADESH AI AGENT TEST\n")
    print("=" * 70)

    for number, question in enumerate(TEST_QUESTIONS, start=1):

        print(f"\nTEST {number}")
        print(f"Question: {question}")
        print("\nAnswer:")

        try:
            answer = ask_agent(question)
            print(answer)

        except Exception as error:
            print(f"ERROR: {error}")

        print("\n" + "-" * 70)


if __name__ == "__main__":
    main()