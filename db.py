import subprocess
import time

# Start the Flask API server
api_process = subprocess.Popen(["python", "models.py"])

# Give the server time to start
time.sleep(5)

# Run the client script
subprocess.run(["python", "app.py"])

# Optionally terminate the API server when done
api_process.terminate()
