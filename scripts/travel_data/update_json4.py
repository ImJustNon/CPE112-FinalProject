import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_edges = [
    # เครื่องบิน สงขลา
    {"zone": "ใต้", "source": "สงขลา", "destination": "กทม", "transport": "เครื่องบิน", "weights": {"distance": 760, "time": 85, "price": 1855.00}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "สมุทรปราการ", "transport": "เครื่องบิน", "weights": {"distance": 756, "time": 90, "price": 2060.00}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ภูเก็ต", "transport": "เครื่องบิน", "weights": {"distance": 258, "time": 55, "price": 2585.00}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "อุดรธานี", "transport": "เครื่องบิน", "weights": {"distance": 1185, "time": 130, "price": 3250}},
    
    # บขส สงขลา
    {"zone": "ใต้", "source": "สงขลา", "destination": "กทม", "transport": "บขส", "weights": {"distance": 990, "time": 813, "price": 785}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "บึงกาฬ", "transport": "บขส", "weights": {"distance": 1751, "time": 1394, "price": 2162}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "เชียงราย", "transport": "บขส", "weights": {"distance": 1782, "time": 1402, "price": 2220}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ชลบุรี", "transport": "บขส", "weights": {"distance": 1000, "time": 840, "price": 1425}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ขอนแก่น", "transport": "บขส", "weights": {"distance": 1436, "time": 1122, "price": 1786}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 296, "time": 330, "price": 450}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "นครราชสีมา", "transport": "บขส", "weights": {"distance": 1217, "time": 994, "price": 1554}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "นครสวรรค์", "transport": "บขส", "weights": {"distance": 1193, "time": 967, "price": 1529}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "นครศรีธรรมราช", "transport": "บขส", "weights": {"distance": 188, "time": 159, "price": 170}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "หนองคาย", "transport": "บขส", "weights": {"distance": 1616, "time": 1285, "price": 2069}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "พัทลุง", "transport": "บขส", "weights": {"distance": 108, "time": 118, "price": 80}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "พะเยา", "transport": "บขส", "weights": {"distance": 1689, "time": 1316, "price": 2106}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "พิษณุโลก", "transport": "บขส", "weights": {"distance": 1367, "time": 1056, "price": 1691}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "แพร่", "transport": "บขส", "weights": {"distance": 1519, "time": 1228, "price": 1918}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 400, "time": 420, "price": 396}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 679, "time": 600, "price": 979}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ราชบุรี", "transport": "บขส", "weights": {"distance": 901, "time": 840, "price": 850}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ระยอง", "transport": "บขส", "weights": {"distance": 1025, "time": 810, "price": 1518}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "สมุทรสาคร", "transport": "บขส", "weights": {"distance": 927, "time": 883, "price": 979}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "สตูล", "transport": "บขส", "weights": {"distance": 125, "time": 90, "price": 300}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 320, "time": 276, "price": 310}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ตรัง", "transport": "บขส", "weights": {"distance": 160, "time": 135, "price": 254}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "อุดรธานี", "transport": "บขส", "weights": {"distance": 1567, "time": 1238, "price": 1929}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "อุตรดิตถ์", "transport": "บขส", "weights": {"distance": 1475, "time": 1130, "price": 1823}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ปัตตานี", "transport": "บขส", "weights": {"distance": 107, "time": 120, "price": 157}},
    {"zone": "ใต้", "source": "สงขลา", "destination": "ยะลา", "transport": "บขส", "weights": {"distance": 140, "time": 120, "price": 380}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
