from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h2>Simple Web Calculator</h2>
        <form action="/calculate" method="get">
            <input type="number" name="num1" placeholder="Enter first number" required>
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="number" name="num2" placeholder="Enter second number" required>
            <button type="submit">Calculate</button>
        </form>
    """

@app.route("/calculate")
def calculate():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        operation = request.args.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = "Error: Division by zero" if num2 == 0 else num1 / num2
        else:
            result = "Invalid operation"

        return f"<h2>Result: {result}</h2><a href='/'>Back</a>"
    except Exception as e:
        return f"<h2>Error: {e}</h2><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
