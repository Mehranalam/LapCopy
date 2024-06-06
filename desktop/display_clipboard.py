import requests
import time

server_url = 'http://localhost:5000/get_clipboard'

def get_clipboard_content():
    response = requests.get(server_url)
    if response.status_code == 200:
        return response.json().get('content')
    return None

if __name__ == '__main__':
    while True:
        content = get_clipboard_content()
        if content:
            print("Clipboard content:", content)
        time.sleep(5) # check every 5 sec
