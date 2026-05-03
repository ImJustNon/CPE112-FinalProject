import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Bangkok (กทม) - Transport: เครื่องบิน
# Region for Bangkok is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "กทม", "destination": "นราธิวาส", "transport": "เครื่องบิน", "weights": {"distance": 831, "time": 90, "price": 2710}},
    {"zone": "กลาง", "source": "กทม", "destination": "สงขลา", "transport": "เครื่องบิน", "weights": {"distance": 776, "time": 85, "price": 1640}},
    {"zone": "กลาง", "source": "กทม", "destination": "ตรัง", "transport": "เครื่องบิน", "weights": {"distance": 720, "time": 85, "price": 1850}},
    {"zone": "กลาง", "source": "กทม", "destination": "กระบี่", "transport": "เครื่องบิน", "weights": {"distance": 670, "time": 85, "price": 1400}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครศรีธรรมราช", "transport": "เครื่องบิน", "weights": {"distance": 602, "time": 80, "price": 1690}},
    {"zone": "กลาง", "source": "กทม", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 692, "time": 85, "price": 1630}},
    {"zone": "กลาง", "source": "กทม", "destination": "สุราษฎร์ธานี", "transport": "เครื่องบิน", "weights": {"distance": 555, "time": 70, "price": 1545}},
    {"zone": "กลาง", "source": "กทม", "destination": "ระนอง", "transport": "เครื่องบิน", "weights": {"distance": 510, "time": 80, "price": 1960}},
    {"zone": "กลาง", "source": "กทม", "destination": "ชุมพร", "transport": "เครื่องบิน", "weights": {"distance": 381, "time": 65, "price": 1595}},
    {"zone": "กลาง", "source": "กทม", "destination": "บุรีรัมย์", "transport": "เครื่องบิน", "weights": {"distance": 320, "time": 60, "price": 2170}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุบลราชธานี", "transport": "เครื่องบิน", "weights": {"distance": 482, "time": 60, "price": 1535}},
    {"zone": "กลาง", "source": "กทม", "destination": "ร้อยเอ็ด", "transport": "เครื่องบิน", "weights": {"distance": 424, "time": 65, "price": 1990}},
    {"zone": "กลาง", "source": "กทม", "destination": "ขอนแก่น", "transport": "เครื่องบิน", "weights": {"distance": 368, "time": 65, "price": 1380}},
    {"zone": "กลาง", "source": "กทม", "destination": "สกลนคร", "transport": "เครื่องบิน", "weights": {"distance": 524, "time": 75, "price": 1545}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครพนม", "transport": "เครื่องบิน", "weights": {"distance": 579, "time": 80, "price": 1440}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุดรธานี", "transport": "เครื่องบิน", "weights": {"distance": 451, "time": 70, "price": 1400}},
    {"zone": "กลาง", "source": "กทม", "destination": "เลย", "transport": "เครื่องบิน", "weights": {"distance": 410, "time": 70, "price": 1895}},
    {"zone": "กลาง", "source": "กทม", "destination": "พิษณุโลก", "transport": "เครื่องบิน", "weights": {"distance": 320, "time": 65, "price": 1230}},
    {"zone": "กลาง", "source": "กทม", "destination": "ลำปาง", "transport": "เครื่องบิน", "weights": {"distance": 499, "time": 70, "price": 2005}},
    {"zone": "กลาง", "source": "กทม", "destination": "น่าน", "transport": "เครื่องบิน", "weights": {"distance": 545, "time": 75, "price": 1455}},
    {"zone": "กลาง", "source": "กทม", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 568, "time": 75, "price": 1595}},
    {"zone": "กลาง", "source": "กทม", "destination": "เชียงราย", "transport": "เครื่องบิน", "weights": {"distance": 676, "time": 85, "price": 1645}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
