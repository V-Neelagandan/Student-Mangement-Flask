from flask import Flask
app=Flask(__name__)

app.secret_key = 'supersecret123'  # ✅ Add this line

# controlers fol_name
# product_controler module

from Controllers.product_controller import*

# if __name__ == "__main__":
#     app.run(debug=True)  