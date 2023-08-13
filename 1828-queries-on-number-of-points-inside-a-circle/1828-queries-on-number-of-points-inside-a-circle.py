class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result: List[int] = []
        for query in queries:
            # Start the result for the j(th) answer
            result.append(0)
            for point in points:
                # Compute the euclidean distance between points
                dx = point[0] - query[0]
                dy = point[1] - query[1]
                distance = sqrt(dx*dx + dy*dy)
                # Increase result for the j(th) if point is inside the circle
                if distance <= query[2]:
                    result[-1] += 1
        return result