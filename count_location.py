import json
import matplotlib.pyplot as plt

with open('data.json','r') as f:
    data = json.load(f)

labels = []
for entry in data:
    tags = entry.get('data_name',[])