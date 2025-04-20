import requests
import os
import json
import boto3

topic_arn = os.getenv('TOPIC_ARN')
sns = boto3.client('sns', region_name='us-east-1')

def fetch_temp_hum(url):
    try:
        response = requests.get(url)
        data = response.json()
        device_data = data.get('devices',{})
        temperature = device_data['ac233fa4d282/2']['dynamb'].get('temperature')
        humidity = device_data['ac233fa4d282/2']['dynamb'].get("relativeHumidity")

        payload = {

                "temperature": temperature,
                "humidity": humidity
        }
        return payload
    except requests.exceptions.RequestException as e:
        print("Error fetching the data:", e)
        return None
    
def update_temp_Hum_dashboard(client_S1,payload):
    try:
        if payload is None:
            print("No payload to send")
            return
        topic = "v1/devices/me/telemetry"
        client_S1.publish(topic, json.dumps(payload))
        print("Data sent to ThingBoard:", payload) 
    except Exception as e:
        print("An error occurred:", e)



def sns_notification(payload):
    try:
        if payload is None:
            print("No data")
            return
        if payload['temperature'] > 24:
            message = f"High Temperature Alert: {round(payload['temperature'])} °C"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
        if payload['humidity'] > 40:
            message = f"High Humidity Alert: {round(payload['humidity'])} R/H"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
    except Exception as e:
        print("An error occurred while sending SNS notification:", e)