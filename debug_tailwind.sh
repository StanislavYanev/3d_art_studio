#!/bin/bash

echo "🔍 Tailwind CSS Debug Script"
echo "============================="

echo ""
echo "📦 Проверка за Node.js и npm:"
echo "-----------------------------"
echo -n "Node.js: "
if command -v node &> /dev/null; then
  node -v
else
  echo "❌ НЕ е инсталиран"
fi

echo -n "npm: "
if command -v npm &> /dev/null; then
  npm -v
else
  echo "❌ НЕ е инсталиран"
fi

echo ""
echo "📁 Проверка за node_modules и Tailwind:"
echo "---------------------------------------"
if [ -d "node_modules" ]; then
  echo "✅ Има node_modules/"
else
  echo "❌ Липсва node_modules/"
fi

echo -n "➡️  Tailwind бинарен файл: "
if [ -f "./node_modules/.bin/tailwindcss" ]; then
  echo "✅ НАМЕРЕН"
else
  echo "❌ ЛИПСВА"
fi

echo ""
echo "📄 Списък на инсталираните npm пакети:"
echo "-------------------------------------"
npm list --depth=0 || echo "⚠️ Неуспешно четене на npm пакетите."

echo ""
echo "📂 Проверка за конфигурационни файлове:"
echo "---------------------------------------"
[ -f "tailwind.config.js" ] && echo "✅ tailwind.config.js наличен" || echo "❌ Липсва tailwind.config.js"
[ -f "postcss.config.js" ] && echo "✅ postcss.config.js наличен" || echo "❌ Липсва postcss.config.js"

echo ""
echo "🧪 Опит за стартиране на Tailwind:"
echo "----------------------------------"
if [ -f "./node_modules/.bin/tailwindcss" ]; then
  ./node_modules/.bin/tailwindcss -v || echo "❌ Tailwind не се стартира"
else
  echo "⛔ tailwindcss не е наличен в node_modules/.bin"
fi

echo ""
echo "✅ Диагностиката приключи. Сподели резултатите, ако искаш помощ."
