#!/bin/bash

# Exit on error
set -e

# Project root (adjust if needed)
PROJECT_ROOT=$(pwd)
STATIC_DIR="$PROJECT_ROOT/static"
CSS_INPUT="$STATIC_DIR/src/input.css"
CSS_OUTPUT="$STATIC_DIR/css/output.css"

# Create necessary directories
mkdir -p "$STATIC_DIR/src"
mkdir -p "$STATIC_DIR/css"

# Step 1: Initialize npm if not present
if [ ! -f "$PROJECT_ROOT/package.json" ]; then
  npm init -y
fi

# Step 2: Install Tailwind and dependencies
npm install -D tailwindcss postcss autoprefixer

# Step 3: Generate config files
npx tailwindcss init -p

# Step 4: Create input.css with Tailwind directives
cat <<EOL > "$CSS_INPUT"
@tailwind base;
@tailwind components;
@tailwind utilities;
EOL

# Step 5: Configure Tailwind to scan your templates
cat <<EOL > tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOL

# Step 6: Build Tailwind output
npx tailwindcss -i "$CSS_INPUT" -o "$CSS_OUTPUT" --minify

echo "✅ Tailwind CSS setup complete. Output file: $CSS_OUTPUT"

