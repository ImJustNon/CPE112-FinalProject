import json

province_codes = {
    "กทม": "BKK", "กระบี่": "KBI", "กาญจนบุรี": "KAN", "กาฬสินธุ์": "KAL", "กำแพงเพชร": "KPT", 
    "ขอนแก่น": "KKC", "จันทบุรี": "CTI", "ฉะเชิงเทรา": "CCO", "ชลบุรี": "CHB", "ชัยนาท": "CNT", 
    "ชัยภูมิ": "CPM", "ชุมพร": "CJM", "เชียงราย": "CEI", "เชียงใหม่": "CNX", "ตรัง": "TST", 
    "ตราด": "TDX", "ตาก": "TAK", "นครนายก": "NYK", "นครปฐม": "NPT", "นครพนม": "KOP", 
    "นครราชสีมา": "NAK", "นครศรีธรรมราช": "NST", "นครสวรรค์": "NWN", "นนทบุรี": "NBI", 
    "นราธิวาส": "NAW", "น่าน": "NNT", "บึงกาฬ": "BKN", "บุรีรัมย์": "BFV", "ปทุมธานี": "PTE", 
    "ประจวบคีรีขันธ์": "PKN", "ปราจีนบุรี": "PRI", "ปัตตานี": "PTN", "พระนครศรีอยุธยา": "AYA", 
    "พะเยา": "PYO", "พังงา": "PNA", "พัทลุง": "PLG", "พิจิตร": "PCT", "พิษณุโลก": "PHS", 
    "เพชรบุรี": "PBI", "เพชรบูรณ์": "PHY", "แพร่": "PRH", "ภูเก็ต": "HKT", "มหาสารคาม": "MKM", 
    "มุกดาหาร": "MDH", "แม่ฮ่องสอน": "HGN", "ยโสธร": "YST", "ยะลา": "YLA", "ร้อยเอ็ด": "ROI", 
    "ระนอง": "UNN", "ระยอง": "RYG", "ราชบุรี": "RBR", "ลพบุรี": "LRI", "ลำปาง": "LPT", 
    "ลำพูน": "LPN", "เลย": "LOE", "ศรีสะเกษ": "SSK", "สกลนคร": "SNO", "สงขลา": "SGZ", 
    "สตูล": "SAT", "สมุทรปราการ": "SPK", "สมุทรสงคราม": "SKM", "สมุทรสาคร": "SKN", 
    "สระแก้ว": "SKW", "สระบุรี": "SRI", "สิงห์บุรี": "SBR", "สุโขทัย": "THS", 
    "สุพรรณบุรี": "SPB", "สุราษฎร์ธานี": "URT", "สุรินทร์": "SRN", "หนองคาย": "NKI", 
    "หนองบัวลำภู": "NBP", "อ่างทอง": "ATG", "อำนาจเจริญ": "ACR", "อุดรธานี": "UTH", 
    "อุตรดิตถ์": "UTD", "อุทัยธานี": "UTI", "อุบลราชธานี": "UBP"
}

transport_codes = {
    "เครื่องบิน": "AIR",
    "บขส": "BUS",
    # Add รถไฟ (Train) if it exists, etc. Or just use uppercase transport type
}


with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# count per source and transport
counts = {}

for edge in data['edges']:
    source = edge.get('source', '')
    transport = edge.get('transport', '')
    
    s_code = province_codes.get(source, "UNK")
    t_code = transport_codes.get(transport, "UNK")
    if t_code == "UNK":
        # Maybe use part of the name if not mapped
        t_code = transport.upper()
        
    key = f"{source}_{transport}"
    counts[key] = counts.get(key, 0) + 1
    
    edge_id = f"{s_code}_{t_code}_{counts[key]}"
    edge['id'] = edge_id
    
    # Reorder keys to put id first
    new_edge = {'id': edge['id']}
    for k, v in edge.items():
        if k != 'id':
            new_edge[k] = v
    edge.clear()
    edge.update(new_edge)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("done")
