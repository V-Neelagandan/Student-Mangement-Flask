from flask import Flask
app = Flask(__name__)

main.secret_key = 'supersecret123'  # ✅ Add this line
from Controllers.product_controller import *

# controlers fol_name
# product_controler module


# if __name__ == "__main__":
#     app.run(debug=True)
