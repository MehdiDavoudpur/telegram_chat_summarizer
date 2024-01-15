
def append_text_with_index(text):

    try:
        # Read existing content to determine the next index
        with open("chat.csv", "r", encoding='utf-8') as file:
            existing_content = file.readlines()
            next_index = len(existing_content) + 1

        # Append new text with the index
        with open("chat.csv", "a", encoding='utf-8') as file:
            file.write(f"{next_index}. {text}\n")

    except FileNotFoundError:
        # If the file doesn't exist, create it with the first entry
        with open("chat.csv", "w") as file:
            file.write(f"1. {text}\n")




