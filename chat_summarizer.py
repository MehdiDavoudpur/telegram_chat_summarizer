import requests
from text_indexed_creator import append_text_with_index

with open("update_ids.txt", "r") as file:
    update_ids = file.readlines()
    print("first update_id:", update_ids)
    update_id = int(update_ids[-1])
    print(update_id)
    # if update_id == '':
    #     update_id = 4750000
    # print(update_id)
    # print(type(update_id))
bot_token = "6553910401:AAGfbPZp3D4m19rYlGFFN1YPYu4KnafTzCM"
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
offset = f"?offset={update_id + 1}"

response = requests.get(url + offset)
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

                chat_line = f"{first_name} {last_name}-({user_name}): {text} - update_id:{update_id}"
                print(chat_line)

                append_text_with_index(chat_line)

        with open("update_ids.txt", "r") as file:
            update_ids = file.read()

        with open("update_ids.txt", "w") as file:
            # print("last updete_id:", update_id)
            update_ids = update_ids + str(update_id) + "\n"
            file.write(update_ids)

        # with open("chat.csv", "w", encoding='utf-8') as file:
        #     file.write(str(chat))

    else:
        print("No 'result' field or 'result' is empty in the JSON response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
