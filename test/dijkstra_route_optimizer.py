import json
import os
import heapq

class Graph:
    def __init__(self):
        # The adjacency list dictionary acts as our linked list mapping for each vertex
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, source, destination, transport, distance, time, price):
        # We append a dictionary (node) matching standard Adjacency List pattern
        self.adj_list[source].append({
            'destination': destination,
            'transport': transport,
            'distance': distance,
            'time': time,
            'price': price
        })

    def dijkstra(self, start_node, end_node, weight_keys):
        # Priority queue to hold (current_weight, current_node)
        pq = [(0, start_node)]
        
        # Track the minimum weight to reach each node
        min_weights = {node: float('inf') for node in self.adj_list}
        min_weights[start_node] = 0
        
        # Track the path (previous_node, edge_details_used)
        predecessors = {}
        
        while pq:
            current_weight, current_node = heapq.heappop(pq)
            
            # If we reached our destination, we can break early
            if current_node == end_node:
                break
                
            # If we already found a shorter path to this node, ignore
            if current_weight > min_weights[current_node]:
                continue
                
            # Traverse all neighbor edges (linked list traversal representation)
            for edge in self.adj_list[current_node]:
                neighbor = edge['destination']
                
                # Fetch weight dynamically depending on user's choices (sum of requested weights)
                weight = sum(edge[k] for k in weight_keys)
                new_weight = current_weight + weight
                
                if new_weight < min_weights[neighbor]:
                    min_weights[neighbor] = new_weight
                    predecessors[neighbor] = (current_node, edge)
                    heapq.heappush(pq, (new_weight, neighbor))
                    
        # Path reconstruction
        if end_node not in predecessors and start_node != end_node:
            return None, None
            
        path = []
        edges_used = []
        current = end_node
        
        while current in predecessors:
            prev_node, edge_data = predecessors[current]
            path.append(current)
            edges_used.append(edge_data)
            current = prev_node
            
        path.append(start_node)
        path.reverse()
        edges_used.reverse()
        
        return path, edges_used

def load_graph(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    graph = Graph()
    
    vertices = data.get('vertices', [])
    for v in vertices:
        graph.add_vertex(v)

    edges = data.get('edges', [])
    for e in edges:
        if e.get('source') and e.get('destination'):
            weights = e.get('weights', {})
            graph.add_edge(
                source=e['source'], 
                destination=e['destination'], 
                distance=weights.get('distance', float('inf')),
                time=weights.get('time', float('inf')),
                price=weights.get('price', float('inf')),
                transport=e.get('transport', 'Unknown')
            )
            
    return graph, set(vertices)

def main():
    # Try looking in 'data' directory if not in root
    json_file = 'weight_data.json'
    if not os.path.exists(json_file):
        json_file = os.path.join('data', 'weight_data.json')
        
    if not os.path.exists(json_file):
        print(f"Could not find JSON data file.")
        return

    print("Loading graph data...")
    G, valid_nodes = load_graph(json_file)
    
    # Calculate edge count from adjacency list
    edge_count = sum(len(edges) for edges in G.adj_list.values())
    print(f"Loaded {len(G.adj_list)} vertices and {edge_count} edges.\n")

    print("=== Route Optimization ===")
    print("What do you want to save the most? (Minimize)")
    print("You can choose multiple separated by commas (e.g., 1,3 or 1,2,3)")
    print("1. Distance (km)")
    print("2. Time (minutes)")
    print("3. Price (Baht)")
    
    choice_input = input("Enter your choice(s) (1-3): ").strip()
    weight_map = {'1': 'distance', '2': 'time', '3': 'price'}
    
    choices = [c.strip() for c in choice_input.split(',')]
    weight_keys = [weight_map[c] for c in choices if c in weight_map]
    
    if not weight_keys:
        print("Invalid choice. Exiting.")
        return

    source = input("Enter source province (e.g., กทม): ").strip()
    if source not in valid_nodes:
        print(f"Error: '{source}' is not a valid location in the data.")
        return

    destination = input("Enter destination province (e.g., เชียงใหม่): ").strip()
    if destination not in valid_nodes:
        print(f"Error: '{destination}' is not a valid location in the data.")
        return

    try:
        # Use our custom Dijkstra's algorithm relying on our graph adjacency list
        path, edge_details = G.dijkstra(source, destination, weight_keys)
        
        if not path:
            print(f"\nNo path found between '{source}' and '{destination}'.")
            return

        print("\n=== Best Route Found ===")
        opt_names = [w.capitalize() for w in weight_keys]
        print(f"Optimized for minimizing: {', '.join(opt_names)}")
        print(f"Path: {' -> '.join(path)}\n")
        
        # Reconstruct details to show segment-by-step
        print("Detailed steps:")
        total_dist = 0
        total_time = 0
        total_price = 0
        
        for i, edge in enumerate(edge_details):
            trans = edge['transport']
            d = edge['distance']
            t = edge['time']
            p = edge['price']
            
            total_dist += d
            total_time += t
            total_price += p
            
            print(f"{i+1}. {path[i]} -> {path[i+1]} (via {trans})")
            print(f"   Distance: {d}km, Time: {t}m, Price: {p}฿")
            
        print("-" * 40)
        print(f"Totals -> Distance: {total_dist}km | Time: {total_time}m | Price: {total_price}฿")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
