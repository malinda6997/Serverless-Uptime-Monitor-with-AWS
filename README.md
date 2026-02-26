# 🚀 Serverless Website Uptime Monitor & Alerting System

<div align="center">

**Enterprise-Grade Cloud Monitoring Solution**

**A Fully Automated AWS + Python + GitHub Actions Infrastructure**

![Deployment Status](https://img.shields.io/badge/Status-Production-green)
![AWS](https://img.shields.io/badge/Infrastructure-AWS-orange)
![Python](https://img.shields.io/badge/Language-Python-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub--Actions-brightgreen)
![License](https://img.shields.io/badge/License-Open--Source-purple)

</div>

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Architecture](#project-architecture)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [CI/CD Pipeline - GitHub Actions](#cicd-pipeline---github-actions)
- [Monitoring & Results](#monitoring--results)
- [Troubleshooting](#troubleshooting)
- [What I Learned](#what-i-learned)
- [Contact & Support](#contact--support)

---

## 🎯 Project Overview

**Serverless Website Uptime Monitor** is a robust, cloud-native solution designed to ensure high availability for web applications. The system performs automated health checks every 5 minutes and triggers real-time email alerts via Amazon SNS if any downtime is detected.

✅ **Fully Automated** - Scheduled health checks every 5 minutes.
✅ **Cloud-Native Hosting** - Operates entirely on AWS Lambda (No servers to manage).
✅ **Automated CI/CD** - Seamless deployment using GitHub Actions.
✅ **Real-Time Alerting** - Instant email notifications via AWS SNS.
✅ **Production Ready** - Includes logging, error handling, and performance metrics.

---

## ✨ Key Features

### 📊 **Automated Health Monitoring**
- Automated HTTP status code validation (200 OK checks).
- Capability to monitor multiple endpoints simultaneously.

### 🔄 **Continuous Integration/Deployment**
- Automated workflow to update AWS Lambda on every code push.
- Secure credential management using GitHub Action Secrets.

### ☁️ **Enterprise Observability**
- Detailed execution logs via Amazon CloudWatch.
- Performance metrics tracking (Duration, Success rate, Errors).

---

## 🛠️ Technology Stack

| Category | Technology | Purpose |
|:--- |:--- |:--- |
| **Language** | **Python (Boto3)** | Logic & AWS SDK |
| **Compute** | **AWS Lambda** | Serverless Execution |
| **Messaging** | **AWS SNS** | Real-time Email Alerts |
| **Scheduler** | **AWS EventBridge** | 5-Minute Cron Trigger |
| **Monitoring** | **CloudWatch** | Logs & Metrics |
| **DevOps** | **GitHub Actions** | CI/CD Automation |

---

## 🏗️ Project Architecture

```mermaid
graph TD
    A[GitHub Push] --> B[GitHub Actions CI/CD]
    B --> C[AWS Lambda Function]
    D[EventBridge Scheduler] -->|Every 5 Mins| C
    C -->|HTTP Request| E[Target Website]
    C -->|Failure Detected| F[AWS SNS Topic]
    F -->|Email Alert| G[Administrator Inbox]
    C -->|Logs/Metrics| H[Amazon CloudWatch]