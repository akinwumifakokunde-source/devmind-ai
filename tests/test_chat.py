from services.chat_session import ChatSession

print("=" * 60)
print("🚀 DevMind Repository Chat")
print("=" * 60)

url = input("GitHub Repository: ").strip()

chat = ChatSession(url)

print("\nRepository indexed successfully.\n")

while True:

    question = input("You: ")

    if question.lower() in {
        "exit",
        "quit",
        "q",
    }:
        break

    answer = chat.ask(question)

    print()
    print("AI:")
    print(answer)
    print()