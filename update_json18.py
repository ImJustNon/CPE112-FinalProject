import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Chonburi (ชลบุรี)
# Region: "ตะวันออก" (East)
new_edges = [
    # Transport: บขส (Bus)
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 565, "time": 666, "price": 790}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 452, "time": 420, "price": 650}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 274, "time": 250, "price": 450}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 110, "time": 120, "price": 153}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "กาญจนบุรี", "transport": "บขส", "weights": {"distance": 249, "time": 186, "price": 310}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 182, "time": 141, "price": 500}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 66.5, "time": 70, "price": 140}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 139, "time": 109, "price": 160}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 396, "time": 360, "price": 628}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 730, "time": 680, "price": 755}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 860, "time": 800, "price": 966}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 1030, "time": 960, "price": 1501}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 85, "time": 120, "price": 95}}, # กรุงเทพมหานคร -> กทม
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 755, "time": 684, "price": 840}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 153, "time": 139, "price": 218}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 564, "time": 520, "price": 685}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 523, "time": 464, "price": 739}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 459, "time": 324, "price": 454}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 477, "time": 416, "price": 739}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 749, "time": 652, "price": 840}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 345, "time": 245, "price": 342}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 562, "time": 520, "price": 750}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "พิจิตร", "transport": "บขส", "weights": {"distance": 426, "time": 390, "price": 441}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 489, "time": 346, "price": 441}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 920, "time": 850, "price": 966}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 653, "time": 593, "price": 750}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 600, "time": 448, "price": 510}},
    {"zone": "ตะวันออก", "source": "ชลบุรี", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 204, "time": 190, "price": 279}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
