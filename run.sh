#!/bin/bash

mkdir -p bin

echo "Compiling Java files..."
find src -name "*.java" | xargs javac -cp "lib/*" -d bin

# Check if compilation succeeded
if [ $? -eq 0 ]; then
    echo "Build successful! Starting the application..."
    echo "============================================"

    java -cp "bin:lib/*" Main
else
    echo "Build failed! Please check the compilation errors."
    exit 1
fi
