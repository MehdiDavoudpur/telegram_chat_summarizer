import requests


def summarizer(api_key, file_path):
    api_url = "https://api.openai.com/v1/chat/completions"  # Replace with the actual API endpoint

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()



    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'لطفا این گفتگو را برای من خلاصه کنید' + '\n' + text}
        ]
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        summary = data['choices'][0]['message']['content']
        return print(summary)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


if __name__ == '__main__':
    api_key = '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'
    file_path = 'chat.txt'
    summary = summarizer(api_key, file_path)

    if summary:
        print("Summary:")
        print(summary)
