#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#


# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        from collections import deque

        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        seen = set()
        queue = deque()
        queue.append((sr, sc))

        default_color = image[sr][sc]

        while queue:
            r, c = queue.popleft()

            if (r, c) in seen:
                continue

            image[r][c] = color
            seen.add((r, c))

            if r > 0 and default_color == image[r - 1][c] and (r - 1, c) not in seen:
                queue.append((r - 1, c))
            if (
                r < len(image) - 1
                and default_color == image[r + 1][c]
                and (r + 1, c) not in seen
            ):
                queue.append((r + 1, c))
            if c > 0 and default_color == image[r][c - 1] and (r, c - 1) not in seen:
                queue.append((r, c - 1))
            if (
                c < len(image[0]) - 1
                and default_color == image[r][c + 1]
                and (r, c + 1) not in seen
            ):
                queue.append((r, c + 1))

        return image


# @lc code=end
