import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 725, "time": 584, "price": 504}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 936, "time": 798, "price": 1253}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 375, "time": 350, "price": 373}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 362, "time": 319, "price": 294}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 618, "time": 525, "price": 914}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 370, "time": 310, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 558, "time": 449, "price": 611}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 495, "time": 392, "price": 544}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 647, "time": 600, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 569, "time": 448, "price": 524}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 94.7, "time": 92, "price": 77}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 228, "time": 208, "price": 500}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 400, "time": 370, "price": 504}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 997, "time": 920, "price": 1329}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 827, "time": 706, "price": 838}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 896, "time": 762, "price": 932}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 211, "time": 190, "price": 227}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 165, "time": 146, "price": 157}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 292, "time": 270, "price": 240}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 940, "time": 870, "price": 1212}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 478, "time": 423, "price": 487}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 597, "time": 518, "price": 611}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 736, "time": 625, "price": 748}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 157, "time": 140, "price": 420}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 332, "time": 294, "price": 247}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 87.4, "time": 85, "price": 544}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 171, "time": 169, "price": 544}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 690, "time": 587, "price": 699}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 101, "time": 86, "price": 588}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 482, "time": 65, "price": 1355}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุบลราชธานี", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 477, "time": 75, "price": 1460}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes (bus & flight) for Ubon Ratchathani.")
