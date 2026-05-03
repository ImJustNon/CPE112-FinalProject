import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Kanchanaburi (กาญจนบุรี)
# Region: "ตะวันตก" (West)
new_edges = [
    # Transport: บขส (Bus)
    {"zone": "ตะวันตก", "source": "กาญจนบุรี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 133, "time": 120, "price": 240}},
    {"zone": "ตะวันตก", "source": "กาญจนบุรี", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 684, "time": 710, "price": 778}},
    {"zone": "ตะวันตก", "source": "กาญจนบุรี", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 713, "time": 720, "price": 666}},
    {"zone": "ตะวันตก", "source": "กาญจนบุรี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 683, "time": 600, "price": 860}},
    {"zone": "ตะวันตก", "source": "กาญจนบุรี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 350, "time": 420, "price": 600}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
