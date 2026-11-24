# Лайфстайл-лента Jacey: Google Flow (Nano Banana → Frames to Video)
Ингредиенты: image 1 — Jacey (анфас/3/4, лицо открыто); image 2 — продукт бренда (сумка/очки/одежда, фото на белом фоне); image 3 — референс с Pinterest (только поза/сцена/свет, НЕ лицо).

## JSON — фото
{
  "format": "vertical 9:16 photo",
  "subject": "the woman from image 1; keep her face exactly as in image 1: same full lip volume and lip shape, nose, eye shape, face proportions, skin texture; no beautification, no face reshaping, no lip thinning, no skin smoothing",
  "pose_and_scene_reference": "use image 3 ONLY for pose, composition, location and lighting; do NOT copy the face, hair or body of the person in image 3",
  "outfit": "<одежда>",
  "brand_item": "the <item> from image 2, kept exactly the same: shape, color, hardware and logo as in image 2, logo sharp and readable",
  "scene": "<где>",
  "action": "<что делает в этот момент>",
  "camera": "<селфи / со стороны / сверху>, <объектив>",
  "light": "<свет>",
  "style": "candid lifestyle photo, natural iPhone look, real skin with pores, no filter",
  "avoid": "extra fingers, warped logo, invented text, changed face"
}

## JSON — видео (Frames to Video, 8 c)
{
  "instruction": "animate this exact frame",
  "identity_lock": "keep her face exactly as in the first frame for the whole video; same lips, nose, eyes, proportions; no beautification",
  "product_lock": "keep the <item> and its logo exactly as in the first frame, no warping",
  "action": "<одно простое действие>",
  "rules": "hands never pass in front of her face; small head movements only; no big mouth movements",
  "camera": "<движение камеры>",
  "sound": "<звуки>, no speech",
  "duration": "8 seconds"
}
