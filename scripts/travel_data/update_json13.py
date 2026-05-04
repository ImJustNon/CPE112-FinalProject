import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Samut Prakan (สมุทรปราการ)
# Region for Samut Prakan is "กลาง" (Central)
new_edges = [
    # Transport: บขส (Bus)
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 279, "time": 218, "price": 420}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 589, "time": 540, "price": 420}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 131, "time": 103, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 109, "time": 93, "price": 153}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 104, "time": 85, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 164, "time": 150, "price": 151}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 61.2, "time": 53, "price": 517}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 293, "time": 243, "price": 423}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 645, "time": 600, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 765, "time": 710, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "กทม", "transport": "บขส", "weights": {"distance": 30.5, "time": 30, "price": 50}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 233, "time": 215, "price": 218}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 461, "time": 425, "price": 588}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 845, "time": 780, "price": 966}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 308, "time": 285, "price": 279}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 605, "time": 560, "price": 420}},

    # Transport: เครื่องบิน (Airplane)
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สงขลา", "transport": "เครื่องบิน", "weights": {"distance": 751, "time": 90, "price": 1765}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "กระบี่", "transport": "เครื่องบิน", "weights": {"distance": 650, "time": 85, "price": 1635}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "นครศรีธรรมราช", "transport": "เครื่องบิน", "weights": {"distance": 578, "time": 70, "price": 1940}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 674, "time": 95, "price": 1715}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "สุราษฎร์ธานี", "transport": "เครื่องบิน", "weights": {"distance": 535, "time": 75, "price": 1440}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "อุบลราชธานี", "transport": "เครื่องบิน", "weights": {"distance": 477, "time": 75, "price": 1515}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ขอนแก่น", "transport": "เครื่องบิน", "weights": {"distance": 379, "time": 65, "price": 1365}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "อุดรธานี", "transport": "เครื่องบิน", "weights": {"distance": 466, "time": 75, "price": 1665}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 597, "time": 85, "price": 1500}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "เชียงราย", "transport": "เครื่องบิน", "weights": {"distance": 703, "time": 85, "price": 1760}},
    {"zone": "กลาง", "source": "สมุทรปราการ", "destination": "ตราด", "transport": "เครื่องบิน", "weights": {"distance": 231, "time": 60, "price": 1720}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
