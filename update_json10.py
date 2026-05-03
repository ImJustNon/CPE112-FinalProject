import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Pathum Thani (ปทุมธานี) - Transport: บขส
# Region for Pathum Thani is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "กทม", "transport": "บขส", "weights": {"distance": 40.8, "time": 38, "price": 156}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 565, "time": 496, "price": 473}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 419, "time": 387, "price": 433}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 323, "time": 255, "price": 227}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 650, "time": 548, "price": 524}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 654, "time": 489, "price": 693}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 138, "time": 110, "price": 160}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 63, "time": 57, "price": 80}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 80.2, "time": 74, "price": 156}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 53.3, "time": 49, "price": 88}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 77.6, "time": 71, "price": 80}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 196, "time": 181, "price": 269}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 588, "time": 491, "price": 486}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "อ่างทอง", "transport": "บขส", "weights": {"distance": 97.7, "time": 90, "price": 128}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 735, "time": 678, "price": 565}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 359, "time": 287, "price": 333}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ชัยนาท", "transport": "บขส", "weights": {"distance": 171, "time": 158, "price": 571}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 336, "time": 310, "price": 261}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 263, "time": 243, "price": 363}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 824, "time": 671, "price": 758}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 490, "time": 452, "price": 508}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 333, "time": 307, "price": 313}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 579, "time": 534, "price": 522}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 583, "time": 538, "price": 594}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "เลย", "transport": "บขส", "weights": {"distance": 512, "time": 473, "price": 550}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ลพบุรี", "transport": "บขส", "weights": {"distance": 147, "time": 136, "price": 156}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 378, "time": 301, "price": 420}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 629, "time": 581, "price": 558}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 716, "time": 661, "price": 576}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 274, "time": 253, "price": 216}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 640, "time": 495, "price": 661}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 522, "time": 441, "price": 527}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 624, "time": 554, "price": 515}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 693, "time": 545, "price": 691}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 323, "time": 298, "price": 380}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "พิจิตร", "transport": "บขส", "weights": {"distance": 298, "time": 275, "price": 333}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 356, "time": 329, "price": 320}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 525, "time": 397, "price": 468}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ปราจีนบุรี", "transport": "บขส", "weights": {"distance": 124, "time": 114, "price": 558}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 432, "time": 356, "price": 420}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 620, "time": 572, "price": 558}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สิงห์บุรี", "transport": "บขส", "weights": {"distance": 129, "time": 119, "price": 135}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 500, "time": 462, "price": 418}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 405, "time": 374, "price": 376}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 448, "time": 414, "price": 367}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 411, "time": 379, "price": 362}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 338, "time": 312, "price": 435}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 501, "time": 462, "price": 473}},
    {"zone": "กลาง", "source": "ปทุมธานี", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 520, "time": 427, "price": 460}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
