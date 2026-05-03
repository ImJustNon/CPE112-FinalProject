import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Phetchaburi (เพชรบุรี)
# Region: "ตะวันตก" (West)
new_edges = [
    # Transport: บขส (Bus)
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 153, "time": 142, "price": 400}},
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 733, "time": 810, "price": 763}}, # 13 ชม 30 นาที -> 810
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 171, "time": 165, "price": 169}}, # 2 ชม 45 นาที -> 165
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 322, "time": 243, "price": 467}}, # 4 ชม 03 นาที -> 243
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 645, "time": 825, "price": 800}}, # 13 ชม 45 นาที -> 825
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 750, "time": 875, "price": 800}}, # 14 ชม 35 นาที -> 875
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 634, "time": 770, "price": 763}}, # 12 ชม 50 นาที -> 770
    {"zone": "ตะวันตก", "source": "เพชรบุรี", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 721, "time": 850, "price": 800}}  # 14 ชม 10 นาที -> 850
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
