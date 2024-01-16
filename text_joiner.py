def text_joiner(text):
    # Read existing content to determine the next index
    with open("chat.txt", "r", encoding='utf-8') as file:
        existing_content = file.read()
        # next_index = len(existing_content) + 1

    # Append new text with the index
    with open("chat.txt", "a", encoding='utf-8') as file:
        file.write(text)

