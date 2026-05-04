import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Chachoengsao (ฉะเชิงเทรา)
# Region: "ตะวันออก" (East)
new_edges = [
    # Transport: บขส (Bus)
    {"zone": "ตะวันออก", "source": "ฉะเชิงเทรา", "destination": "กทม", "transport": "บขส", "weights": {"distance": 150, "time": 90, "price": 170}}, # 1 ชม 30 นาที
    {"zone": "ตะวันออก", "source": "ฉะเชิงเทรา", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 162, "time": 150, "price": 190}}, # 2 ชม 30 นาที
    {"zone": "ตะวันออก", "source": "ฉะเชิงเทรา", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 76.8, "time": 60, "price": 170}}, # 1 ชม
    {"zone": "ตะวันออก", "source": "ฉะเชิงเทรา", "destination": "สระแก้ว", "transport": "บขส", "weights": {"distance": 109, "time": 210, "price": 126}}, # 3 ชม 30 นาที
    {"zone": "ตะวันออก", "source": "ฉะเชิงเทรา", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 450, "time": 420, "price": 427}} # 7 ชม
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
