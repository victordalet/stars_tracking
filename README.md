# stars_tracking

---

# I - Image base

---

![](assets/test_1.png)

# II - black and white picture

---

![](assets/output_image_black_and_white.png)

# III - Find track of stars

---

![](assets/output_image_tracking.png)

# IV - Generate new picture

---

```bash
export PYTHONPATH=$(pwd)
python3 tools/generate_picutre.py assets/test_1.png 5
```

![](generate/picture_0.png)
![](generate/picture_1.png)

# V - Apply tracking of all pictures