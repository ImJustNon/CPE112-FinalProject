import json

provinces = [
    "กทม", "กระบี่", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร", "ขอนแก่น", 
    "จันทบุรี", "ฉะเชิงเทรา", "ชลบุรี", "ชัยนาท", "ชัยภูมิ", "ชุมพร", 
    "เชียงราย", "เชียงใหม่", "ตรัง", "ตราด", "ตาก", "นครนายก", 
    "นครปฐม", "นครพนม", "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์", "นนทบุรี", 
    "นราธิวาส", "น่าน", "บึงกาฬ", "บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์", 
    "ปราจีนบุรี", "ปัตตานี", "พระนครศรีอยุธยา", "พะเยา", "พังงา", "พัทลุง", 
    "พิจิตร", "พิษณุโลก", "เพชรบุรี", "เพชรบูรณ์", "แพร่", "ภูเก็ต", 
    "มหาสารคาม", "มุกดาหาร", "แม่ฮ่องสอน", "ยโสธร", "ยะลา", "ร้อยเอ็ด", 
    "ระนอง", "ระยอง", "ราชบุรี", "ลพบุรี", "ลำปาง", "ลำพูน", 
    "เลย", "ศรีสะเกษ", "สกลนคร", "สงขลา", "สตูล", "สมุทรปราการ", 
    "สมุทรสงคราม", "สมุทรสาคร", "สระแก้ว", "สระบุรี", "สิงห์บุรี", "สุโขทัย", 
    "สุพรรณบุรี", "สุราษฎร์ธานี", "สุรินทร์", "หนองคาย", "หนองบัวลำภู", "อ่างทอง", 
    "อำนาจเจริญ", "อุดรธานี", "อุตรดิตถ์", "อุทัยธานี", "อุบลราชธานี"
]

edges = [
    # เครื่องบิน (Airplane)
    {"zone": "ใต้", "source": "กระบี่", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 670, "time": 90, "price": 1626.80}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 650, "time": 85, "price": 1734.60}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 1360, "time": 120, "price": 3324.47}},
    
    # บขส (Bus)
    {"zone": "ใต้", "source": "กระบี่", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 168, "time": 180, "price": 345}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 742, "time": 660, "price": 675}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 303, "time": 270, "price": 450}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "สตูล", "transport": "บขส", "weights": {"distance": 266, "time": 240, "price": 1090}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "กทม", "transport": "บขส", "weights": {"distance": 801, "time": 631, "price": 715}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 889, "time": 720, "price": 996}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 327, "time": 300, "price": 844}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 1057, "time": 810, "price": 1518}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 153, "time": 190, "price": 320}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 120, "time": 90, "price": 400}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 650, "time": 500, "price": 844}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 163, "time": 180, "price": 320}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 495, "time": 480, "price": 844}},
    {"zone": "ใต้", "source": "กระบี่", "destination": "ราชบุรี", "transport": "บขส", "weights": {"distance": 714, "time": 588, "price": 844}}
]

data = {
    "vertices": provinces,
    "edges": edges
}

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
