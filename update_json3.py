import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    # บขส พังงา
    {"zone": "ใต้", "source": "พังงา", "destination": "กทม", "transport": "บขส", "weights": {"distance": 766, "time": 636, "price": 866}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 869, "time": 910, "price": 966}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 316, "time": 243, "price": 370}},
    {"zone": "ใต้", "source": "พังงา", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 630, "time": 540, "price": 693}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 120, "time": 72, "price": 100}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 475, "time": 420, "price": 693}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ระนอง", "transport": "บขส", "weights": {"distance": 194, "time": 185, "price": 125}},
    {"zone": "ใต้", "source": "พังงา", "destination": "ราชบุรี", "transport": "บขส", "weights": {"distance": 705, "time": 592, "price": 899}},
    {"zone": "ใต้", "source": "พังงา", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 769, "time": 630, "price": 966}},
    {"zone": "ใต้", "source": "พังงา", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 722, "time": 540, "price": 693}},
    {"zone": "ใต้", "source": "พังงา", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 161, "time": 159, "price": 150}},
    {"zone": "ใต้", "source": "พังงา", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 120, "time": 130, "price": 357}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
