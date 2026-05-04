import subprocess
import json
import random
import re
import os
import sys

def extract_info(output):
    """Extracts the Path and Totals from the CLI output."""
    path_match = re.search(r"Path:\s*(.*)", output)
    path = path_match.group(1).strip() if path_match else None
    
    totals_match = re.search(r"Totals -> Distance:\s*([\d\.]+)km\s*\|\s*Time:\s*([\d\.]+)m\s*\|\s*Price:\s*([\d\.]+)฿", output)
    totals = None
    if totals_match:
        totals = {
            "distance": float(totals_match.group(1)),
            "time": float(totals_match.group(2)),
            "price": float(totals_match.group(3))
        }
    return path, totals

def run_implementation(cmd_list, choice, src, dest):
    """Runs a given implementation with the specified inputs."""
    input_str = f"{choice}\n{src}\n{dest}\n"
    # Ensure UTF-8 encoding for Thai characters
    result = subprocess.run(
        cmd_list,
        input=input_str,
        text=True,
        capture_output=True,
        encoding='utf-8'
    )
    return result.stdout

def get_vertices(json_path):
    """Loads vertices from the graph JSON to use for testing."""
    if not os.path.exists(json_path):
        print(f"Cannot find JSON data at {json_path}")
        sys.exit(1)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('vertices', [])

def main():
    # Make sure we're built
    if not os.path.exists("bin/Main.class"):
        print("Please compile the Java project first by running: ./run.sh")
        sys.exit(1)

    json_path = 'data/weight_data.json'
    vertices = get_vertices(json_path)
    
    if len(vertices) < 2:
        print("Not enough vertices inside JSON to perform tests.")
        sys.exit(1)

    print(f"Loaded {len(vertices)} vertices. Starting verification...\n")

    # Generate many test cases ensuring all travel options (choices) are tested
    test_cases = []
    all_choices = ["1", "2", "3", "1,2", "1,3", "2,3", "1,2,3"]
    
    # Create 3 test paths for EVERY possible combination of choices (21 total cases)
    for c in all_choices:
        for _ in range(3):
            u, v = random.sample(vertices, 2)
            test_cases.append((c, u, v))
            
    # Shuffle the test cases so the output is mixed
    random.shuffle(test_cases)

    java_cmd = ['java', '-cp', 'bin', 'Main']
    python_cmd = ['python3', 'scripts/test/dijkstra_route_optimizer.py']
    
    # If Python3 prefix doesn't work, try just python
    try:
        subprocess.run(['python3', '--version'], capture_output=True, check=True)
    except Exception:
        python_cmd[0] = 'python'

    passed = 0
    failed = 0

    for i, (choice, src, dest) in enumerate(test_cases, 1):
        print(f"Test Case {i}: Route {src} -> {dest} (Optimizing for: {choice})")
        
        py_out = run_implementation(python_cmd, choice, src, dest)
        java_out = run_implementation(java_cmd, choice, src, dest)

        py_path, py_totals = extract_info(py_out)
        java_path, java_totals = extract_info(java_out)

        print(f"  [Expected - Python]")
        print(f"    Path:   {py_path}")
        print(f"    Totals: {py_totals}")
        print(f"  [Result - Java]")
        print(f"    Path:   {java_path}")
        print(f"    Totals: {java_totals}")

        has_error = False

        if py_path != java_path:
            print(f"  ❌ PATH MISMATCH!")
            has_error = True
        else:
            print(f"  ✅ Paths match.")

        if py_totals and java_totals:
            # Check totals with a small margin of error for floating point differences
            diff_d = abs(py_totals['distance'] - java_totals['distance'])
            diff_t = abs(py_totals['time'] - java_totals['time'])
            diff_p = abs(py_totals['price'] - java_totals['price'])
            
            if diff_d > 0.1 or diff_t > 0.1 or diff_p > 0.1:
                print(f"  ❌ TOTALS MISMATCH!")
                has_error = True
            else:
                print(f"  ✅ Totals match.")
        elif py_totals != java_totals:
             print(f"  ❌ TOTALS MISMATCH (One is None)!")
             has_error = True

        if has_error:
            failed += 1
            print("  --- Failed ---")
        else:
            passed += 1
            print("  --- Passed ---")
        print()

    print("========================================")
    print(f"Verification Summary: {passed}/{passed+failed} Passed.")
    print("========================================")

    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
