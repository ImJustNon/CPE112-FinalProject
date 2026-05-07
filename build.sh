#!/bin/bash

SRC_DIR="src"
OUT_DIR="build/classes"
JAR_DIR="build"
JAR_NAME="FinalProject.jar"
MAIN_CLASS="Main"

echo "=== Building Java Project ==="

echo "Cleaning old build..."
rm -rf "$OUT_DIR" "$JAR_DIR/$JAR_NAME"
mkdir -p "$OUT_DIR"

JAVA_FILES=$(find "$SRC_DIR" -name "*.java")

if [ -z "$JAVA_FILES" ]; then
    echo "Error: No Java files found in $SRC_DIR"
    exit 1
fi

echo "Compiling Java files..."
javac -d "$OUT_DIR" -sourcepath "$SRC_DIR" $JAVA_FILES

if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi

MANIFEST_FILE="$JAR_DIR/Manifest.txt"
echo "Main-Class: $MAIN_CLASS" > "$MANIFEST_FILE"

echo "Creating JAR file..."
jar cfm "$JAR_DIR/$JAR_NAME" "$MANIFEST_FILE" -C "$OUT_DIR" .

if [ $? -ne 0 ]; then
    echo "Failed to create JAR file!"
    rm -f "$MANIFEST_FILE"
    exit 1
fi

rm -f "$MANIFEST_FILE"

echo "=== Build Successful ==="
echo "JAR created at: $JAR_DIR/$JAR_NAME"
echo ""
echo "To run the application:"
echo "java -jar $JAR_DIR/$JAR_NAME"
