#!/bin/bash

echo "Checking Python..."

python3 --version


echo ""
echo "Checking Ollama connectivity..."

curl $OLLAMA_HOST/api/tags


echo ""
echo "Checking Python packages..."

pip list | grep langchain
pip list | grep chroma


echo ""
echo "Verification completed"