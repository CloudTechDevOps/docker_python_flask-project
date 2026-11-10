
from flask import Flask
import os
import logging

app = Flask(__name__)

# Log directory
LOG_DIR = "/var/logs/myapp"

# Create log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
LOG_FILE = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def hello():
    app.logger.info("Homepage accessed")
    return "updated Flask sample application on azure hghapp service updated version-6"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.logger.info("Starting Flask application on port %s", port)
    app.run(host="0.0.0.0", port=port, debug=False)
