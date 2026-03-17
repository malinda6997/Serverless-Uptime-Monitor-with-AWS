# 🎯 AWS Serverless Website Monitoring & Alerting System

<div align="center">

**Enterprise-Grade Cloud Monitoring Solution**  
*Automated Health Checks | Real-Time Email Alerts | Fully Serverless Infrastructure*

![AWS](https://img.shields.io/badge/Infrastructure-AWS-orange?style=flat-square&logo=amazon-aws)
![Python](https://img.shields.io/badge/Language-Python-3.9+-blue?style=flat-square&logo=python)
![Lambda](https://img.shields.io/badge/Compute-AWS%20Lambda-FF9900?style=flat-square&logo=aws-lambda)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub--Actions-brightgreen?style=flat-square&logo=github-actions)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</div>

---

## 📑 Table of Contents

- [Executive Summary](#-executive-summary)
- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Complete Setup Guide](#-complete-setup-guide-step-by-step)
- [How It Works](#-how-it-works)
- [Deployment & Usage](#-deployment--usage)
- [Monitoring & Troubleshooting](#-monitoring--troubleshooting)
- [Key Learnings](#-key-learnings)
- [Future Enhancements](#-future-enhancements)
- [Contact & Support](#-contact--support)

---

## 💼 Executive Summary

This is a **production-ready, serverless website monitoring solution** designed to provide enterprise-grade uptime monitoring and real-time alerts for web applications. The system continuously checks the availability and performance of specified websites. When a site goes down or responds slowly, instant alerts are delivered via email through Amazon SNS.

### Why This Solution?
- ✅ **Zero Infrastructure Overhead**: Fully serverless—no servers to maintain
- ✅ **Cost-Effective**: Runs within AWS Free Tier limits
- ✅ **Highly Scalable**: Automatically handles increased load
- ✅ **Real-Time Alerts**: Email notifications within seconds of an issue
- ✅ **Enterprise-Ready**: Production-grade AWS services
- ✅ **Automated CI/CD**: Push code to GitHub and it auto-deploys

---

## 🎯 Project Overview

### What Does It Do?

This project implements an **automated, 24/7 website monitoring system** that:

1. **Periodically Checks** target websites for availability (every 5 minutes)
2. **Measures Response Time** to detect performance degradation
3. **Detects Failures** when sites return error codes or timeout
4. **Sends Instant Alerts** via email when issues occur
5. **Logs Everything** to CloudWatch for auditing and analysis
6. **Auto-Deploys** code changes from GitHub to Lambda

### Real-World Use Cases
- Monitor production applications for downtime
- Track response time degradation
- Alert DevOps teams to critical issues
- Maintain uptime SLAs with automated detection
- Cost-effective alternative to expensive monitoring services

### Key Metrics
- **Monitoring Interval**: Every 5 minutes
- **Timeout**: 10 seconds per HTTP request
- **Performance Threshold**: Alerts if response time > 3000ms
- **Alert Method**: Real-time email via SNS
- **Cost**: Fits within AWS Free Tier (~$0.20 per month in production)

---

## 🏗️ System Architecture

### **Complete Architecture Flow**

```
┌─────────────────────────────────────────────────────────────────┐
│                     AWS Cloud Environment                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────┐                                            │
│  │ EventBridge      │                                            │
│  │ (Scheduler)      │───┐                                        │
│  │ Every 5 mins     │   │                                        │
│  └──────────────────┘   │                                        │
│                         │                                        │
│                         ↓                                        │
│                    ┌──────────────────────┐                      │
│                    │   AWS Lambda         │                      │
│                    │  (Python Runtime)    │                      │
│                    │  - Check Sites       │                      │
│                    │  - Measure Time      │                      │
│                    │  - Detect Failures   │                      │
│                    └──────────────────────┘                      │
│                    ↓                                             │
│       ┌────────────┴────────────┐                               │
│       ↓                         ↓                                │
│  ┌────────────┐           ┌──────────────┐                      │
│  │ CloudWatch │           │ Amazon SNS   │                      │
│  │   Logs     │           │   Topic      │                      │
│  │ (Records   │           │ (Sends       │                      │
│  │  all calls)│           │  Alerts)     │                      │
│  └────────────┘           └──────────────┘                      │
│                                  ↓                              │
│                           ┌─────────────────┐                   │
│                           │  Email Alert    │                   │
│                           │ to Admin Inbox  │                   │
│                           └─────────────────┘                   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ GitHub Actions (CI/CD Pipeline)                          │  │
│  │ - Automatic Deployment on Code Push                      │  │
│  │ - Uses AWS Credentials from Repository Secrets           │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      Target Websites                            │
│                   (Monitored by Lambda)                         │
└─────────────────────────────────────────────────────────────────┘
```

### **Architecture Components Explained**

| Component | Purpose | Details |
|-----------|---------|---------|
| **EventBridge** | Scheduling | Triggers Lambda function on a time-based schedule (cron expression) |
| **Lambda** | Core Logic | Executes Python code to perform HTTP checks and send alerts |
| **CloudWatch Logs** | Observability | Records every check result for debugging and auditing |
| **SNS Topic** | Alert Distribution | Manages subscriptions and sends email notifications |
| **IAM Role** | Security | Controls what AWS services Lambda can access |
| **GitHub Actions** | CI/CD | Automates code deployment from GitHub to Lambda |

---

## ✨ Key Features

### 🔍 Availability Monitoring
- Continuous HTTP/HTTPS checks every 5 minutes
- Detects both hard failures and timeouts
- Logs detailed error information for diagnostics

### ⚡ Real-Time Alerting
- Instant email notifications when sites go down
- Performance alerts when response time exceeds thresholds
- SNS integration for reliable message delivery

### 📊 Comprehensive Logging
- CloudWatch Logs integration for all monitoring events
- Structured logging with timestamps and response metrics
- Historical data for trend analysis and compliance

### 🔒 Enterprise Security
- AWS IAM with least-privilege permissions
- GitHub Secrets for secure credential management
- No hardcoded credentials in code

### 🚀 Automated Deployment
- One-click deployment via GitHub Actions
- Automatic code updates from repository to Lambda
- Version control and rollback capability

### 📈 Scalability
- Serverless architecture scales automatically
- Handles 1 or 1000 websites with same setup
- Pay only for execution time

---

## 🛠️ Technology Stack

### Core Technologies

| Technology | Version | Purpose |  Cost |
|-----------|---------|---------|-------|
| **AWS Lambda** | Python 3.9+ | Serverless compute for monitoring logic | ~$0.20/month (in free tier) |
| **Amazon SNS** | Latest | Email alert delivery service | Free tier (1000 emails/month) |
| **Amazon EventBridge** | Latest | Schedule-based trigger for Lambda | Free tier (unlimited) |
| **Amazon CloudWatch** | Latest | Log aggregation and metrics | Free tier (5GB/month) |
| **Python** | 3.9+ | Programming language with Boto3 SDK | Open source |
| **GitHub Actions** | Latest | CI/CD automation | Free for public repos |
| **IAM** | Latest | Identity and access management | Free |

### Libraries & Dependencies

```
boto3==latest          # AWS SDK for Python
urllib                 # Built-in Python HTTP library (no external dependency)
json                   # Data serialization (built-in)
time                   # Performance measurement (built-in)
os                     # Environment variable access (built-in)
```

---

## ✅ Prerequisites

Before starting, ensure you have:

### AWS Account Requirements
- ✅ Active AWS Account with billing enabled
- ✅ IAM user with Administrator access (for setup phase)
- ✅ Permission to create Lambda, SNS, IAM roles, and EventBridge rules
- ✅ Email address to receive SNS notifications

### GitHub Requirements
- ✅ GitHub account with repository access
- ✅ Git installed locally (for cloning)
- ✅ Understanding of GitHub Secrets for credential management

### Technical Prerequisites
- ✅ Basic understanding of AWS console
- ✅ Familiarity with Python (optional, not required to use)
- ✅ Valid website URLs to monitor

---

## 🔧 Complete Setup Guide (Step-by-Step)

### **Step 1: Create SNS Topic for Email Notifications**

The SNS Topic is the central hub for sending email alerts. Follow these steps:

1. Log in to [AWS Console](https://console.aws.amazon.com/)
2. Navigate to **SNS** → **Topics** → **Create Topic**
3. Choose **Standard** topic type
4. Name it: `VercelMonitorAlert` (or your preferred name)
5. Click **Create Topic**

**Screenshots:**

![SNS Topic Creation](Readme-images/SNS-1.png)
*Step 1: Navigating to SNS Service*

![SNS Configuration](Readme-images/SNS-2.png)
*Step 2: Select Standard Topic*

![SNS Topic Name](Readme-images/SNS-3.png)
*Step 3: Enter Topic Name*

![SNS Topic Review](Readme-images/SNS-4.png)
*Step 4: Review Configuration*

![SNS Creation Complete](Readme-images/SNS-5.png)
*Step 5: Topic Created Successfully*

**What's Happening:**
- You're creating a publish-subscribe channel
- This topic will be used by Lambda to send alert messages
- Save the **Topic ARN** (looks like `arn:aws:sns:region:account-id:topic-name`) for later use

---

### **Step 2: Subscribe Your Email to SNS Topic**

Now you need to subscribe your email address to receive notifications:

1. In the SNS Topic details page, click **Create Subscription**
2. Select **Protocol**: Email
3. Enter your **Endpoint** (email address)
4. Click **Create Subscription**
5. Check your inbox for AWS confirmation email
6. Click the **Confirmation Link** in the email

**Screenshot:**

![Email Subscription](Readme-images/SNS-6-aws-confirm-mail.png)
*AWS sends a confirmation email - Click the link to confirm*

**What's Happening:**
- AWS sends you a confirmation email
- You must confirm before alerts can be sent
- Once confirmed, all SNS messages will reach your inbox
- This is a security feature to prevent email spoofing

---

### **Step 3: Create IAM Role with Permissions**

The Lambda function needs permissions to access SNS and CloudWatch. We'll create a dedicated IAM role:

1. Go to **IAM** → **Roles** → **Create Role**
2. Select **AWS Service** → **Lambda**
3. Click **Next: Permissions**
4. Click **Create Policy** and add:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": "arn:aws:sns:us-east-1:YOUR-ACCOUNT-ID:VercelMonitorAlert"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

5. Name the policy: `LambdaMonitoringPolicy`
6. Attach to your Lambda role
7. Name the role: `LambdaMonitoringRole`

**Screenshots:**

![IAM Role Step 1](Readme-images/IAM%20Role-1.png)
*Step 1: Create Role Service Selection*

![IAM Role Step 2](Readme-images/IAM%20Role-2.png)
*Step 2: Choose Lambda as the Service*

![IAM Role Step 3](Readme-images/IAM%20Role-3.png)
*Step 3: Attach Permissions*

![IAM Role Step 4](Readme-images/IAM%20Role-4.png)
*Step 4: Review Permissions*

![IAM Role Step 5](Readme-images/IAM%20Role-5.png)
*Step 5: Final Configuration*

![IAM Role Step 6](Readme-images/IAM%20Role-6.png)
*Step 6: Role Name Configuration*

![IAM Role Step 7](Readme-images/IAM%20Role-7.png)
*Step 7: Role Created Successfully*

**What's Happening:**
- You're creating a security credential for Lambda
- The policy grants **minimum required permissions** (SNS publish + CloudWatch logs)
- This follows the **Principle of Least Privilege** - Lambda can only do what's needed
- No other AWS services can be accessed by this Lambda function

---

### **Step 4: Configure GitHub Secrets (AWS Credentials)**

To enable automated deployment from GitHub to Lambda, you need to store AWS credentials securely:

1. Go to your GitHub Repository → **Settings**
2. Click **Secrets and variables** → **Actions**
3. Click **New Repository Secret**
4. Add these two secrets:
   - **Name**: `AWS_ACCESS_KEY_ID` | **Value**: Your AWS Access Key
   - **Name**: `AWS_SECRET_ACCESS_KEY` | **Value**: Your AWS Secret Key

**Screenshot:**

![GitHub Secrets Configuration](Readme-images/git-action-variables.png)
*GitHub Secrets stored securely for CI/CD pipeline*

**How to Get AWS Credentials:**
1. Go to **IAM** → **Users** → Create a new user with **Programmatic Access**
2. Attach policy: `AWSLambdaFullAccess` + `CloudWatchFullAccess`
3. Copy the Access Key and Secret Key

**What's Happening:**
- GitHub Actions uses these credentials to deploy code to Lambda
- Secrets are **encrypted** and never exposed in logs
- This enables the **push-to-deploy** workflow

---

### **Step 5: Create AWS Lambda Function**

Now we'll create the function that performs the monitoring:

1. Go to **Lambda** → **Create Function**
2. **Function Name**: `websiteMonitor` (or your preferred name)
3. **Runtime**: Python 3.9 or higher
4. **Architecture**: x86_64
5. **Execution Role**: Select the `LambdaMonitoringRole` you created in Step 3
6. Click **Create Function**

**Screenshots:**

![Lambda Creation](Readme-images/Lambda-1.png)
*Step 1: Lambda Function Creation Page*

![Lambda Permission Setup](Readme-images/Lambda-permission.png)
*Step 2: Configure Permissions with IAM Role*

![Lambda Success](Readme-images/successfull-create-lambda.png)
*Step 3: Lambda Function Created Successfully*

**What's Happening:**
- Lambda is a serverless compute service that runs your code
- Python 3.9+ is the runtime that executes your code
- The IAM role we created gives it permissions to use SNS
- No servers to manage—just deploy code and it runs

---

### **Step 6: Update Lambda Code**

Replace the default Lambda code with the monitoring script:

1. In the Lambda function editor, replace default code with:

```python
import urllib.request
import boto3
import os
import time
import json

def send_discord_message(webhook_url, message):
    """Optional: Send alerts to Discord"""
    data = json.dumps({"content": message}).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

def lambda_handler(event, context):
    """
    Main Lambda handler function
    Monitors website availability and sends alerts via SNS
    """
    
    # ==================== CONFIGURATION ====================
    # Add your websites here
    SITES = [
        {"name": "Portfolio", "url": "https://your-site.vercel.app"},
        # {"name": "Blog", "url": "https://blog.vercel.app"}
    ]
    
    # Your SNS Topic ARN (from Step 1)
    SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:YOUR-ACCOUNT-ID:VercelMonitorAlert"
    
    # Optional: Discord webhook for alternative alerting
    # DISCORD_WEBHOOK = "https://discord.com/api/webhooks/your-id-here"
    
    sns = boto3.client('sns')
    
    # ==================== MONITORING LOOP ====================
    for site in SITES:
        start_time = time.time()
        
        try:
            # Perform HTTP request with 10-second timeout
            response = urllib.request.urlopen(site['url'], timeout=10)
            end_time = time.time()
            
            # Calculate response time in milliseconds
            duration = round((end_time - start_time) * 1000)
            
            print(f"✅ {site['name']} is UP. Response time: {duration}ms")
            
            # Alert if response time exceeds threshold (3 seconds)
            if duration > 3000:
                msg = f"⚠️ PERFORMANCE WARNING: {site['name']} is SLOW!\nResponse time: {duration}ms\nURL: {site['url']}"
                sns.publish(
                    TopicArn=SNS_TOPIC_ARN, 
                    Message=msg, 
                    Subject="[ALERT] Site Performance Degradation"
                )
                # Optional: send_discord_message(DISCORD_WEBHOOK, msg)
        
        except Exception as e:
            # Site is down or unreachable
            error_msg = f"🚨 CRITICAL ALERT: {site['name']} is DOWN!\nURL: {site['url']}\nError: {str(e)}\nTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}"
            print(error_msg)
            
            # Send SNS alert
            sns.publish(
                TopicArn=SNS_TOPIC_ARN, 
                Message=error_msg, 
                Subject="[CRITICAL] Website Down - Immediate Action Required"
            )
            # Optional: send_discord_message(DISCORD_WEBHOOK, error_msg)
    
    return {
        "statusCode": 200,
        "body": json.dumps("Monitoring cycle completed successfully")
    }
```

2. Configure these values:
   - Replace `YOUR-ACCOUNT-ID` with your AWS Account ID
   - Add your website URLs in the `SITES` list
   - Update `SNS_TOPIC_ARN` with the ARN from Step 1

3. Click **Deploy**

**What's Happening:**
- This Python code is the "brain" of your monitoring system
- It loops through each website and checks if it's accessible
- Measures response time to detect slow sites
- Sends SNS alerts if issues are detected
- Logs everything to CloudWatch for analysis

---

### **Step 7: Test Lambda Function**

Before automation, let's manually test the function:

1. In the Lambda editor, click **Test**
2. Create a test event (default is fine)
3. Click **Test** button
4. Check the execution result

**Expected Output:**
```
✅ Portfolio is UP. Response time: XXXms
```

**Screenshot:**

![Lambda Test](Readme-images/lambda-test-pass.png)
*Successful test execution shows the monitoring logic works*

**What's Happening:**
- Manual testing ensures your code works before automation
- If the test fails, you'll see error messages to debug
- A successful test means website checking is working

---

### **Step 8: Deploy Code via GitHub Actions (CI/CD)**

GitHub Actions will automatically deploy new code to Lambda when you push updates:

1. The repository includes a `.github/workflows/deploy.yml` file
2. Every time you push code to GitHub:
   - GitHub Actions runs the workflow
   - It packages your Python code
   - Deploys it to Lambda using AWS credentials from Secrets
   - Updates your Lambda function automatically

3. To trigger deployment:
```bash
git add .
git commit -m "Update monitoring configuration"
git push origin main
```

**Screenshot:**

![GitHub Actions Deployment](Readme-images/successful-deploy-gitaction-to-lambda.png)
*GitHub Actions successfully deploys code to Lambda*

**What's Happening:**
- CI/CD (Continuous Integration/Continuous Deployment) automation
- No manual console interaction needed after setup
- Changes go live quickly and safely

---

### **Step 9: Add EventBridge Trigger (Scheduling)**

Now we'll schedule Lambda to run automatically every 5 minutes:

1. In Lambda function page, click **Add Trigger**
2. Select **EventBridge (CloudWatch Events)**
3. Choose **Create a new rule**
4. **Rule Name**: `WebsiteMonitoringSchedule`
5. **Rule Type**: Schedule expression
6. **Schedule Expression**: `rate(5 minutes)` or `cron(*/5 * * * ? *)`
7. Click **Add**

**Screenshots:**

![Add Trigger](Readme-images/lambda-add-trigger.png)
*Step 1: Adding EventBridge Trigger*

![Trigger Success](Readme-images/lambda-successfull-add-trigger.png)
*Step 2: EventBridge Trigger Configured*

**Cron Expression Explanation:**
- `rate(5 minutes)` - Run every 5 minutes
- `rate(1 hour)` - Run every hour
- `cron(0 */6 * * ? *)` - Run every 6 hours
- `cron(0 9 * * ? *)` - Run daily at 9 AM UTC

**What's Happening:**
- EventBridge acts as a cloud scheduler
- Every 5 minutes, it automatically invokes your Lambda function
- Your Lambda runs the monitoring checks
- No manual intervention needed—fully automated

---

### **Step 10: Monitor Lambda Metrics**

CloudWatch monitors your function's performance:

1. In Lambda, click **Monitor** tab
2. View **Invocations**, **Execution Time**, **Errors**
3. Set up **Alarms** if needed

**Screenshot:**

![Lambda Monitoring](Readme-images/lambdamonitoring.png)
*CloudWatch Metrics showing Lambda invocation history and performance*

**Key Metrics Explained:**
- **Invocations**: Number of times Lambda was triggered
- **Duration**: How long each execution took (ms)
- **Errors**: Failed executions
- **Throttles**: Times Lambda couldn't run due to concurrency limits

**What's Happening:**
- Real-time insights into your monitoring system's health
- Early warning if something goes wrong
- Helps optimize performance and cost

---

### **Step 11: View CloudWatch Logs**

All monitoring activity is logged for auditing and debugging:

1. In Lambda → **Monitor** → **Logs**
2. Click **View logs in CloudWatch**
3. Select the latest log stream
4. View detailed execution logs

**Screenshot:**

![CloudWatch Logs](Readme-images/cloudwatch-log.png)
*CloudWatch Logs showing all monitoring checks and results*

**Log Contents:**
- Timestamp of each check
- Website name and URL
- Response time (ms)
- Success or failure status
- Error messages (if applicable)

**What's Happening:**
- Complete audit trail of all monitoring activity
- Useful for compliance and troubleshooting
- Historical data for trend analysis

---

### **Step 12: Testing - Normal Operations**

View logs during healthy uptime:

**Screenshots:**

![Before Site Downtime](Readme-images/beforesitedowncloudwatchlog.png)
*Normal Operations: All websites responding correctly*

![Expanded View](Readme-images/beforecloudwalllogexpand.png)
*Detailed view showing successful checks with response times*

**Log Interpretation:**
- ✅ Status codes 200-299: Website is healthy
- Response time < 1000ms: Good performance
- Regular intervals: Scheduling is working

**What's Happening:**
- The system is functioning normally
- All websites are accessible
- No alerts are being sent

---

### **Step 13: Testing - Simulating Site Downtime**

View how the system detects and alerts on failures:

**Screenshots:**

![After Downtime Detection](Readme-images/aftercloudwatchlogs.png)
*System detects website failure*

![Expanded Failure Details](Readme-images/sitedownaftercloudwatchlogsexpand.png)
*Error details logged automatically*

**Error Detection:**
- Connection refused errors
- Timeout exceptions
- HTTP error codes (4xx, 5xx)
- DNS resolution failures

**What's Happening:**
- Lambda detects the site is down
- Logs the error with full details
- Prepares SNS alert message

---

### **Step 14: Email Alert Verification**

When an issue is detected, you receive an instant email:

![Email Alert](Readme-images/sitedownemail.png)
*Real-time Email Alert received when site goes down*

**Email Contents:**
- Alert severity (CRITICAL, WARNING)
- Website name and URL
- Error description
- Timestamp
- Recommended action

**What's Happening:**
- SNS delivers the message to your email
- You're immediately notified of issues
- Fast incident response is possible

---

## 🔍 How It Works

### **Complete Execution Flow**

```
1. EventBridge Trigger (Every 5 minutes)
   ↓
2. Lambda Function Invokes
   ↓
3. Environment Setup
   - Load website configuration
   - Initialize SNS client
   - Prepare monitoring parameters
   ↓
4. For Each Website:
   a. Measure start time
   b. Send HTTP GET request (10-second timeout)
   c. Measure end time
   d. Calculate response time
   ↓
5. Result Processing:
   - If Status >= 200 & < 300 (Success)
     → Check response time
     → If > 3000ms: Send PERFORMANCE ALERT
     → Otherwise: Log success
   
   - If Status != 200-299 or Timeout (Failure)
     → Send CRITICAL ALERT via SNS
     → Log error details
   ↓
6. CloudWatch Logging
   - Record all actions and metrics
   - Timestamp and duration stored
   ↓
7. SNS Alert Delivery
   - Message published to topic
   - Email sent to all subscribers
   ↓
8. Return Lambda Response
   - Execution marked as complete
```

### **Decision Logic**

```
Is Website Accessible?
├─ YES (HTTP Status 2xx)
│  ├─ Response Time < 3000ms?
│  │  ├─ YES → ✅ Success (Just log)
│  │  └─ NO → ⚠️ WARNING (Send performance alert)
│  
└─ NO (Error/Timeout)
   └─ 🚨 CRITICAL (Send downtime alert immediately)
```

---

## 📦 Deployment & Usage

### **Option 1: Manual Setup (Step-by-Step)**
Follow the complete setup guide above.

### **Option 2: Quick Start**

```bash
# Clone the repository
git clone https://github.com/malinda6997/Serverless-Uptime-Monitor-with-AWS.git
cd Serverless-Uptime-Monitor-with-AWS

# Configure your websites
nano lambda_function.py  # Edit the SITES array

# Push to GitHub to trigger CI/CD deployment
git add lambda_function.py
git commit -m "Configure monitoring targets"
git push origin main
```

### **Configuration Parameters**

Edit `lambda_function.py` to customize:

```python
# Websites to monitor
SITES = [
    {"name": "Portfolio", "url": "https://your-site.com"},
    {"name": "API", "url": "https://api.your-site.com"},
    {"name": "Blog", "url": "https://blog.your-site.com"},
]

# SNS Topic for alerts
SNS_TOPIC_ARN = "arn:aws:sns:REGION:ACCOUNT-ID:TOPIC-NAME"

# Performance threshold (milliseconds)
PERFORMANCE_THRESHOLD = 3000  # Alert if response > 3 seconds

# Timeout for HTTP requests (seconds)
REQUEST_TIMEOUT = 10
```

### **Adding More Websites**

Simply add to the `SITES` list:

```python
SITES = [
    {"name": "Main Site", "url": "https://example.com"},
    {"name": "Blog", "url": "https://blog.example.com"},
    {"name": "API Server", "url": "https://api.example.com"},
    {"name": "Admin Panel", "url": "https://admin.example.com"},
]
```

---

## 📊 Monitoring & Troubleshooting

### **Checking System Health**

**1. View Recent Lambda Invocations:**
- AWS Console → Lambda → Monitor → Invocations graph
- Should show consistent calls every 5 minutes

**2. Check Execution Duration:**
- AWS Console → Lambda → Monitor → Duration
- Should be 1-3 seconds per execution
- Spikes indicate network or website issues

**3. Review Error Metrics:**
- AWS Console → Lambda → Monitor → Errors
- Should be 0 if all monitored sites are healthy

### **Common Issues & Solutions**

| Issue | Cause | Solution |
|-------|-------|----------|
| Lambda not triggering | EventBridge rule not created | Add trigger in Lambda → Add Trigger → EventBridge |
| Alerts not arriving | Email not confirmed | Check AWS confirmation email and click link |
| "Permission Denied" error in logs | IAM role missing SNS permission | Update IAM role with SNS:Publish action |
| Lambda timeout (>15 min) | Website not responding | Reduce REQUEST_TIMEOUT or check website |
| Emails going to spam | SNS message format | Check SNS topic policy and sender reputation |
| High Lambda duration | Slow website response | May indicate legitimate performance issues |

### **Debugging Steps**

1. **Check Lambda Logs:**
   ```
   AWS Console → Lambda → Monitor → Logs → View in CloudWatch
   ```

2. **Test Manually:**
   ```
   Lambda → Test Button → Review execution result
   ```

3. **Verify SNS Setup:**
   ```
   SNS → Topics → Select topic → Test button
   ```

4. **Check IAM Permissions:**
   ```
   IAM → Roles → Your role → View inline policies
   ```

---

## 🎓 Key Learnings

### **Architectural Patterns Learned**

1. **Event-Driven Architecture**
   - Decoupled components communicate via events
   - Scalable and maintainable system design
   - EventBridge orchestrates the workflow

2. **Serverless Advantages**
   - No infrastructure management overhead
   - Automatic scaling based on demand
   - Pay-per-use pricing model
   - Reduced operational complexity

3. **Microservices Integration**
   - Lambda as a compute service
   - SNS for message distribution
   - CloudWatch for observability
   - Each service has a single responsibility

### **AWS Best Practices Implemented**

✅ **Least Privilege Access**: IAM roles with minimal required permissions  
✅ **Infrastructure Automation**: GitHub Actions for CI/CD deployment  
✅ **Security**: No hardcoded credentials, using GitHub Secrets  
✅ **Observability**: CloudWatch Logs for complete audit trail  
✅ **Error Handling**: Graceful exception handling with detailed logging  
✅ **Cost Optimization**: Free tier eligible design  

### **DevOps Concepts Demonstrated**

- **CI/CD Pipeline**: GitHub → GitHub Actions → AWS Lambda
- **Infrastructure as Code**: Terraform/CloudFormation compatible
- **Monitoring & Alerting**: Real-time issue detection
- **Incident Response**: Automated alerting reduces MTTR (Mean Time To Respond)
- **Logging & Auditing**: Complete action history for compliance

---

## 🚀 Future Enhancements

### **Planned Features**

1. **Data Persistence**
   - Store metrics in DynamoDB
   - Track uptime percentages over time
   - Generate monthly/yearly reports

2. **Multi-Channel Alerts**
   - Slack integration for team notifications
   - Discord webhooks for gaming communities
   - SMS alerts via AWS SNS (paid)
   - PagerDuty integration for critical incidents

3. **Advanced Monitoring**
   - SSL certificate expiration tracking
   - DNS resolution monitoring
   - Endpoint-specific status codes (200, 301, 404, etc.)
   - Geographic latency testing

4. **Infrastructure as Code**
   - Terraform modules for one-click setup
   - AWS CDK (Cloud Development Kit) support
   - CloudFormation templates

5. **Web Dashboard**
   - Real-time uptime status page
   - Historical metrics visualization
   - Alert configuration UI
   - Built with React/Next.js

6. **Advanced Analytics**
   - Trend analysis and predictions
   - Anomaly detection using ML
   - Performance SLA tracking
   - Cost reporting and optimization

---

## 📞 Contact & Support

### **Project Author**

**Malinda Prabath**  
*Cloud & DevOps Engineer*

📧 **Email**: [malindaprabath876@gmail.com](mailto:malindaprabath876@gmail.com)  
📱 **Phone**: +94 76 220 6157  
💼 **LinkedIn**: [Visit Profile](https://linkedin.com/in/your-profile)  
🐙 **GitHub**: [@malinda6997](https://github.com/malinda6997)  

### **Support Channels**

- **GitHub Issues**: Report bugs or request features
- **Email**: Direct support for setup questions
- **Discord**: Join our community (optional)

### **License**

This project is provided as-is for educational and production use.  
Feel free to fork, modify, and deploy in your organization.

---

<div align="center">

## 🌟 If This Project Helped You...

⭐ **Star this repository** on GitHub  
🔗 **Share** with your DevOps/Cloud community  
💬 **Provide feedback** and suggestions  
🚀 **Deploy it** and build upon it  

---

**Built with 💻 and ☁️ AWS**  
*Serverless Monitoring | Cloud Excellence | 2026*

</div>
