import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "กทม", "transport": "บขส", "weights": {"distance": 859, "time": 716, "price": 594}}, # Using กทม for กรุงเทพมหานคร based on vertices list
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 611, "time": 630, "price": 1162}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 644, "time": 570, "price": 1002}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 951, "time": 1007, "price": 932}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "กาญจนบุรี", "transport": "บขส", "weights": {"distance": 678, "time": 660, "price": 684}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 702, "time": 660, "price": 796}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 631, "time": 490, "price": 594}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 887, "time": 658, "price": 895}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 672, "time": 480, "price": 594}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 800, "time": 720, "price": 1145}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 623, "time": 660, "price": 722}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 330, "time": 225, "price": 317}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 506, "time": 300, "price": 310}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 368, "time": 195, "price": 293}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "เลย", "transport": "บขส", "weights": {"distance": 500, "time": 540, "price": 656}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "แม่ฮ่องสอน", "transport": "บขส", "weights": {"distance": 273, "time": 351, "price": 420}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 978, "time": 930, "price": 1113}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 395, "time": 370, "price": 482}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 560, "time": 510, "price": 872}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 649, "time": 690, "price": 1240}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 272, "time": 310, "price": 373}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 451, "time": 360, "price": 586}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 348, "time": 380, "price": 405}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 201, "time": 230, "price": 334}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 1534, "time": 1320, "price": 3024}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 852, "time": 1034, "price": 1067}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 772, "time": 830, "price": 1145}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สิงห์บุรี", "transport": "บขส", "weights": {"distance": 559, "time": 420, "price": 821}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 298, "time": 290, "price": 439}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 854, "time": 834, "price": 952}},
    {"zone": "เหนือ", "source": "เชียงใหม่", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 276, "time": 240, "price": 374}},
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes for Chiang Mai.")
