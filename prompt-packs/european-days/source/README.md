# Исходник European Days
- data_fixed.json — 50 промптов и 4 фотоистории (исправлено: Birkin → top-handle bag, экспозиция в №06).
- texts.py — тексты страниц RU/EN. style.css — вёрстка.
- Сборка: скопировать img/*.jpg рядом со скриптами в папку build/, затем
  `python3 build.py ru && python3 build.py en && node build/render.js`
- im-005-clean.jpg — фото №06 без псевдо-логотипа на сумке.
