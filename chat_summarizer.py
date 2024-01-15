import requests
from text_indexed_creator import append_text_with_index

with open("update_id.txt", "r") as file:
    update_id = int(file.read())
    if update_id == '':
        update_id = 4750000
    # print(update_id)
    # print(type(update_id))
bot_token = "6553910401:AAGfbPZp3D4m19rYlGFFN1YPYu4KnafTzCM"
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
offset = f"?offset={update_id + 1}"

response = requests.get(url)
chat_line = ""

if response.status_code == 200:
    data = response.json()

    if 'result' in data and data['result']:
        for item in data['result']:

            if 'message' in item and 'text' in item['message']:
                first_name = item['message']['from']['first_name']
                last_name = item['message']['from'].get('last_name', "")
                user_name = item['message']['from'].get('username', "")
                text = item['message']['text']
                update_id = item['update_id']

                chat_line = f"{first_name} {last_name}-({user_name}): {text}"
                print(chat_line)

                append_text_with_index(chat_line)

        with open("update_id.txt", "w") as file:
            file.write(str(update_id))

        # with open("chat.csv", "w", encoding='utf-8') as file:
        #     file.write(str(chat))

    else:
        print("No 'result' field or 'result' is empty in the JSON response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
