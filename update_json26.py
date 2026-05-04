import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "กทม", "transport": "บขส", "weights": {"distance": 755, "time": 598, "price": 380}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 801, "time": 540, "price": 645}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 113, "time": 99, "price": 200}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 374, "time": 321, "price": 294}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 526, "time": 850, "price": 700}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 193, "time": 170, "price": 154}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "พระนครศรีอยุธยา", "transport": "บขส", "weights": {"distance": 406, "time": 338, "price": 295}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 730, "time": 587, "price": 1092}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 343, "time": 281, "price": 295}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 1083, "time": 1050, "price": 1940}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "สงขลา", "transport": "บขส", "weights": {"distance": 1434, "time": 1122, "price": 1859}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 452, "time": 615, "price": 650}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ปทุมธานี", "transport": "บขส", "weights": {"distance": 417, "time": 390, "price": 500}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 717, "time": 745, "price": 775}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 154, "time": 120, "price": 374}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 548, "time": 525, "price": 619}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 616, "time": 595, "price": 693}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "เลย", "transport": "บขส", "weights": {"distance": 214, "time": 105, "price": 430}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 71.9, "time": 75, "price": 150}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 222, "time": 240, "price": 267}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 305, "time": 270, "price": 380}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ฉะเชิงเทรา", "transport": "บขส", "weights": {"distance": 470, "time": 420, "price": 427}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 477, "time": 480, "price": 459}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "พัทลุง", "transport": "บขส", "weights": {"distance": 1284, "time": 1230, "price": 2078}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 623, "time": 710, "price": 729}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 237, "time": 240, "price": 374}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 317, "time": 275, "price": 374}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 1067, "time": 1200, "price": 1890}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 112, "time": 90, "price": 200}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 410, "time": 470, "price": 389}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 410, "time": 360, "price": 546}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 220, "time": 180, "price": 270}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 368, "time": 60, "price": 1305}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 379, "time": 70, "price": 1640}},
    {"zone": "ตะวันออกเฉียงเหนือ", "source": "ขอนแก่น", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 479, "time": 65, "price": 1670}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Added {len(new_edges)} routes (bus & flight) for Khon Kaen.")
