import json
import networkx as nx
import matplotlib.pyplot as plt

# Set font to support Thai characters on macOS
plt.rcParams['font.family'] = 'Ayuthaya'  # Apple's Thai font, alternative: 'Thonburi' or 'Tahoma'

def visualize_graph(json_file):
    print(f"Loading data from {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create a Directed Graph
    G = nx.DiGraph()

    # Add nodes (vertices)
    nodes = data.get('vertices', [])
    G.add_nodes_from(nodes)
    print(f"Added {len(nodes)} vertices.")

    # Add edges
    edges = data.get('edges', [])
    edge_count = 0
    for e in edges:
        # Some objects in the JSON might be empty from data cleaning, check if 'source' and 'destination' exist
        if e.get('source') and e.get('destination'):
            G.add_edge(e['source'], e['destination'], transport=e.get('transport', ''))
            edge_count += 1
            
    print(f"Added {edge_count} edges.")

    # Visualization setup
    plt.figure(figsize=(16, 12))
    
    # Calculate layout
    print("Calculating graph layout (this might take a few seconds)...")
    pos = nx.spring_layout(G, k=1.5, seed=42)  # k controls distance between nodes

    # Draw the graph
    print("Drawing the graph...")
    # Nodes
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue', alpha=0.8)
    
    # Edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.3, arrowsize=10, edge_color='gray')
    
    # Labels
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='Ayuthaya', font_color='black')

    plt.title("Transportation Network Graph", fontsize=16)
    plt.axis('off')  # Hide axis
    plt.tight_layout()
    
    print("Opening visualization window...")
    plt.show()

if __name__ == "__main__":
    visualize_graph('weight_data.json')
