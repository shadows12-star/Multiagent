from agent import ask_agent


def print_header():

    print("\n")
    print("=" * 65)
    print("       BANGLADESH MULTI-TOOL AI AGENT")
    print("       Powered by Mistral AI + LangChain")
    print("=" * 65)

    print(
        "\nAvailable knowledge sources:"
    )

    print(
        "1. Bangladesh Institutional Information"
    )

    print(
        "2. Bangladesh Hospitals"
    )

    print(
        "3. Bangladesh Restaurants"
    )

    print(
        "4. Web Search"
    )

    print(
        "\nType 'exit' or 'quit' to close the program.\n"
    )


def main():

    print_header()

    while True:

        try:

            question = input(
                "You: "
            ).strip()

            if not question:
                continue

            if question.lower() in [
                "exit",
                "quit",
                "q"
            ]:

                print(
                    "\nGoodbye!\n"
                )

                break

            print(
                "\nAgent is processing...\n"
            )

            answer = ask_agent(
                question
            )

            print(
                "Agent:"
            )

            print(
                answer
            )

            print(
                "\n" + "-" * 65 + "\n"
            )

        except KeyboardInterrupt:

            print(
                "\n\nProgram stopped."
            )

            break

        except Exception as error:

            print(
                "\nAn error occurred:"
            )

            print(
                str(error)
            )

            print()


if __name__ == "__main__":
    main()