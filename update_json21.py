import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 711, "time": 80, "price": 2390}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สุราษฎร์ธานี", "transport": "เครื่องบิน", "weights": {"distance": 444, "time": 65, "price": 3240}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 587, "time": 100, "price": 3500}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} flight routes for Rayong.")
