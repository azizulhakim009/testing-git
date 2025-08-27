from flask import Flask, render_template, request
import web_calculator  # your pulled calculator code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        # Get the input from form
        expression = request.form.get("expression")
        try:
            # Assuming your web_calculator has a function calculate()
            result = web_calculator.calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
