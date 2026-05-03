import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Bangkok (กทม) - Transport: บขส
# Region for Bangkok is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "กทม", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 861, "time": 701, "price": 594}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 761, "time": 585, "price": 473}},
    {"zone": "กลาง", "source": "กทม", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 765, "time": 593, "price": 380}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 345, "time": 284, "price": 232}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 725, "time": 587, "price": 504}},
    {"zone": "กลาง", "source": "กทม", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 97.5, "time": 78, "price": 156}},
    {"zone": "กลาง", "source": "กทม", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 154, "time": 117, "price": 95}},
    {"zone": "กลาง", "source": "กทม", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 34.8, "time": 40, "price": 200}},
    {"zone": "กลาง", "source": "กทม", "destination": "กาญจนบุรี", "transport": "บขส", "weights": {"distance": 186, "time": 155, "price": 110}},
    {"zone": "กลาง", "source": "กทม", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 98.1, "time": 88, "price": 88}},
    {"zone": "กลาง", "source": "กทม", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 45.4, "time": 42, "price": 80}},
    {"zone": "กลาง", "source": "กทม", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 200, "time": 159, "price": 151}},
    {"zone": "กลาง", "source": "กทม", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 38.9, "time": 55, "price": 118}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครปฐม", "transport": "บขส", "weights": {"distance": 56.8, "time": 52, "price": 90}},
    {"zone": "กลาง", "source": "กทม", "destination": "ฉะเชิงเทรา", "transport": "บขส", "weights": {"distance": 150, "time": 138, "price": 130}},
    {"zone": "กลาง", "source": "กทม", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 171, "time": 144, "price": 169}},
    {"zone": "กลาง", "source": "กทม", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 679, "time": 517, "price": 218}},
    {"zone": "กลาง", "source": "กทม", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 823, "time": 723, "price": 558}},
    {"zone": "กลาง", "source": "กทม", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 804, "time": 650, "price": 650}},
    {"zone": "กลาง", "source": "กทม", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 860, "time": 672, "price": 715}},
    {"zone": "กลาง", "source": "กทม", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 988, "time": 772, "price": 749}},
    {"zone": "กลาง", "source": "กทม", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 624, "time": 523, "price": 486}},
    {"zone": "กลาง", "source": "กทม", "destination": "อ่างทอง", "transport": "บขส", "weights": {"distance": 118, "time": 108, "price": 128}},
    {"zone": "กลาง", "source": "กทม", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 729, "time": 623, "price": 565}},
    {"zone": "กลาง", "source": "กทม", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 447, "time": 352, "price": 333}},
    {"zone": "กลาง", "source": "กทม", "destination": "ชัยนาท", "transport": "บขส", "weights": {"distance": 193, "time": 178, "price": 200}},
    {"zone": "กลาง", "source": "กทม", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 405, "time": 336, "price": 265}},
    {"zone": "กลาง", "source": "กทม", "destination": "จันทบุรี", "transport": "บขส", "weights": {"distance": 250, "time": 205, "price": 218}},
    {"zone": "กลาง", "source": "กทม", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 838, "time": 699, "price": 650}},
    {"zone": "กลาง", "source": "กทม", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 548, "time": 416, "price": 400}},
    {"zone": "กลาง", "source": "กทม", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 568, "time": 457, "price": 508}},
    {"zone": "กลาง", "source": "กทม", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 501, "time": 423, "price": 313}},
    
    {"zone": "กลาง", "source": "กทม", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 639, "time": 491, "price": 432}},
    {"zone": "กลาง", "source": "กทม", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 652, "time": 512, "price": 594}},
    {"zone": "กลาง", "source": "กทม", "destination": "เลย", "transport": "บขส", "weights": {"distance": 600, "time": 517, "price": 550}},
    {"zone": "กลาง", "source": "กทม", "destination": "ลพบุรี", "transport": "บขส", "weights": {"distance": 180, "time": 148, "price": 156}},
    {"zone": "กลาง", "source": "กทม", "destination": "แม่ฮ่องสอน", "transport": "บขส", "weights": {"distance": 801, "time": 739, "price": 758}},
    {"zone": "กลาง", "source": "กทม", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 532, "time": 435, "price": 349}},
    {"zone": "กลาง", "source": "กทม", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 659, "time": 529, "price": 535}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครนายก", "transport": "บขส", "weights": {"distance": 98.6, "time": 91, "price": 120}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 731, "time": 616, "price": 576}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 226, "time": 181, "price": 360}},
    {"zone": "กลาง", "source": "กทม", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 884, "time": 682, "price": 617}},
    {"zone": "กลาง", "source": "กทม", "destination": "น่าน", "transport": "บขส", "weights": {"distance": 744, "time": 612, "price": 547}},
    {"zone": "กลาง", "source": "กทม", "destination": "นราธิวาส", "transport": "บขส", "weights": {"distance": 1186, "time": 930, "price": 1184}},
    {"zone": "กลาง", "source": "กทม", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 637, "time": 536, "price": 527}},
    {"zone": "กลาง", "source": "กทม", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 711, "time": 600, "price": 515}},
    {"zone": "กลาง", "source": "กทม", "destination": "ปัตตานี", "transport": "บขส", "weights": {"distance": 1086, "time": 874, "price": 1085}},
    {"zone": "กลาง", "source": "กทม", "destination": "พัทลุง", "transport": "บขส", "weights": {"distance": 890, "time": 679, "price": 706}},
    {"zone": "กลาง", "source": "กทม", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 766, "time": 620, "price": 576}},
    {"zone": "กลาง", "source": "กทม", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 410, "time": 341, "price": 380}},
    {"zone": "กลาง", "source": "กทม", "destination": "พิจิตร", "transport": "บขส", "weights": {"distance": 328, "time": 257, "price": 257}},
    {"zone": "กลาง", "source": "กทม", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 412, "time": 321, "price": 320}},
    {"zone": "กลาง", "source": "กทม", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 635, "time": 491, "price": 468}},
    {"zone": "กลาง", "source": "กทม", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 875, "time": 715, "price": 715}},
    {"zone": "กลาง", "source": "กทม", "destination": "ปราจีนบุรี", "transport": "บขส", "weights": {"distance": 274, "time": 252, "price": 140}},
    {"zone": "กลาง", "source": "กทม", "destination": "ระนอง", "transport": "บขส", "weights": {"distance": 619, "time": 483, "price": 491}},
    {"zone": "กลาง", "source": "กทม", "destination": "ราชบุรี", "transport": "บขส", "weights": {"distance": 101, "time": 87, "price": 120}},
    {"zone": "กลาง", "source": "กทม", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 542, "time": 437, "price": 380}},
    {"zone": "กลาง", "source": "กทม", "destination": "สระแก้ว", "transport": "บขส", "weights": {"distance": 258, "time": 217, "price": 220}},
    {"zone": "กลาง", "source": "กทม", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 785, "time": 686, "price": 558}},
    {"zone": "กลาง", "source": "กทม", "destination": "สตูล", "transport": "บขส", "weights": {"distance": 966, "time": 789, "price": 787}},
    {"zone": "กลาง", "source": "กทม", "destination": "สิงห์บุรี", "transport": "บขส", "weights": {"distance": 150, "time": 138, "price": 135}},
    {"zone": "กลาง", "source": "กทม", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 534, "time": 437, "price": 418}},
    {"zone": "กลาง", "source": "กทม", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 476, "time": 369, "price": 376}},
    {"zone": "กลาง", "source": "กทม", "destination": "สุพรรณบุรี", "transport": "บขส", "weights": {"distance": 120, "time": 100, "price": 100}},
    {"zone": "กลาง", "source": "กทม", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 494, "time": 404, "price": 367}},
    {"zone": "กลาง", "source": "กทม", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 485, "time": 378, "price": 362}},
    
    {"zone": "กลาง", "source": "กทม", "destination": "ตรัง", "transport": "บขส", "weights": {"distance": 863, "time": 692, "price": 711}},
    {"zone": "กลาง", "source": "กทม", "destination": "ตราด", "transport": "บขส", "weights": {"distance": 346, "time": 283, "price": 279}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุทัยธานี", "transport": "บขส", "weights": {"distance": 243, "time": 224, "price": 317}},
    {"zone": "กลาง", "source": "กทม", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 485, "time": 363, "price": 229}},
    {"zone": "กลาง", "source": "กทม", "destination": "ยะลา", "transport": "บขส", "weights": {"distance": 1188, "time": 962, "price": 1298}},
    {"zone": "กลาง", "source": "กทม", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 703, "time": 568, "price": 443}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
