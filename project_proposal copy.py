import gradio as gr

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/future_value', methods=['GET'])
def future_value():
    r = float(request.args.get("r", 0.5))
    N = int(request.args.get("N", 20))
    A = float(request.args.get("A", 100))
    show_increment = request.args.get("show_increment", "false").lower() == "true"

    if show_increment:
        total = 0
        increments = []

        for i in range(N):
            increment = A * (1 + r) ** i
            total += increment
            increments.append(round(increment, 2))

        return jsonify({"total": round(total, 2), "increments": increments})
    
    else:
        value = A * (1 + r) ** N
        return jsonify({"final_value": round(value, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
