🚀 Flask Kubernetes CI/CD AWS DevOps Project

![Flask Kubernetes CI/CD AWS DevOps pipeline workflow showing developer pushing code through GitHub and GitHub Actions to build Docker images, push to DockerHub, deploy to AWS EC2 with Kubernetes, and run live application with kubectl port-forward on port 5000](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/architecture/workflow.png)

This project demonstrates a complete DevOps pipeline for deploying a Flask application using...

🐳 Docker (Containerization)
☸️ Kubernetes (Minikube)
🔄 GitHub Actions (CI/CD)
☁️ AWS EC2 (Cloud Deployment)

🎯 The goal is to simulate a real-world production pipeline from development to deployment..

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
![Project Structure](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/project-structure.png)

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

![DockerHub dashboard displaying the tanvishinde017 repository namespace with flask-k8s-app image successfully pushed, showing image layers, tags, and push history in the container registry interface](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/dockerhub-k8s.png)


☸️ Kubernetes Deployment
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml


![Kubernetes pods running on AWS EC2 instance displaying two flask-app pods in Running status with 1/1 ready replicas, each 155 seconds old. kubectl get svc output shows flask-service NodePort exposing port 5000 on cluster IP 10.109.183.0 with external access via port 30007 on TCP, created 15 seconds ago. Successful deployment confirmation showing containerized Flask application actively running in Kubernetes cluster on AWS infrastructure.](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/k8-running-ec2.png)

k8s-live
![Minikube service dashboard showing flask-service successfully running on local Kubernetes cluster with namespace default, service name flask-service, target port 5000, and URL http://192.168.49.2:30007. Tunnel established to localhost:58380. Terminal displays kubectl port-forward command output confirming service is accessible locally. Message indicates Docker driver is active on Windows, requiring open terminal to maintain connection. Screenshot captures successful local Kubernetes deployment ready for testing.](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/k8s-live.png)


🌍 Live Application on AWS

http://EC2_PUBLIC_IP:NodePort
🔄 CI/CD Pipeline (GitHub Actions)

☁️ EC2 Instance
![EC2 Instance](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/ec2-instance-created.png)


GitHub Actions automates:

Build Docker Image
Push to DockerHub
Deploy to Kubernetes

🐳 Minikube on EC2
![Minikube EC2](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/minikube-ec2-running.png)


🏗️ DevOps Workflow

1️⃣ Developer pushes code
2️⃣ GitHub Actions triggers pipeline
3️⃣ Docker image is built
4️⃣ Image pushed to DockerHub
5️⃣ EC2 pulls image
6️⃣ Kubernetes deploys container
7️⃣ Application goes live

🌍 Live AWS App
![Live AWS](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/live-aws.png)

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

⚙️ WSL Config
![WSL Config](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/wslconfig.png)

👩‍💻 Author

Tanavi Shinde
DevOps | Cloud | Kubernetes | AWS
