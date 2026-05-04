import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 588, "time": 523, "price": 473}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 610, "time": 562, "price": 822}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 131, "time": 115, "price": 150}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 377, "time": 350, "price": 373}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 640, "time": 563, "price": 750}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 310, "time": 273, "price": 515}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 523, "time": 441, "price": 473}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 843, "time": 685, "price": 1235}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 460, "time": 384, "price": 473}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 1196, "time": 980, "price": 1569}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 1563, "time": 1237, "price": 2005}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 531, "time": 490, "price": 473}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 303, "time": 292, "price": 310}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 152, "time": 140, "price": 252}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 683, "time": 630, "price": 655}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 157, "time": 150, "price": 140}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 513, "time": 483, "price": 1162}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 581, "time": 540, "price": 699}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "เลย", "transport": "บขส", "weights": {"distance": 215, "time": 215, "price": 378}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 266, "time": 247, "price": 240}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 213, "time": 200, "price": 269}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 1333, "time": 1041, "price": 2122}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "พัทลุง", "transport": "บขส", "weights": {"distance": 1414, "time": 1103, "price": 1809}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 589, "time": 545, "price": 581}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 354, "time": 336, "price": 378}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 421, "time": 402, "price": 605}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 161, "time": 143, "price": 80}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 375, "time": 365, "price": 464}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 451, "time": 65, "price": 1530}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "อุดรธานี", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 466, "time": 70, "price": 2615}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes (bus & flight) for Udon Thani.")
