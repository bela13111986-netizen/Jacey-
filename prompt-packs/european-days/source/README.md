# Исходник European Days
- data_fixed.json — 50 промптов и 4 фотоистории (исправлена экспозиция в №06).
- texts.py — тексты страниц RU/EN. style.css — вёрстка.
- Сборка: скопировать img/*.jpg рядом со скриптами в папку build/, затем
  `python3 build.py ru && python3 build.py en && node build/render.js`
