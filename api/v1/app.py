#!/usr/bin/python3

"""A script that:
    - creates a varriable app
    - regesters the blue prints
    - 
"""

from flask import Flask

# Import modules from other files
import storage  # Assuming models.py is renamed to storage.py
import app_views  # Assuming the views are in api/v1/views.py

# Create Flask application instance
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views.bp)  # Assuming bp is the name in app_views.py

# Close storage connection on teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Run the Flask server
if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded
