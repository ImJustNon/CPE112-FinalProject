import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "กทม", "transport": "บขส", "weights": {"distance": 261, "time": 206, "price": 220}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 701, "time": 650, "price": 796}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 328, "time": 300, "price": 590}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 193, "time": 169, "price": 154}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 380, "time": 350, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 335, "time": 300, "price": 392}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 305, "time": 274, "price": 362}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 213, "time": 177, "price": 275}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 151, "time": 120, "price": 275}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 301, "time": 280, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 429, "time": 337, "price": 372}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 452, "time": 357, "price": 527}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 1036, "time": 788, "price": 1518}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 232, "time": 210, "price": 275}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 351, "time": 305, "price": 283}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 494, "time": 450, "price": 650}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 128, "time": 121, "price": 150}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 773, "time": 710, "price": 929}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 262, "time": 230, "price": 400}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 598, "time": 550, "price": 695}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ลพบุรี", "transport": "บขส", "weights": {"distance": 159, "time": 150, "price": 416}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 221, "time": 200, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 402, "time": 370, "price": 412}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 492, "time": 450, "price": 473}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 290, "time": 270, "price": 416}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 301, "time": 281, "price": 550}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 377, "time": 350, "price": 407}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 550, "time": 510, "price": 623}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ปราจีนบุรี", "transport": "บขส", "weights": {"distance": 180, "time": 170, "price": 355}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 256, "time": 240, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 396, "time": 370, "price": 650}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 302, "time": 261, "price": 250}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 1210, "time": 1110, "price": 1554}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สุพรรณบุรี", "transport": "บขส", "weights": {"distance": 269, "time": 230, "price": 332}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 220, "time": 201, "price": 169}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "นครราชสีมา", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 277, "time": 260, "price": 297}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes for Nakhon Ratchasima.")
