# 🏷️ PyQt5 QLabel Demo

This project demonstrates how to use **QLabels in PyQt5**.  
Labels are used to display text (or images) inside a PyQt5 window.

---

## 🚀 Features
- Create a **QLabel** widget
- Set custom **font family and size**
- Apply CSS **styles** (color, background, bold, italic, underline)
- Control text **alignment** (horizontal + vertical)

---

## 📦 Requirements
Install PyQt5 with:

```bash
pip install PyQt5

Control label alingment:
label.setAlignment(Qt.AlignCenter)       # Center both ways
label.setAlignment(Qt.AlignTop)          # Align top
label.setAlignment(Qt.AlignBottom)       # Align bottom
label.setAlignment(Qt.AlignRight)        # Align right
label.setAlignment(Qt.AlignHCenter)      # Align horizontally center
label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)   # Top + Center
