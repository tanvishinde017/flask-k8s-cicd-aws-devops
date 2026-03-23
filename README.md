🚀 Flask Kubernetes CI/CD AWS DevOps Project

![Flask Kubernetes CI/CD AWS DevOps pipeline workflow showing developer pushing code through GitHub and GitHub Actions to build Docker images, push to DockerHub, deploy to AWS EC2 with Kubernetes, and run live application with kubectl port-forward on port 5000](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/architecture/workflow.png)

This project demonstrates a complete DevOps pipeline for deploying a Flask application using:

🐳 Docker (Containerization)
☸️ Kubernetes (Minikube)
🔄 GitHub Actions (CI/CD)
☁️ AWS EC2 (Cloud Deployment)

🎯 The goal is to simulate a real-world production pipeline from development to deployment.

🧠 Project Architecture

Pipeline Flow:
Developer → GitHub → GitHub Actions → DockerHub → AWS EC2 → Kubernetes → Live App

⚙️ Tech Stack
Python (Flask)
Docker
Kubernetes (Minikube)
AWS EC2
GitHub Actions
Linux

📂 Project Structure
FLASK-K8S-CICD-AWS-DEVOPS
│
├── .github/
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── architecture/
│   └── workflow.png
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── screenshots/
│   ├── docker-build-k8s.png
│   ├── dockerhub-k8s.png
│   ├── ec2-instance-created.png
│   ├── k8-running-ec2.png
│   ├── k8s-live.png
│   ├── live-aws.png
│   ├── minikube-ec2-running.png
│   ├── project-structure.png
│   └── wslconfig.png
│
├── Dockerfile
├── .dockerignore
└── README.md

🐍 Flask Application
Endpoint
/

Response:

Hello from Flask DevOps Project

🐳 Docker Build

docker build -t flask-k8s-app .
📦 DockerHub Push

docker tag flask-k8s-app your-dockerhub/flask-k8s-app
docker push your-dockerhub/flask-k8s-app


![Docker successfully builds flask-k8s-app image showing multiple layers created with hash IDs, demonstrating containerization of the Flask application for deployment to Kubernetes and AWS](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/docker-build-k8s.png)


☸️ Kubernetes Deployment
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

🌍 Live Application on AWS

http://EC2_PUBLIC_IP:NodePort
🔄 CI/CD Pipeline (GitHub Actions)

GitHub Actions automates:

Build Docker Image
Push to DockerHub
Deploy to Kubernetes

🏗️ DevOps Workflow

1️⃣ Developer pushes code
2️⃣ GitHub Actions triggers pipeline
3️⃣ Docker image is built
4️⃣ Image pushed to DockerHub
5️⃣ EC2 pulls image
6️⃣ Kubernetes deploys container
7️⃣ Application goes live

⚠️ Challenges & Solutions
❌ Docker not running

✔ Started Docker service

❌ Port not accessible

✔ Opened port in AWS Security Group

❌ Kubernetes not starting

✔ Restarted Minikube

❌ Image pull error

✔ Verified DockerHub image name

📌 GitHub Repository

👉 https://github.com/tanvishinde017/flask-k8s-cicd-aws-devops

👩‍💻 Author

Tanavi Shinde
DevOps | Cloud | Kubernetes | AWS