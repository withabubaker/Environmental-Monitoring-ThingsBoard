
import paho.mqtt.client as mqtt
import time
import os
from helpers import fetch_temp_hum, update_temp_Hum_dashboard, sns_notification

 
MQTT_Broker = '192.168.2.75'  # Thingsboard MQTT broker address
S1_ACCESS_TOKEN =os.getenv('S1_ACCESS_TOKEN')
url = "http://192.168.2.75:3001/devices/ac233fa4d282/2"


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
                #sns_notification(payload)
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

