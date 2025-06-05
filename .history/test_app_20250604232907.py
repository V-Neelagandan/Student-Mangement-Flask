from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    print("✅ Test route called")
    return "✅ Test route works!"

if __name__ == "__main__":
    app.run(debug=True)
