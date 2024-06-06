import requests
import pyperclip

# mobile

server_url = 'http://<ip>:5000/update_clipboard'

def send_clipboard_content():
    content = pyperclip.paste()
    if content:
        response = requests.post(server_url, json={"content": content})
        if response.status_code == 200:
            print("Clipboard content sent successfully.")
        else:
            print("Failed to send clipboard content.")

if __name__ == '__main__':
    send_clipboard_content()
