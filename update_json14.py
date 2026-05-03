import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Prachuap Khiri Khan (ประจวบคีรีขันธ์)
# Region for Prachuap Khiri Khan is "ตะวันตก" (West) but often grouped with Central/South. Let's use "กลาง" or "ตะวันตก". Based on previous patterns, you've used "กลาง" for central ones. Let's stick with "ตะวันตก" as technically defined by Thai regions, or "กลาง" to match. I'll use "ตะวันตก" as it's standard, but wait, the prompt doesn't specify. I will assume "ตะวันตก" for Prachuap Khiri Khan. Actually, some sources put it in "ตะวันตก". Let's use "ตะวันตก".

def time_to_minutes(time_str):
    if "ชม" in time_str and "นาที" in time_str:
        parts = time_str.split("ชม")
        hours = int(parts[0].strip().replace('.', ''))
        mins = int(parts[1].replace("นาที", "").replace(".", "").strip())
        return hours * 60 + mins
    elif "ชม" in time_str:
        hours = int(time_str.replace("ชม", "").replace(".", "").strip())
        return hours * 60
    elif "นาที" in time_str:
        return int(time_str.replace("นาที", "").strip())
    else:
        try:
            return int(time_str.strip())
        except ValueError:
            return time_str

new_edges = [
    # Transport: บขส (Bus)
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "กทม", "transport": "บขส", "weights": {"distance": 501, "time": 240, "price": 256}}, # 4ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 454, "time": 354, "price": 355}}, # 354 is already minutes as it has no ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 398, "time": 300, "price": 628}}, # 5ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "สมุทรปราการ", "transport": "บขส", "weights": {"distance": 299, "time": 240, "price": 397}}, # 4ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 249, "time": 197, "price": 400}},
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 459, "time": 362, "price": 745}},
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "เพชรบุรี", "transport": "บขส", "weights": {"distance": 151, "time": 139, "price": 169}},
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 363, "time": 280, "price": 899}},
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 475, "time": 417, "price": 899}},
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 498, "time": 430, "price": 899}}, # 7ชม. 10 นาที
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 398, "time": 300, "price": 592}}, # Duplicate row, different price?? Wait, it's there. 5ชม.
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 161.62, "time": 200, "price": 625}}, # 3 ชม.20 นาที
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 881, "time": 695, "price": 1000}}, # 11ชม. 35 นาที
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 454, "time": 320, "price": 652}}, # 5ชม. 20
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 555, "time": 510, "price": 1316}}, # 8ชม. 30
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "สมุทรสงคราม", "transport": "บขส", "weights": {"distance": 207, "time": 170, "price": 205}}, # 2ชม. 50
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ยะลา", "transport": "บขส", "weights": {"distance": 790, "time": 780, "price": 995}}, # 13 ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ปัตตานี", "transport": "บขส", "weights": {"distance": 769, "time": 660, "price": 970}}, # 11 ชม
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "ระนอง", "transport": "บขส", "weights": {"distance": 290, "time": 250, "price": 549}}, # 4 ชม 10 นาที

    # Transport: เครื่องบิน (Airplane)
    {"zone": "ตะวันตก", "source": "ประจวบคีรีขันธ์", "destination": "เชียงใหม่", "transport": "เครื่องบิน", "weights": {"distance": 690, "time": 75, "price": 3890}} # 1 ชม. 15 นาที
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
