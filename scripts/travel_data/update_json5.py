import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    # เครื่องบิน สุราษฎร์ธานี
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 552, "time": 75, "price": 1510.00}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 533, "time": 75, "price": 2050.00}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 1066, "time": 110, "price": 2910.00}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 144, "time": 60, "price": 4810.00}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ระยอง", "transport": "เครื่องบิน", "weights": {"distance": 440, "time": 70, "price": 5900.00}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "กระบี่", "transport": "เครื่องบิน", "weights": {"distance": 100, "time": 50, "price": 4735.00}},
    
    # บขส สุราษฎร์ธานี
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 718, "time": 545, "price": 558}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 746, "time": 710, "price": 947}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 180, "time": 165, "price": 450}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 1092, "time": 883, "price": 1400}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 274, "time": 180, "price": 375}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 867, "time": 905, "price": 1379}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 139, "time": 270, "price": 310}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 1254, "time": 1030, "price": 1610}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "นนทบุรี", "transport": "บขส", "weights": {"distance": 653, "time": 465, "price": 643}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 161, "time": 161, "price": 150}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 509, "time": 375, "price": 717}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 1008, "time": 1045, "price": 1559}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 241, "time": 270, "price": 408}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 354, "time": 289, "price": 684}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 647, "time": 570, "price": 630}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 324, "time": 390, "price": 533}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ตรัง", "transport": "บขส", "weights": {"distance": 211, "time": 180, "price": 385}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 1205, "time": 1130, "price": 1332}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "ยะลา", "transport": "บขส", "weights": {"distance": 350, "time": 450, "price": 590}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "นราธิวาส", "transport": "บขส", "weights": {"distance": 500, "time": 510, "price": 690}},
    {"zone": "ใต้", "source": "สุราษฎร์ธานี", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 609, "time": 600, "price": 684}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
