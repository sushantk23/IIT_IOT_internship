from flask import Flask, request

app = Flask(__name__)

# ---------- Store Temperature ----------
@app.route('/send_temperature', methods=['GET', 'POST'])
def send_temperature():
    temp = request.args.get('value')

    if temp is None:
        return "Temperature value missing", 400

    with open("temperature.txt", "a") as f:
        f.write(temp + "\n")

    return "Temperature stored successfully"


# ---------- Store Light Intensity ----------
@app.route('/send_light', methods=['GET', 'POST'])
def send_light():
    light = request.args.get('value')

    if light is None:
        return "Light value missing", 400

    with open("light.txt", "a") as f:
        f.write(light + "\n")

    return "Light intensity stored successfully"


# ---------- Display Temperature ----------
@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    try:
        with open("temperature.txt", "r") as f:
            data = f.read()
        return "<h3>Temperature Readings</h3><pre>" + data + "</pre>"
    except FileNotFoundError:
        return "No temperature data available"


# ---------- Display Light ----------
@app.route('/get_light', methods=['GET'])
def get_light():
    try:
        with open("light.txt", "r") as f:
            data = f.read()
        return "<h3>Light Intensity Readings</h3><pre>" + data + "</pre>"
    except FileNotFoundError:
        return "No light data available"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
