import subprocess
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  # Get gitInfo
  git = {}  
  git['name'] = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).rstrip()
  git['sHA'] = subprocess.check_output(["git", "rev-parse", "HEAD"]).rstrip()
  git['shortSHA'] = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).rstrip()
  git['lastCommitTime'] = subprocess.check_output(["git", "log", "--format=\"%ai\"", "-n1", "HEAD"]).rstrip()
  git['lastCommitMessage'] = subprocess.check_output(["git", "log","--format=\"%B\"", "-n1", "HEAD"]).rstrip()
  git['lastCommitAuthor'] = subprocess.check_output(["git", "log", "--format=\"%aN\"", "-n1", "HEAD"]).rstrip()
  git['remoteOriginUrl'] = subprocess.check_output(["git", "config", "--get-all", "remote.origin.url"]).rstrip()
  return render_template('index.html', git=git )

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='80')
