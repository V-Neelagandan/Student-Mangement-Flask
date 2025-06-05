from flask import Flask

@app.route('/')
def home():
    return "✅ Flask App Running Successfully on Render!"
app = Flask(__name__)

app.secret_key = 'supersecret123'  # ✅ Add this line
from Controllers.product_controller import *

# controlers fol_name
# product_controler module

if __name__ == "__main__":
    app.run(debug=True)

