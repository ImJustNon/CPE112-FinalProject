import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The user has uploaded a corrected version of the Samut Prakan (สมุทรปราการ) Bus (บขส) routes.
# We will first remove the old ones, then add the new corrected list (15 routes).
data['edges'] = [
    e for e in data['edges'] 
    if not (e['source'] == 'สมุทรปราการ' and e['transport'] == 'บขส')
]

new_edges = [
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 279, "time": 218, "price": 420}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 589, "time": 540, "price": 420}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 131, "time": 103, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 109, "time": 93, "price": 153}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 104, "time": 85, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 164, "time": 150, "price": 151}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 61.2, "time": 53, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 293, "time": 243, "price": 423}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 645, "time": 600, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 765, "time": 720, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 233, "time": 210, "price": 218}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 461, "time": 430, "price": 588}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 845, "time": 800, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 308, "time": 290, "price": 279}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 605, "time": 560, "price": 420}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Re-added updated data. Found {len(new_edges)} routes.")
