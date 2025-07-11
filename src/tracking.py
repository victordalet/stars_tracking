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
