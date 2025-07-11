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

- 5 correspond to number of pictures to generate

![](generate/picture_0.png)

![](assets/gif_generate_picture.gif)

### TO generate gif of the pictures

```bash
python3 tools/generate_gif.py generate/ my_gif.gif
```

# V - Apply tracking of all pictures

---

Generating a picture with vector of stars mouvement

![](assets/output_image_vectors_3.png)

![](assets/gif_vector.gif)

# VI - Run main code

```bash
python3 main.py assets/test_1.png 
```