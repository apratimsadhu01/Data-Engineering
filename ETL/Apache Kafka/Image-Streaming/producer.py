from kafka import KafkaProducer
import os
from datetime import datetime
import time

now = datetime.now()

bootstrap_servers = ['localhost:9092']
topicName = 'Media'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

base_path = os.getcwd()
print(base_path)
os.mkdir("local_dir")
source = base_path+'/server/'
destination = base_path+'/local_dir/'

files = os.listdir(source)

time.sleep(15)

for file in files:
    os.rename(source + file, destination + file)
    current_time = now.strftime("%H:%M:%S")
    data = {"time":current_time,"file_path":destination + file}
    ack = producer.send(topicName, bytes(str(data).encode('utf-8')))
    print(ack.get())