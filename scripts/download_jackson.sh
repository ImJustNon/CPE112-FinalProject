#!/bin/bash
mkdir -p lib
cd lib
if [ ! -f "jackson-core-2.15.2.jar" ]; then
    echo "Downloading Jackson Core..."
    curl -sO https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.15.2/jackson-core-2.15.2.jar
fi
if [ ! -f "jackson-annotations-2.15.2.jar" ]; then
    echo "Downloading Jackson Annotations..."
    curl -sO https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.15.2/jackson-annotations-2.15.2.jar
fi
if [ ! -f "jackson-databind-2.15.2.jar" ]; then
    echo "Downloading Jackson Databind..."
    curl -sO https://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.15.2/jackson-databind-2.15.2.jar
fi
