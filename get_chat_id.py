import requests

BOT_TOKEN = ' ENTER YOUR BOT TOKEN HERE'

def get_chat_id():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    response = requests.get(url)
    
    # Print the status code and the entire response for debugging
    print(f"Status Code: {response.status_code}")
    updates = response.json()
    print("API Response:", updates)
    
    # Check if 'result' key exists in the response
    if 'result' in updates:
        for update in updates['result']:
            if 'message' in update:
                chat_id = update['message']['chat']['id']
                print(f"Chat ID: {chat_id}")
                return chat_id
    else:
        print("Error: 'result' key not found in the response.")
        if 'error_code' in updates and 'description' in updates:
            print(f"Error {updates['error_code']}: {updates['description']}")
        return None

chat_id = get_chat_id()



