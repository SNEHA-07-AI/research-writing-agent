import os
from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient

load_dotenv()

# Connect to both AI and search
ai = Groq(api_key=os.getenv("GROQ_API_KEY"))
search = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

print("=================================")
print("   Research Agent - Ask Anything!")
print("=================================")
print("I can search the web for you!\n")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Step 1 - Search the web
    print("\nSearching the web...")
    results = search.search(user_input, max_results=3)

    # Step 2 - Pull out the text from search results
    web_info = ""
    for r in results["results"]:
        web_info += f"Source: {r['url']}\n"
        web_info += f"Content: {r['content']}\n\n"

    # Step 3 - Send question + web results to AI
    print("Thinking...\n")
    response = ai.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful research assistant. Use the web search results provided to answer the user's question accurately. Always base your answer on the search results."
            },
            {
                "role": "user",
                "content": f"Question: {user_input}\n\nWeb search results:\n{web_info}\n\nPlease answer the question based on these results."
            }
        ]
    )

    answer = response.choices[0].message.content
    print("AI: " + answer)
    print("\n" + "-"*40)