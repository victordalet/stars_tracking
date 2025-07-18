from typing import Dict, Tuple

import cv2
import numpy as np


class PictureManager:
    @staticmethod
    def load_image(path: str) -> np.ndarray:
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"Image not found at {path}")
        return image

    @staticmethod
    def apply_filter(image: np.ndarray, min_white_detection=80) -> np.ndarray:
        image = cv2.threshold(
            cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
            min_white_detection,
            255,
            cv2.THRESH_BINARY,
        )[1]
        return image

    @staticmethod
    def display_tracking_stars(
        image: np.ndarray, stars: Dict[int, Tuple[float, float, float, float]]
    ) -> np.ndarray:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for i, (x1, x2, y1, y2) in stars.items():
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        return image

    @staticmethod
    def generate_picture(
        stars: Dict[int, Tuple[float, float, float, float]],
        image_w: float,
        image_h: float,
    ) -> np.ndarray:
        image = np.zeros((int(image_h), int(image_w), 3), dtype=np.uint8)
        for x1, x2, y1, y2 in stars.values():
            cv2.rectangle(
                image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), -1
            )
        return image

    @staticmethod
    def display_vectors(
        image: np.ndarray,
        vectors: Dict[int, Tuple[Tuple[float, float], Tuple[float, float]]],
    ) -> np.ndarray:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        for i, (dx, dy) in vectors.items():
            cv2.arrowedLine(
                image,
                (int(dx[0]), int(dx[1])),
                (int(dy[0]), int(dy[1])),
                (255, 0, 0),
                2,
                tipLength=0.1,
            )
        return image

    @staticmethod
    def save_image(image: np.ndarray, path: str) -> None:
        success = cv2.imwrite(path, image)
        if not success:
            raise IOError(f"Failed to save image at {path}")
