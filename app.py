from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "TASK 10 SUCCESS: Latest code fetched from GitHub by Jenkins!"


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/version")
def version():
    return {
        "application": "myapp",
        "version": "v2",
        "message": "Updated application deployed successfully"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
