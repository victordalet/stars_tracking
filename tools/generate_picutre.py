import os
import random
from typing import Dict, Tuple

from src.picture_manager import PictureManager
from src.tracking import Tracking

import sys


class GeneratePicture:
    def __init__(self, image_path: str, nb_picture_to_generate: int):
        self.image_path = image_path
        self.nb_picture_to_generate = nb_picture_to_generate

    @staticmethod
    def generate_new_stars(
        stars: Dict[int, Tuple[float, float, float, float]],
        max_random_space=5,
    ) -> Dict[int, Tuple[float, float, float, float]]:
        new_stars = {}
        for key, value in stars.items():
            random_space = random.randint(1, max_random_space)
            random_position = random.choice([1, 2, 3, 4])
            match random_position:
                case 1:
                    new_stars[key] = (
                        value[0] + random_space,
                        value[1] + random_space,
                        value[2],
                        value[3],
                    )
                case 2:
                    new_stars[key] = (
                        value[0] - random_space,
                        value[1] - random_space,
                        value[2],
                        value[3],
                    )
                case 3:
                    new_stars[key] = (
                        value[0],
                        value[1],
                        value[2] + random_space,
                        value[3] + random_space,
                    )
                case 4:
                    new_stars[key] = (
                        value[0],
                        value[1],
                        value[2] - random_space,
                        value[3] - random_space,
                    )
        return new_stars

    def run(self):
        if not os.path.exists("generate"):
            os.makedirs("generate")
        img = PictureManager.load_image(self.image_path)
        filtered_image = PictureManager.apply_filter(img)
        stars = Tracking.find_coordinate_of_all_stars(filtered_image)
        stars = Tracking.remove_false_positive(stars)
        for i in range(self.nb_picture_to_generate):
            stars = self.generate_new_stars(stars)
            new_picture = PictureManager.generate_picture(
                stars, filtered_image.shape[1], filtered_image.shape[0]
            )
            PictureManager.save_image(new_picture, f"generate/picture_{i}.png")


if __name__ == "__main__":
    run = GeneratePicture(sys.argv[1], int(sys.argv[2]))
    run.run()
