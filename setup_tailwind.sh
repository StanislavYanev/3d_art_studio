#!/bin/bash

set -e

echo "🚀 Настройка на Tailwind CSS за Django (v3)..."

# Проверка за Node и npm
if ! command -v node &> /dev/null; then
  echo "❌ Node.js не е инсталиран."
  exit 1
fi

if ! command -v npm &> /dev/null; then
  echo "❌ npm не е инсталиран."
  exit 1
fi

# Папки и пътища
PROJECT_ROOT=$(pwd)
STATIC_DIR="$PROJECT_ROOT/static"
INPUT_CSS="$STATIC_DIR/src/input.css"
OUTPUT_CSS="$STATIC_DIR/css/output.css"
TAILWIND="$PROJECT_ROOT/node_modules/.bin/tailwindcss"

# Създаване на нужните папки
mkdir -p "$STATIC_DIR/src"
mkdir -p "$STATIC_DIR/css"

# Инициализация на npm
if [ ! -f package.json ]; then
  echo "📦 Създаване на package.json..."
  npm init -y
fi

# Инсталиране на Tailwind CSS v3 и зависимости
echo "📥 Инсталиране на Tailwind CSS v3 + PostCSS..."
npm install -D tailwindcss@3 postcss autoprefixer

# Проверка дали Tailwind е инсталиран
if [ ! -f "$TAILWIND" ]; then
  echo "❌ Tailwind не се е инсталирал правилно."
  exit 1
fi

# Генериране на конфигурационни файлове
echo "⚙️ Генериране на Tailwind и PostCSS конфигурации..."
npx tailwindcss init -p

# Създаване на input.css
echo "🎨 Създаване на input.css..."
cat <<EOL > "$INPUT_CSS"
@tailwind base;
@tailwind components;
@tailwind utilities;
EOL

# Конфигуриране на tailwind.config.js
echo "🔧 Настройка на Tailwind config..."
cat <<EOL > tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOL

# Генериране на финалния CSS файл
echo "🏗️ Генериране на output.css..."
$TAILWIND -i "$INPUT_CSS" -o "$OUTPUT_CSS" --minify

echo "✅ Tailwind CSS е успешно конфигуриран! CSS файл: $OUTPUT_CSS"
echo "📌 Включи го в Django шаблон с: {% load static %} <link href=\"{% static 'css/output.css' %}\" rel=\"stylesheet\">"
