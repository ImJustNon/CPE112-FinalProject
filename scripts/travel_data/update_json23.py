import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สงขลา", "transport": "เครื่องบิน", "weights": {"distance": 1325, "time": 125, "price": 4465}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 1187, "time": 130, "price": 2640}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สุราษฎร์ธานี", "transport": "เครื่องบิน", "weights": {"distance": 1072, "time": 110, "price": 4740}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "กระบี่", "transport": "เครื่องบิน", "weights": {"distance": 1186, "time": 120, "price": 4880}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ประจวบคีรีขันธ์", "transport": "เครื่องบิน", "weights": {"distance": 690, "time": 80, "price": 2155}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 568, "time": 70, "price": 2055}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 597, "time": 75, "price": 3095}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ขอนแก่น", "transport": "เครื่องบิน", "weights": {"distance": 479, "time": 65, "price": 3045}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} flight routes for Chiang Mai.")
