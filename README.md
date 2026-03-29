# 🚀 Flask Kubernetes CI/CD AWS DevOps Project

![Workflow](https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/architecture/workflow.png)

---

## 📌 Project Overview

This project demonstrates a complete DevOps pipeline for deploying a Flask application using:

- 🐳 Docker  
- ☸️ Kubernetes (Minikube + EKS)  
- 🔄 GitHub Actions  
- ☁️ AWS  

---

## 🧠 Architecture Flow


Developer → GitHub → GitHub Actions → DockerHub → AWS → Kubernetes → Live App


This flow represents a **real-world CI/CD pipeline**, where code moves from development to production automatically.

---

## 🐳 Docker

```bash
docker build -t flask-k8s-app .
docker push your-dockerhub/flask-k8s-app

🔗 Docker Build Screenshot
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/docker-build-k8s.png

👉 This screenshot shows the Docker image build process, including:

Layer-by-layer image creation
Successful build confirmation
Image tagging for deployment

🔗 DockerHub Screenshot
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/dockerhub-k8s.png

👉 This shows the DockerHub repository, where:

The image is successfully pushed
Versioning and tags are visible
Registry acts as a central storage for deployment
☸️ Kubernetes Deployment
kubectl apply -f k8s/

🔗 Kubernetes Pods Running
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/k8-running-ec2.png

👉 This screenshot confirms:

Pods are in Running state
Application is successfully deployed on Kubernetes
Cluster is stable and ready to serve traffic

🔗 Kubernetes Live Output
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/k8s-live.png

👉 This shows:

Service exposure via NodePort / Minikube service
Local URL generated for accessing the app
Application is reachable from browser
☁️ AWS EC2

🔗 EC2 Instance Created
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/ec2-instance-created.png

👉 This shows:

EC2 instance successfully launched
Instance type, region, and status
Cloud environment setup for deployment

🔗 Minikube Running on EC2
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/minikube-ec2-running.png

👉 This confirms:

Minikube is running inside EC2
Kubernetes cluster initialized
Ready for container deployment

🔗 Live Application Output
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshots/live-aws.png

👉 This shows:

Flask app running in browser
Successful deployment on cloud
End-to-end pipeline working
🔄 CI/CD Pipeline

🔗 GitHub Actions Workflow
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/github_actions.png

👉 This screenshot shows:

Automated pipeline execution
Steps like build, push, deploy
Successful CI/CD workflow

🔗 GitHub Secrets Setup
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/github_secrets.png

👉 This shows:

Secure environment variables
AWS credentials & DockerHub secrets
Secure pipeline configuration
🚀 PART 2: AWS EKS + MONITORING + SCALING
☸️ EKS Cluster Creation
eksctl create cluster --name flask-cluster --region ap-south-1

🔗 CloudFormation Stack
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/created_cloudformation.png

👉 This shows:

AWS creating infrastructure automatically
Stack creation progress
Managed resources for EKS

🔗 CloudFormation Dashboard
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/cloudformation_dashboard.png

👉 This confirms:

Stack successfully created
All services (VPC, IAM, Nodes) ready
EKS backend setup complete
🔗 Connect to Cluster
aws eks update-kubeconfig --name flask-cluster --region ap-south-1

👉 This command connects your local system to the EKS cluster.

🚀 Deploy Application
kubectl apply -f k8s/

🔗 Pods Running (EKS)
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/Monitoring_pods_running.png

👉 This shows:

Application + monitoring pods running
Multi-component Kubernetes deployment
Cluster health is stable
🌐 Ingress Setup
kubectl apply -f k8s/ingress.yaml

🔗 Ingress Working
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/ingress_domain_working.png

👉 This shows:

Public URL access working
AWS LoadBalancer created
External traffic routing to app
📊 Monitoring (Prometheus + Grafana)
helm install monitoring prometheus-community/kube-prometheus-stack

🔗 Monitoring Pods
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/Monitoring_pods_running.png

👉 This confirms:

Prometheus & Grafana pods running
Monitoring stack deployed
Metrics collection active
📈 Grafana Dashboard
kubectl port-forward svc/monitoring-grafana 3000:80

🔗 Grafana Dashboard
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/graphana_dashboard.png

👉 This shows:

Real-time metrics visualization
CPU, Memory usage
Cluster health dashboards
⚡ Auto Scaling (HPA)
kubectl autoscale deployment flask-app --cpu-percent=50 --min=1 --max=5

🔗 HPA Output
https://raw.githubusercontent.com/tanvishinde017/flask-k8s-cicd-aws-devops/main/screenshot2/HPA_showing_min_max_pods.png

👉 This shows:

Auto scaling configuration
Min and max pod limits
Dynamic scaling based on load
🌍 Final Output
http://<your-loadbalancer-url>

👉 Application is publicly accessible via AWS LoadBalancer.

🧠 Key Learnings
EKS (Managed Kubernetes)
CI/CD Automation
Monitoring with Grafana
Auto Scaling (HPA)
Ingress Networking
👩‍💻 Author

Tanavi Shinde
DevOps | AWS | Kubernetes