import math
from typing import Dict, Tuple


class StarMatcher:
    @staticmethod
    def compute_center(star: Tuple[float, float, float, float]) -> Tuple[float, float]:
        x_center = (star[0] + star[1]) / 2
        y_center = (star[2] + star[3]) / 2
        return x_center, y_center

    @staticmethod
    def euclidean_distance(
        point1: Tuple[float, float], point2: Tuple[float, float]
    ) -> float:
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    @staticmethod
    def associate_stars_methode_2(
        stars_image1: Dict[int, Tuple[float, float, float, float]],
        stars_image2: Dict[int, Tuple[float, float, float, float]],
    ) -> Dict[int, int]:
        associations = {}
        tested_keys_image2 = set()

        for key1, star1 in stars_image1.items():
            center1 = StarMatcher.compute_center(star1)
            min_dist = float("inf")
            best_match_key2 = None

            for key2, star2 in stars_image2.items():
                if key2 in tested_keys_image2:
                    continue

                center2 = StarMatcher.compute_center(star2)
                dist = StarMatcher.euclidean_distance(center1, center2)

                if dist < min_dist:
                    min_dist = dist
                    best_match_key2 = key2

            if best_match_key2 is not None:
                associations[key1] = best_match_key2
                tested_keys_image2.add(best_match_key2)

        return associations

    @staticmethod
    def associate_stars(
        stars_image1: Dict[int, Tuple[float, float, float, float]],
        stars_image2: Dict[int, Tuple[float, float, float, float]],
        max_displacement: float = 5.0,
    ) -> Dict[int, int]:
        associations = {}
        tested_keys_image2 = set()

        for key1, star1 in stars_image1.items():
            center1 = StarMatcher.compute_center(star1)
            best_match_key2 = None
            min_dist = float("inf")

            for key2, star2 in stars_image2.items():
                if key2 in tested_keys_image2:
                    continue

                center2 = StarMatcher.compute_center(star2)

                dx = abs(center1[0] - center2[0])
                dy = abs(center1[1] - center2[1])

                if dx <= max_displacement and dy <= max_displacement:
                    dist = math.hypot(dx, dy)
                    if dist < min_dist:
                        min_dist = dist
                        best_match_key2 = key2

            if best_match_key2 is not None:
                associations[key1] = best_match_key2
                tested_keys_image2.add(best_match_key2)

        return associations
