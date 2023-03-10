from kafka import KafkaConsumer
import csv
import datetime as datetime
import os

consumer = KafkaConsumer('example1', bootstrap_servers='localhost:9092', group_id=None, auto_offset_reset='earliest')
if os.path.isfile('message.csv'):
    print("messages.csv already exists...\ndeleting...")
    os.remove('message.csv')

with open('message.csv', 'a') as f:
    fWriter = csv.writer(f)
    fWriter.writerow(['timestamp', 'message'])
    print('CSV Initialized')
    for message in consumer:
        msg = str(message.value.decode())
        print(msg)
        # divide by 1000 as it's in ms
        ts = datetime.datetime.fromtimestamp(message.timestamp/1000).strftime("%A, %B %d, %Y %I:%M:%S")
        print("Writing message %s..." % msg)
        fWriter.writerow([ts, msg])