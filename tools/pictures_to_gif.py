import os
import sys
from PIL import Image


class PicturesToGif:
    def __init__(self, pictures, gif_path):
        self.pictures = pictures
        self.gif_path = gif_path

    def create_gif(self):
        images = [Image.open(picture) for picture in self.pictures]
        images[0].save(
            self.gif_path, save_all=True, append_images=images[1:], loop=0, duration=500
        )
        print(f"GIF saved to {self.gif_path}")


if __name__ == "__main__":
    pictures = os.listdir(sys.argv[1])
    PicturesToGif(
        [
            os.path.join(sys.argv[1], picture)
            for picture in pictures
            if picture.endswith(".png")
        ],
        sys.argv[2],
    ).create_gif()
