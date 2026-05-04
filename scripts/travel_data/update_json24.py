import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "อ่างทอง", "transport": "บขส", "weights": {"distance": 268.7, "time": 180, "price": 436}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 311, "time": 247, "price": 436}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "กทม", "transport": "บขส", "weights": {"distance": 383, "time": 300, "price": 360}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 528, "time": 480, "price": 743}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 298, "time": 270, "price": 374}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 348, "time": 360, "price": 344}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 408, "time": 540, "price": 491}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 467, "time": 495, "price": 701}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 316, "time": 280, "price": 374}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 247, "time": 250, "price": 360}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 272, "time": 330, "price": 362}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "เลย", "transport": "บขส", "weights": {"distance": 230, "time": 205, "price": 305}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 540, "time": 461, "price": 701}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 590, "time": 535, "price": 714}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 136, "time": 110, "price": 436}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 290, "time": 230, "price": 328}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 277, "time": 240, "price": 470}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 321, "time": 300, "price": 491}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 160, "time": 106, "price": 374}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 195, "time": 150, "price": 328}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 476, "time": 480, "price": 567}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 530, "time": 510, "price": 743}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 60, "time": 90, "price": 337}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 240, "time": 140, "price": 191}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 900, "time": 660, "price": 762}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 400, "time": 360, "price": 470}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 510, "time": 480, "price": 647}},
    {"zone": "เหนือ", "source": "พิษณุโลก", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 320, "time": 60, "price": 1115}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes (bus & flight) for Phitsanulok.")
