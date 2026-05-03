import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Phra Nakhon Si Ayutthaya (พระนครศรีอยุธยา) - Transport: บขส
# Region for Phra Nakhon Si Ayutthaya is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "กทม", "transport": "บขส", "weights": {"distance": 80.7, "time": 73, "price": 470}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 522, "time": 439, "price": 473}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 404, "time": 338, "price": 433}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 213, "time": 179, "price": 250}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "อุบลราชธานี", "transport": "บขส", "weights": {"distance": 558, "time": 455, "price": 524}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 772, "time": 654, "price": 594}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 179, "time": 165, "price": 300}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 105, "time": 89, "price": 470}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สระบุรี", "transport": "บขส", "weights": {"distance": 57.4, "time": 53, "price": 156}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "อำนาจเจริญ", "transport": "บขส", "weights": {"distance": 555, "time": 512, "price": 517}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 712, "time": 657, "price": 650}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "บุรีรัมย์", "transport": "บขส", "weights": {"distance": 345, "time": 282, "price": 333}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ชัยนาท", "transport": "บขส", "weights": {"distance": 120, "time": 111, "price": 571}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ชัยภูมิ", "transport": "บขส", "weights": {"distance": 313, "time": 289, "price": 265}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 719, "time": 664, "price": 650}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "กาฬสินธุ์", "transport": "บขส", "weights": {"distance": 467, "time": 390, "price": 550}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "กำแพงเพชร", "transport": "บขส", "weights": {"distance": 277, "time": 212, "price": 313}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 539, "time": 426, "price": 432}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ลำพูน", "transport": "บขส", "weights": {"distance": 580, "time": 447, "price": 594}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "เลย", "transport": "บขส", "weights": {"distance": 485, "time": 448, "price": 550}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ลพบุรี", "transport": "บขส", "weights": {"distance": 104, "time": 96, "price": 156}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "มหาสารคาม", "transport": "บขส", "weights": {"distance": 421, "time": 389, "price": 380}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "มุกดาหาร", "transport": "บขส", "weights": {"distance": 606, "time": 559, "price": 513}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "นครพนม", "transport": "บขส", "weights": {"distance": 693, "time": 640, "price": 576}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 176, "time": 141, "price": 693}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "หนองบัวลำภู", "transport": "บขส", "weights": {"distance": 468, "time": 421, "price": 550}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 576, "time": 485, "price": 515}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 625, "time": 577, "price": 576}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "เพชรบูรณ์", "transport": "บขส", "weights": {"distance": 296, "time": 273, "price": 407}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "พิจิตร", "transport": "บขส", "weights": {"distance": 271, "time": 220, "price": 299}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 317, "time": 251, "price": 320}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 500, "time": 462, "price": 468}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ปราจีนบุรี", "transport": "บขส", "weights": {"distance": 141, "time": 130, "price": 558}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ร้อยเอ็ด", "transport": "บขส", "weights": {"distance": 457, "time": 422, "price": 420}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สกลนคร", "transport": "บขส", "weights": {"distance": 597, "time": 551, "price": 558}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สิงห์บุรี", "transport": "บขส", "weights": {"distance": 77.8, "time": 70, "price": 135}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ศรีสะเกษ", "transport": "บขส", "weights": {"distance": 499, "time": 408, "price": 418}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สุโขทัย", "transport": "บขส", "weights": {"distance": 354, "time": 327, "price": 378}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "สุรินทร์", "transport": "บขส", "weights": {"distance": 385, "time": 318, "price": 367}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ตาก", "transport": "บขส", "weights": {"distance": 386, "time": 295, "price": 362}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 422, "time": 333, "price": 405}},
    {"zone": "กลาง", "source": "พระนครศรีอยุธยา", "destination": "ยโสธร", "transport": "บขส", "weights": {"distance": 481, "time": 444, "price": 457}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
