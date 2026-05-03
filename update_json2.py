import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    # เครื่องบิน ภูเก็ต
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 690, "time": 90, "price": 1735.00}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 680, "time": 85, "price": 2000.00}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 1192, "time": 110, "price": 3516.00}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ระยอง", "transport": "เครื่องบิน", "weights": {"distance": 589, "time": 100, "price": 5375}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สุราษฎร์ธานี", "transport": "เครื่องบิน", "weights": {"distance": 150, "time": 55, "price": 3385}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สงขลา", "transport": "เครื่องบิน", "weights": {"distance": 460, "time": 60, "price": 2635}},
    
    # บขส ภูเก็ต
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "กทม", "transport": "บขส", "weights": {"distance": 846, "time": 699, "price": 715}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 1518, "time": 1206, "price": 3255}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 1620, "time": 1339, "price": 2646}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 620, "time": 777, "price": 966}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 385, "time": 348, "price": 390}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 1285, "time": 1260, "price": 1258}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 191, "time": 196, "price": 320}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 1430, "time": 1360, "price": 2885}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 299, "time": 302, "price": 320}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "นราธิวาส", "transport": "บขส", "weights": {"distance": 654, "time": 577, "price": 635}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 1448, "time": 1225, "price": 1415}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 122, "time": 100, "price": 100}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 1500, "time": 1435, "price": 2283}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 713, "time": 600, "price": 715}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 620, "time": 526, "price": 715}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ระนอง", "transport": "บขส", "weights": {"distance": 294, "time": 306, "price": 300}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ราชบุรี", "transport": "บขส", "weights": {"distance": 779, "time": 669, "price": 715}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 852, "time": 780, "price": 966}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สมุทรสงคราม", "transport": "บขส", "weights": {"distance": 805, "time": 615, "price": 715}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 274, "time": 450, "price": 396}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 234, "time": 232, "price": 421}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "ตรัง", "transport": "บขส", "weights": {"distance": 281, "time": 284, "price": 279}},
    {"zone": "ใต้", "source": "ภูเก็ต", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 1399, "time": 1176, "price": 1367}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
