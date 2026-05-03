import json

with open('weight_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Data from Nakhon Pathom (นครปฐม) - Transport: บขส
# Region for Nakhon Pathom is "กลาง" (Central)
new_edges = [
    {"zone": "กลาง", "source": "นครปฐม", "destination": "กาญจนบุรี", "transport": "บขส", "weights": {"distance": 68.9, "time": 64, "price": 90}},
    {"zone": "กลาง", "source": "นครปฐม", "destination": "เชียงใหม่", "transport": "บขส", "weights": {"distance": 696, "time": 642, "price": 733}},
    {"zone": "กลาง", "source": "นครปฐม", "destination": "ลำปาง", "transport": "บขส", "weights": {"distance": 610, "time": 563, "price": 733}}
]

data['edges'].extend(new_edges)

with open('weight_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("success")
