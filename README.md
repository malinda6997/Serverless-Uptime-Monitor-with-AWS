
# 📡 AWS Serverless Website Monitoring & Alerting System

## 📌 Project Overview
This project is a **real-world AWS serverless monitoring system** built to continuously monitor website availability and response time.
When a website goes **down** or becomes **slow**, the system automatically sends **alerts via Amazon SNS**.

The solution is **fully serverless**, scalable, and cost-efficient, making it suitable for production use and DevOps/Cloud portfolios.

---

## 🏗️ System Architecture

### Architecture Flow
```

Amazon EventBridge (Schedule)
|
v
AWS Lambda (Python)
|
|----> Amazon CloudWatch Logs
|
|----> Amazon SNS (Email Alerts)

```

### Architecture Explanation
- EventBridge triggers Lambda at fixed intervals
- Lambda checks website status and response time
- CloudWatch stores logs
- SNS sends alerts when issues are detected

---

## 🌍 Real-World Use Cases
- Website uptime monitoring
- Production health checks
- Startup MVP monitoring
- DevOps automation
- Cloud / DevOps portfolio project

---

## ⚙️ Technologies Used
- AWS Lambda
- Amazon EventBridge
- Amazon SNS
- Amazon CloudWatch
- Python
- GitHub Actions
- Vercel-hosted website (monitored target)

---

## 🧠 What I Learned From This Project
- Designing event-driven serverless architectures
- Monitoring real systems using AWS Lambda
- Implementing alerting mechanisms with SNS
- Analyzing logs using CloudWatch
- Writing production-ready Python code
- Understanding serverless cost efficiency

---

## 📁 Project Structure
```

aws-serverless-monitor-project-01/
├── lambda_function.py
├── README.md   
└── .gitignore

````

---

## 🔧 Setup & Implementation (Step-by-Step)

### Step 01 – Create SNS Topic
![Step 01](Readme-images/SNS-1.png)
![Step 01](Readme-images/SNS-2.png)
![Step 01](Readme-images/SNS-3.png)
![Step 01](Readme-images/SNS-4.png)
![Step 01](Readme-images/SNS-5.png)

---

### Step 02 – Subscribe Email to SNS Topic
![Step 02](Readme-images/SNS-6-aws-confirm-mail.png)

---

### Step 03 – Create IAM Role
![Step 03](Readme-images/IAM%20Role-1.png)
![Step 03](Readme-images/IAM%20Role-2.png)
![Step 03](Readme-images/IAM%20Role-3.png)
![Step 03](Readme-images/IAM%20Role-4.png)
![Step 03](Readme-images/IAM%20Role-5.png)
![Step 03](Readme-images/IAM%20Role-6.png)
![Step 03](Readme-images/IAM%20Role-7.png)

---

### Step 04 – Configuring GitHub Secrets (AWS Credentials)
To enable automated deployment via GitHub Actions, you must securely store your AWS credentials as repository secrets. This ensures your keys are never exposed in the source code.

Follow these steps to add secrets:

- Go to your GitHub Repository → Settings.
- On the left sidebar, click Secrets and variables → Actions.
- Click the New repository secret button.
Add the following secrets one by one:
![Step 04](Readme-images/git-action-variables.png)

---

### Step 05 – Create Lambda Function
![Step 05](Readme-images/Lambda-1.png)
![Step 05](Readme-images/Lambda-permission.png)
![Step 05](Readme-images/successfull-create-lambda.png)


---

### Step 06 – Test Lambda Fuction
![Step 06](Readme-images/lambda-test-pass.png)

---

### Step 07 – Deploy Lambda Code Using Git Action
![Step 07](Readme-images/successful-deploy-gitaction-to-lambda.png)

---

### Step 08 – Configure Website URLs
![Step 08](Readme-images/08.png)

---

### Step 09 – Add SNS Topic ARN
![Step 09](Readme-images/09.png)

---

### Step 10 – Save & Deploy Lambda
![Step 10](Readme-images/10.png)

---

### Step 11 – Enable CloudWatch Logging
![Step 11](Readme-images/11.png)

---

### Step 12 – View CloudWatch Log Group
![Step 12](Readme-images/12.png)

---

### Step 13 – Create EventBridge Rule
![Step 13](Readme-images/13.png)

---

### Step 14 – Configure Schedule
![Step 14](Readme-images/14.png)

---

### Step 15 – Set Lambda as Target
![Step 15](Readme-images/15.png)

---

### Step 16 – Rule Enabled
![Step 16](Readme-images/16.png)

---

### Step 17 – Website Running Normally
![Step 17](Readme-images/17.png)

---

### Step 18 – Normal Execution Logs
![Step 18](Readme-images/18.png)

---

### Step 19 – Website Goes Down
![Step 19](Readme-images/19.png)

---

### Step 20 – Downtime Detected in Logs
![Step 20](Readme-images/20.png)

---

### Step 21 – SNS Alert Triggered
![Step 21](Readme-images/21.png)

---

### Step 22 – Email Alert Received
![Step 22](Readme-images/22.png)

---

### Step 23 – Website Restored
![Step 23](Readme-images/23.png)

---

### Step 24 – Recovery Logged
![Step 24](Readme-images/24.png)

---

### Step 25 – Performance Monitoring
![Step 25](Readme-images/25.png)

---

### Step 26 – Slow Response Detection
![Step 26](Readme-images/26.png)

---

### Step 27 – Latency Alert
![Step 27](Readme-images/27.png)

---

### Step 28 – GitHub Repository Setup
![Step 28](Readme-images/28.png)

---

### Step 29 – GitHub Actions Workflow
![Step 29](Readme-images/29.png)

---

### Step 30 – Final Project Verification
![Step 30](Readme-images/30.png)

---

## 🚀 Clone & Setup Instructions

```bash
git clone https://github.com/malinda6997/Serverless-Uptime-Monitor-with-AWS/tree/main
````

### Setup Summary

1. Create SNS topic
2. Create Lambda function
3. Paste monitoring code
4. Configure EventBridge schedule
5. Test downtime & alerts

---

## 📈 Why This Project Is Important

* Demonstrates real-world cloud monitoring
* Uses production-grade AWS services
* Fully serverless and scalable
* Strong DevOps / Cloud portfolio project

---

## 🔮 Future Improvements

* Store metrics in DynamoDB
* Slack / Discord alerts
* Terraform or AWS CDK deployment
* CloudWatch dashboards

---

## 👤 Author

**Malinda**
AWS Serverless Monitoring Project

```

---
