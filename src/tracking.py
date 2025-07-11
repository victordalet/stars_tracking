from typing import Dict, Tuple

import cv2
import numpy as np


class Tracking:
    @staticmethod
    def find_coordinate_of_all_stars(
        image: np.ndarray,
    ) -> Dict[int, Tuple[float, float, float, float]]:
        contours, _ = cv2.findContours(
            image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        coords_dict = {}
        for i, cnt in enumerate(contours):
            x, y, w, h = cv2.boundingRect(cnt)
            x1, x2 = x, x + w
            y1, y2 = y, y + h
            coords_dict[i] = (x1, x2, y1, y2)

        return coords_dict

    @staticmethod
    def remove_false_positive(
        stars: Dict[int, Tuple[float, float, float, float]], max_air: float = 10
    ) -> Dict[int, Tuple[float, float, float, float]]:
        new_stars = {}
        for key, value in stars.items():
            if value[1] - value[0] < max_air and value[3] - value[2] < max_air:
                new_stars[key] = value
        return new_stars

    @staticmethod
    def find_vector_of_stars(
        stars_image1: Dict[int, Tuple[float, float, float, float]],
        stars_image2: Dict[int, Tuple[float, float, float, float]],
        associations: Dict[int, int],
    ) -> Dict[int, Tuple[Tuple[float, float], Tuple[float, float]]]:
        vectors = {}
        for key1, value1 in stars_image1.items():
            if key1 in associations:
                key2 = associations[key1]
                value2 = stars_image2.get(key2)
                if value2 is not None:
                    x1 = (value1[0] + value1[1]) / 2
                    y1 = (value1[2] + value1[3]) / 2
                    x2 = (value2[0] + value2[1]) / 2
                    y2 = (value2[2] + value2[3]) / 2
                    vectors[key1] = ((x1, y1), (x2, y2))
        return vectors
