import sys

from picture_manager import PictureManager
from tracking import Tracking


class Main:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def run(self):
        img = PictureManager.load_image(self.image_path)
        filtered_image = PictureManager.apply_filter(img)
        PictureManager.save_image(filtered_image, "output_image_black_and_white.png")
        stars = Tracking.find_coordinate_of_all_stars(filtered_image)
        stars = Tracking.remove_false_positive(stars)
        filtered_image = PictureManager.display_tracking_stars(filtered_image, stars)
        PictureManager.save_image(filtered_image, "output_image_tracking.png")
        print(stars)


if __name__ == "__main__":
    run = Main(sys.argv[1])

    run.run()
