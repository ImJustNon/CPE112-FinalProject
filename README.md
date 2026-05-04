# Thai Route Optimizer (Dijkstra's Algorithm)

A Java-based route optimization application that calculates the best travel paths between provinces in Thailand. It uses a custom implementation of Dijkstra's algorithm relying on an Adjacency Linked-List graph structure.

## Features
- Custom Graph implementation using an Adjacency List (`Map<String, LinkedList<Edge>>`).
- Optimize travel routes based on single or combined criteria:
  - Distance (km)
  - Time (minutes)
  - Price (Baht)
- Object-Oriented design with cleanly separated packages for Model, Graph, Algorithm, and Parsing logic.

## Folder Structure
- `src/`: Java source code organized conceptually:
  - `model/`: Data structures representing Edges and Path Results.
  - `graph/`: Adjacency List Graph representation.
  - `algorithm/`: Core Dijkstra logic using Priority Queues.
  - `parser/`: JSON parsing logic for graph generation.
- `data/`: Contains `weight_data.json` comprising nodes (provinces) and edges (routes).
- `bin/`: Output directory for compiled Java `.class` files.
- `scripts/test/`: Contains the original Python implementation and automated verifier scripts.

## Prerequisites
- **Java Development Kit (JDK)** 8 or higher.
- (Optional) **Python 3** to run the verification and testing script.

## How to Build and Run

### Option 1: Quick Start (Mac/Linux)
The easiest way to automatically compile and run the application is by using the included `run.sh` file.
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Manual Terminal Commands
1. Compile the Java files dynamically into the `bin` directory:
   ```bash
   mkdir -p bin
   find src -name "*.java" | xargs javac -d bin
   ```
2. Execute the compiled application from the root directory:
   ```bash
   java -cp bin Main
   ```

## How to Use
Once the program launches in your terminal, follow the interactive prompts:
1. **Optimization Choice**: Decide what constraints you want to minimize. Enter `1` for Distance, `2` for Time, or `3` for Price. You can also mix them separated by commas (e.g., `1,3` for Distance and Price).
2. **Source**: Enter your starting province (e.g., `กทม`).
3. **Destination**: Enter your target province (e.g., `เชียงใหม่`).

The program will print out the step-by-step route, the transportation method for each link, and the total cost/distance/time.

## Testing and Verification
To ensure the Java implementation behaves identically to the original Python algorithm, run the automated test script. It will generate random routing cases and compare both outputs dynamically.
```bash
python3 scripts/test/verify_routes.py
```
