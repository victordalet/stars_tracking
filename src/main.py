import os
import sys

from picture_manager import PictureManager
from star_matcher import StarMatcher
from tracking import Tracking


class Main:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.stars_positions = []

    def preprocess(self):
        img = PictureManager.load_image(self.image_path)
        filtered_image = PictureManager.apply_filter(img)
        PictureManager.save_image(filtered_image, "output_image_black_and_white.png")
        stars = Tracking.find_coordinate_of_all_stars(filtered_image)
        stars = Tracking.remove_false_positive(stars)
        self.stars_positions.append(stars)
        filtered_image = PictureManager.display_tracking_stars(filtered_image, stars)
        PictureManager.save_image(filtered_image, "output_image_tracking.png")

    def tracking(self):
        if not os.path.exists("generate"):
            os.makedirs("generate")
        images = os.listdir("generate")
        for image in images:
            img = PictureManager.load_image(f"generate/{image}")
            filtered_image = PictureManager.apply_filter(img)
            stars = Tracking.find_coordinate_of_all_stars(filtered_image)
            self.stars_positions.append(stars)

        for i in range(len(self.stars_positions) - 1):
            associations = StarMatcher.associate_stars(
                self.stars_positions[i], self.stars_positions[i + 1]
            )
            vectors = Tracking.find_vector_of_stars(
                self.stars_positions[i], self.stars_positions[i + 1], associations
            )
            img = PictureManager.load_image(f"generate/picture_{i}.png")
            filtered_image = PictureManager.apply_filter(img)
            image_vectors = PictureManager.display_vectors(filtered_image, vectors)
            PictureManager.save_image(image_vectors, f"output_image_vectors_{i}.png")

    def run(self):
        self.preprocess()
        self.tracking()


if __name__ == "__main__":
    run = Main(sys.argv[1])

    run.run()
