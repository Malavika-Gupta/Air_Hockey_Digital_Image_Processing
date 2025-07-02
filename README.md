# 🏒✨ Air Hockey — Hand Gesture Controlled Game

A real-time air hockey game powered by **OpenCV** and **PyTorch**, with hand gesture tracking, physics, power-ups, sound effects, and a neon vibe.

![Gameplay Preview](./preview.gif)

---

## 📌 **About**

This project demonstrates digital image processing and computer vision for interactive gaming.  
Use your webcam to control paddles with simple colored gloves or hand tracking.

- **Completed:** January 31, 2025  
- **Language:** Python  
- **Libraries:** OpenCV, Pygame

---

## 🎮 **Features**

✅ Real-time hand gesture detection (HSV + contours)  
✅ Physics-based puck with speed boost  
✅ Neon glow effect for the ball  
✅ Paddle collisions, edge bounces, scoring  
✅ Random power-ups: speed boost, paddle freeze, (multi-ball placeholder)  
✅ Visual score overlay with outlined text & backdrop  
✅ Game ends with clear win message

---

## 🧩 **How it Works**

- **Detection:** Color-based HSV filtering + contour centroids → your hand = paddle.  
- **Power-Ups:** Spawns every 10 seconds, expires after 8 seconds if untouched.  
- **Audio:** Pygame mixer plays sounds for paddle hits, wall bounces, and goals.  
- **Score:** First to 5 points wins!

---

## 🚀 **Run It Yourself**

1️⃣ Install requirements:
```bash
pip install opencv-python pygame numpy
```
2️⃣ Run:
```bash
python main.py
```
3️⃣ Use q to quit.
