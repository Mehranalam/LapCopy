# LapCopy

A Python program that can transfer text copied on a phone to a laptop can be used as a combination of web service, mobile and desktop applications. 

For this purpose, we use Flask for the backend to create a small server that can receive the copied texts and then display these texts on the laptop.

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install flask
```

### Setps for use

1. install Termux in your android device : https://github.com/termux/termux-app/releases/tag/v0.118.0

2. install python and requests lib : `pkg install python git && pip install requests`

3. clone LapCopy from github : `git clone https://github.com/mehranalam/LapCopy.git`

4. run server.py
5. go to termux app in android
6. run mobile/clipboard_sender.py
7. back to your system
8. run desktop/display_clipboard.py


Tip: Be sure to enter mobile/clipboard sender.py and enter the ip part of your system: 

```python
server_url = 'http://<ip>:5000/update_clipboard'
```

