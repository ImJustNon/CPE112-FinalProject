import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 843, "time": 623, "price": 1194}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 629, "time": 566, "price": 800}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 517, "time": 477, "price": 700}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 324, "time": 305, "price": 565}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 628, "time": 691, "price": 914}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 266, "time": 196, "price": 350}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 68.9, "time": 65, "price": 70}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 166, "time": 153, "price": 165}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "กาญจนบุรี", "transport": "บขส", "weights": {"distance": 313, "time": 256, "price": 310}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 205, "time": 164, "price": 615}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "กทม", "transport": "บขส", "weights": {"distance": 189, "time": 150, "price": 210}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 451, "time": 356, "price": 745}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 802, "time": 657, "price": 825}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 1128, "time": 914, "price": 1590}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 818, "time": 744, "price": 890}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 437, "time": 383, "price": 664}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 110, "time": 130, "price": 158}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 950, "time": 733, "price": 1195}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 621, "time": 432, "price": 745}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 586, "time": 524, "price": 815}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 515, "time": 372, "price": 571}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 541, "time": 422, "price": 750}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 814, "time": 751, "price": 890}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 402, "time": 292, "price": 758}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 904, "time": 747, "price": 1285}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 829, "time": 626, "price": 1061}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 678, "time": 626, "price": 750}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "พัทลุง", "transport": "บขส", "weights": {"distance": 1017, "time": 816, "price": 1394}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "พิจิตร", "transport": "บขส", "weights": {"distance": 484, "time": 447, "price": 557}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 546, "time": 393, "price": 557}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 734, "time": 678, "price": 912}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 716, "time": 653, "price": 840}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 576, "time": 496, "price": 838}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 463, "time": 412, "price": 723}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 656, "time": 495, "price": 628}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 185, "time": 168, "price": 250}},
    {"zone": "ตะวันออก", "source": "ระยอง", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 647, "time": 470, "price": 808}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes for Rayong.")
