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



🚀 PART 2: ADVANCED DEVOPS (AWS EKS + MONITORING + SCALING)

workflow 

![workflow](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/workflow_2.png)


☸️ AWS EKS-Based Production Deployment

This phase demonstrates deploying the Flask application on a managed Kubernetes service (Amazon EKS) with:

🌐 Ingress Controller (Public Access)
📊 Monitoring (Prometheus + Grafana)
⚡ Auto Scaling (HPA)
🔄 CI/CD Integration
🏗️ Step 1: EKS Cluster Creation

The Kubernetes cluster was created using:

eksctl create cluster --name flask-cluster --region ap-south-1
📸 CloudFormation Stack Created
![CloudFormation](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/created_cloudformation.png)
📸 CloudFormation Dashboard
![Dashboard](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/cloudformation_dashboard.png)

👉 AWS automatically provisions :

VPC
Worker Nodes
Security Groups
IAM Roles
🔗 Step 2: Connect to EKS Cluster
aws eks update-kubeconfig --name flask-cluster --region ap-south-1

This updates kubeconfig to interact with your cluster.

🚀 Step 3: Deploy Application to EKS
kubectl apply -f k8s/
kubectl get pods
📸 Pods Running (Application + Monitoring)
![Pods](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/Monitoring_pods_running.png)
🌐 Step 4: Ingress Controller Setup

Installed NGINX Ingress Controller:

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/aws/deploy.yaml

Then applied:

kubectl apply -f k8s/ingress.yaml
📸 Ingress Working (Public Access)
![Ingress](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/ingress_domain_working.png)

👉 This creates an AWS LoadBalancer (ELB) which exposes your app to the internet.

📊 Step 5: Monitoring Setup (Prometheus + Grafana)

Installed monitoring stack using Helm:

helm install monitoring prometheus-community/kube-prometheus-stack
📸 Monitoring Pods Running
![Monitoring](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/Monitoring_pods_running.png)
📈 Step 6: Grafana Dashboard

Access Grafana:

kubectl port-forward svc/monitoring-grafana 3000:80

👉 Open: http://localhost:3000

📸 Grafana Dashboard
![Grafana](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/graphana_dashboard.png)

👉 Features:

CPU Usage
Memory Usage
Pod Metrics
Cluster Health
⚡ Step 7: Horizontal Pod Autoscaler (HPA)

Enable auto scaling:

kubectl autoscale deployment flask-app --cpu-percent=50 --min=1 --max=5

Check status:

kubectl get hpa
📸 HPA Scaling
![HPA](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/HPA_showing_min_max_pods.png)

👉 Automatically scales pods based on CPU load.

🔄 Step 8: CI/CD Deployment to EKS

Pipeline flow:

Push code to GitHub
GitHub Actions builds Docker image
Push to DockerHub
Connect to EKS
Deploy using kubectl apply
📸 GitHub Actions Pipeline
![CI/CD](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/github_actions.png)
📸 GitHub Secrets
![Secrets](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/github_secrets.png)
🌍 Final Deployment (Live Application)

Application is exposed using:

AWS LoadBalancer (ELB)
Kubernetes Ingress

👉 Accessible via public URL:

http://<your-loadbalancer-url>
🧠 Key Learnings
Managed Kubernetes with EKS
Real-world CI/CD pipeline
Monitoring production workloads
Auto scaling using HPA
Exposing apps using Ingress
⚠️ Challenges Faced
Issue	Solution
Pods Pending	Fixed resource limits
Ingress not working	Checked LoadBalancer
Grafana not opening	Used port-forward
CI/CD failed	Fixed AWS credentials
🏁 Conclusion

This project demonstrates a production-grade DevOps pipeline with:

✅ AWS EKS
✅ CI/CD Automation
✅ Monitoring & Observability
✅ Auto Scaling
✅ Public Deployment

👩‍💻 Author

Tanavi Shinde
DevOps | Cloud | Kubernetes | AWS