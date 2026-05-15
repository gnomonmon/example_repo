from typing import List


class Stats:
    def mean(self, values: List[float]) -> float:
        if not values:
            raise ValueError("Cannot compute mean of empty list")
        return sum(values) / len(values)

    def median(self, values: List[float]) -> float:
        if not values:
            raise ValueError("Cannot compute median of empty list")
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
        return sorted_vals[mid]

    def variance(self, values: List[float]) -> float:
        if len(values) < 2:
            raise ValueError("Variance requires at least two values")
        m = self.mean(values)
        return sum((x - m) ** 2 for x in values) / (len(values) - 1)

    def std_dev(self, values: List[float]) -> float:
        return self.variance(values) ** 0.5

    def minimum(self, values: List[float]) -> float:
        if not values:
            raise ValueError("Cannot compute minimum of empty list")
        return min(values)

    def maximum(self, values: List[float]) -> float:
        if not values:
            raise ValueError("Cannot compute maximum of empty list")
        return max(values)
