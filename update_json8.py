import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Saraburi (สระบุรี) - Transport: บขส
# Region for Saraburi is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "สระบุรี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 116, "time": 94, "price": 156}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 460, "time": 383, "price": 473}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 342, "time": 282, "price": 433}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 150, "time": 118, "price": 420}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 496, "time": 399, "price": 524}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 42.2, "time": 35, "price": 156}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 80.6, "time": 74, "price": 156}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 131, "time": 103, "price": 420}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 274, "time": 253, "price": 824}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 499, "time": 460, "price": 432}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 656, "time": 605, "price": 650}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 283, "time": 226, "price": 420}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ชัยนาท", "transport": "บขส", "weights": {"distance": 133, "time": 123, "price": 150}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 257, "time": 237, "price": 433}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 563, "time": 445, "price": 824}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 411, "time": 330, "price": 550}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "เลย", "transport": "บขส", "weights": {"distance": 430, "time": 397, "price": 550}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ลพบุรี", "transport": "บขส", "weights": {"distance": 64.6, "time": 60, "price": 156}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 366, "time": 338, "price": 420}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 551, "time": 509, "price": 558}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 637, "time": 588, "price": 576}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 885, "time": 817, "price": 824}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 600, "time": 554, "price": 260}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 413, "time": 361, "price": 550}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 514, "time": 429, "price": 515}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 485, "time": 413, "price": 260}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ปราจีนบุรี", "transport": "บขส", "weights": {"distance": 111, "time": 102, "price": 150}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 401, "time": 370, "price": 420}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 541, "time": 499, "price": 589}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 437, "time": 351, "price": 418}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 323, "time": 262, "price": 454}},
    {"zone": "กลาง", "source": "สระบุรี", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 426, "time": 393, "price": 460}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
