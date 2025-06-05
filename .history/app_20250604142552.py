from flask import Flask
import flas
app=Flask(__name__)

# controlers fol_name
# product_controler module

from Controllers.product_controller import*

# if __name__ == "__main__":
#     app.run(debug=True)  