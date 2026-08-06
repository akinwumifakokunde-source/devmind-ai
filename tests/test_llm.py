from services.llm import get_llm

llm = get_llm()

response = llm.invoke("Explain what Python is in one paragraph.")

print(response)
print("-" * 60)
print(response.content)