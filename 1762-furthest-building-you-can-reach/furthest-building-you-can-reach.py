class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
      def is_reachable(building_index):
          climbs = []
          for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
              if h2 - h1 > 0:
                  climbs.append(h2 - h1)
          climbs.sort()
          bricks_remaining = bricks
          ladders_remaining = ladders
          for climb in climbs:
              if climb <= bricks_remaining:
                  bricks_remaining -= climb
              elif ladders_remaining >= 1:
                  ladders_remaining -= 1
              else:
                  return False
          return True
        
      lo = 0
      hi = len(heights) - 1
      while lo < hi:
          mid = lo + (hi - lo + 1) // 2
          if is_reachable(mid):
              lo = mid
          else:
              hi = mid - 1
      return hi # Note that return lo would be equivalent.       