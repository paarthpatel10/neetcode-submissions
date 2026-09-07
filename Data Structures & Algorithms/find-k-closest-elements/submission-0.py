class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        right = left
        left = right - 1

        result = []

        while len(result) < k:
            if left < 0:
                result.append(arr[right])
                right += 1

            elif right >= len(arr):
                result.append(arr[left])
                left -= 1

            elif x - arr[left] <= arr[right] - x:
                result.append(arr[left])
                left -= 1

            else:
                result.append(arr[right])
                right += 1

        return sorted(result)