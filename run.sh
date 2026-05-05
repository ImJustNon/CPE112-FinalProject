#!/bin/bash

# Create bin directory if it doesn't exist
mkdir -p bin

# Find all Java files in the src directory and compile them into the bin directory
echo "Compiling Java files..."
find src -name "*.java" | xargs javac -d bin

# Check if compilation succeeded
if [ $? -eq 0 ]; then
    echo "Build successful! Starting the application..."
    echo "============================================"
    # Run the compiled Java program from the bin directory
    # Note: run from the root directory so the app can find data/weight_data.json
    java -cp bin Main
else
    echo "Build failed! Please check the compilation errors."
    exit 1
fi
