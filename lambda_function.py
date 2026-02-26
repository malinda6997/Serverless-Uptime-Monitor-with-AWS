import urllib.request
import boto3
import os
import time
import json

def send_discord_message(webhook_url, message):
    data = json.dumps({"content": message}).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

def lambda_handler(event, context):
    # --- CONFIGURATION ---

    SITES = [
        {"name": "Portfolio", "url": "https://your-site.vercel.app-error"},
       # {"name": "Blog", "url": "https://blog.vercel.app"}
    ]
    
    SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:460678531463:VercelMonitorAlert"
    # DISCORD_WEBHOOK = "https://discord.com/api/webhooks/your-id-here" # Optional
    
    sns = boto3.client('sns')
    
    for site in SITES:
        start_time = time.time()
        try:
            response = urllib.request.urlopen(site['url'], timeout=10)
            end_time = time.time()
            

            duration = round((end_time - start_time) * 1000)
            
            print(f"✅ {site['name']} is UP. Response time: {duration}ms")
            

            if duration > 3000:
                msg = f"⚠️ WARNING: {site['name']} is SLOW ({duration}ms)!"
                sns.publish(TopicArn=SNS_TOPIC_ARN, Message=msg, Subject="Performance Alert")

        except Exception as e:
            error_msg = f"🚨 ALERT: {site['name']} is DOWN!\nURL: {site['url']}\nError: {str(e)}"
            print(error_msg)
            
            sns.publish(TopicArn=SNS_TOPIC_ARN, Message=error_msg, Subject="Site Down Alert")
            

    return {"status": "Monitoring Complete"}
        