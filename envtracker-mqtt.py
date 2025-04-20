import requests
import paho.mqtt.client as mqtt
import json
import time
import os
import boto3

 
MQTT_Broker = '192.168.2.75'  # Thingsboard MQTT broker address
S1_ACCESS_TOKEN =os.getenv('S1_ACCESS_TOKEN')
url = "http://192.168.2.75:3001/devices/ac233fa4d282/2"
sns = boto3.client('sns', region_name='us-east-1')
topic_arn = os.getenv('TOPIC_ARN')

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

        """
        if payload['temperature'] > 30:
            message = f"Temperature Alert: {payload['temperature']}°C"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
        if payload['humidity'] > 40:
            message = f"Humidity Alert: {payload['humidity']}%"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
        """
            
    except Exception as e:
        print("An error occurred:", e)
def sns_notification(payload):
    try:
        if payload is None:
            print("No data")
            return
        if payload['temperature'] > 30:
            message = f"High Temperature Alert: {payload['temperature']}°C"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
        if payload['humidity'] > 40:
            message = f"High Humidity Alert: {payload['humidity']}R/H"
            sns.publish(TopicArn=topic_arn, Message=message)
            print("Alert sent to SNS:", message)
    except Exception as e:
        print("An error occurred while sending SNS notification:", e)

def main():
    try:
        client_S1 = mqtt.Client()
        client_S1.username_pw_set(S1_ACCESS_TOKEN)
        client_S1.connect(MQTT_Broker, 1883, keepalive=60)
        client_S1.loop_start()
        while True:
            try:
                payload = fetch_temp_hum(url)
                update_temp_Hum_dashboard(client_S1,payload)
                sns_notification(payload)
                time.sleep(60)
            except Exception as e:
                print("error in Temperature and Humidity function:", e)

    except KeyboardInterrupt:
        print("User interupted")
    except Exception as e:
        print("An unexpected error occured:", e)

    finally:
        client_S1.loop_stop()
        client_S1.disconnect()

if __name__ == "__main__":
    main()

