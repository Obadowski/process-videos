#!/bin/bash

set -e

echo "🧹 Cleaning previous builds..."
rm -rf build dist *.egg-info

echo "📦 Building package..."
python -m build

echo "🚀 Uploading to PyPI..."
twine upload dist/*

echo "✅ Package published successfully!"

