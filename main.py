from dotenv import load_dotenv

from agent.agent import DevMindAgent

load_dotenv()


def main():

    print("=" * 60)
    print("🚀 DevMind AI")
    print("=" * 60)

    print("AI Software Engineering Assistant\n")

    ai = DevMindAgent()

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        print()

        answer = ai.chat(question)

        print(answer)

        print()


if __name__ == "__main__":
    main()