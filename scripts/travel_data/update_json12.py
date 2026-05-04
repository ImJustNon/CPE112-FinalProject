import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Samut Sakhon (สมุทรสาคร) - Transport: บขส
# Region for Samut Sakhon is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "กทม", "transport": "บขส", "weights": {"distance": 44.8, "time": 41, "price": 60}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "ประจวบคีรีขันธ์", "transport": "บขส", "weights": {"distance": 246, "time": 199, "price": 220}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "สุราษฎร์ธานี", "transport": "บขส", "weights": {"distance": 599, "time": 492, "price": 899}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "พังงา", "transport": "บขส", "weights": {"distance": 729, "time": 601, "price": 899}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "กระบี่", "transport": "บขส", "weights": {"distance": 740, "time": 601, "price": 899}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "ชุมพร", "transport": "บขส", "weights": {"distance": 416, "time": 335, "price": 400}},
    {"zone": "กลาง", "source": "สมุทรสาคร", "destination": "ภูเก็ต", "transport": "บขส", "weights": {"distance": 800, "time": 678, "price": 1112}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
