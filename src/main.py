from src.chains import (
    character_chain,
    dialogue_chain,
    plot_chain,
    memory_chain,
)
from src.memory import vectorstore, retrieve_context
from src.character_manager import save_character


def main() -> None:
    while True:
        print("\n" + "=" * 50)
        print("  WRITERGPT — AI Writing Assistant")
        print("=" * 50)
        print("1. Generate Character")
        print("2. Generate Dialogue")
        print("3. Generate Plot")
        print("4. Search Memory")
        print("Type 'exit' to quit")
        print("-" * 50)

        choice = input("\nChoose [1-4]: ").strip()

        if choice.lower() == "exit":
            print("Goodbye!")
            break

        request = input("Request > ").strip()
        if not request:
            print("Please enter a request.")
            continue

        if choice == "1":
            response = character_chain.invoke({"request": request})
            character_text = response.content

            memory_data = memory_chain.invoke({"character": character_text})
            print("\n" + "=" * 50)
            print("  CHARACTER")
            print("=" * 50)
            print(character_text)
            print("\n  MEMORY SNAPSHOT")
            print("-" * 50)
            print(f"  Name:    {memory_data.name}")
            print(f"  Role:    {memory_data.role}")
            print(f"  Summary: {memory_data.summary}")
            print(f"  Facts:   {', '.join(memory_data.facts)}")

            save_character(memory_data.model_dump())

            vectorstore.add_texts(
                [
                    f"Name: {memory_data.name}\n"
                    f"Role: {memory_data.role}\n"
                    f"Summary: {memory_data.summary}\n"
                    f"Facts: {', '.join(memory_data.facts)}"
                ]
            )

        elif choice == "2":
            context = retrieve_context(request)
            response = dialogue_chain.invoke({"request": request, "context": context})
            print("\n" + "=" * 50)
            print("  DIALOGUE")
            print("=" * 50)
            print(response.content)

        elif choice == "3":
            context = retrieve_context(request)
            response = plot_chain.invoke({"request": request, "context": context})
            print("\n" + "=" * 50)
            print("  PLOT")
            print("=" * 50)
            print(response.content)

        elif choice == "4":
            results = vectorstore.similarity_search(request, k=1)
            print("\n" + "=" * 50)
            print("  MEMORY SEARCH RESULTS")
            print("=" * 50)
            if results:
                print(results[0].page_content)
            else:
                print("No matching memories found.")

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
