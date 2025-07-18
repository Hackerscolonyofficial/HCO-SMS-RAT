from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_sms():
    data = request.get_json()
    number = data.get('number')
    message = data.get('message')
    print(f"SMS to {number}: {message}")
    return jsonify({"status": "sent", "number": number, "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)