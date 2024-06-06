from flask import Flask, request, jsonify

app = Flask(__name__)

clipboard_content = ""

@app.route('/update_clipboard', methods=['POST'])
def update_clipboard():
    global clipboard_content
    clipboard_content = request.json.get('content')
    return jsonify({"status": "success"}), 200

@app.route('/get_clipboard', methods=['GET'])
def get_clipboard():
    return jsonify({"content": clipboard_content}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
