from flask import Flask, jsonify, request
import socket
import os
import datetime

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <h1>🚀 Flask Kubernetes DevOps Project</h1>
    <p>Welcome to your production-ready app!</p>

    <h3>📌 Available Endpoints:</h3>
    <ul>
        <li>/health</li>
        <li>/info</li>
        <li>/docs</li>
    </ul>
    """

# Health check (used by Kubernetes)
@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "time": str(datetime.datetime.now())
    })

# System info (very useful in DevOps)
@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "environment": os.getenv("ENV", "production"),
        "version": "1.0.0"
    })

# Documentation endpoint
@app.route("/docs")
def docs():
    return jsonify({
        "project": "Flask Kubernetes DevOps Project",
        "features": [
            "CI/CD with GitHub Actions",
            "Dockerized Flask App",
            "Deployed on AWS EKS",
            "Ingress Controller (NGINX)",
            "Auto Scaling (HPA)",
            "Monitoring with Prometheus & Grafana"
        ],
        "endpoints": {
            "/": "Home Page",
            "/health": "Health Check",
            "/info": "System Info",
            "/docs": "Project Documentation"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)