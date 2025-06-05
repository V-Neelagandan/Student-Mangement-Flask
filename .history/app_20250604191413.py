Exception has occurred: ModuleNotFoundError
No module named 'app'
  File "K:\FLASK_API\Controllers\product_controller.py", line 1, in <module>
    from app import app
ModuleNotFoundError: No module named 'app'

app.secret_key = 'supersecret123'  # ✅ Add this line
from Controllers.product_controller import *

# controlers fol_name
# product_controler module


# if __name__ == "__main__":
#     app.run(debug=True)
