import subprocess
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  error = None
  # Get gitInfo
  name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
  sHA = subprocess.check_output(["git", "rev-parse", "HEAD"])
  shortSHA = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
  lastCommitTime = subprocess.check_output(["git", "log", "--format=\"%ai\"", "-n1", "HEAD"])
  lastCommitMessage = subprocess.check_output(["git", "log"," --format=\"%B\"", "-n1", "HEAD"])
  lastCommitAuthor = subprocess.check_output(["git", "log", "--format=\"%aN\"", "-n1", "HEAD"])
  remoteOriginUrl = subprocess.check_output(["git", "config", "--get-all", "remote.origin.url"])
  return render_template('index.html', error=error)

if __name__ == "__main__":
    app.run()
