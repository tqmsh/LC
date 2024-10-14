from math import pow
from typing import List
class Solution:
    def _p_move_failing(self, u: tuple, v: tuple, p: float, q: float):
        r1 = u[0]; c1 = u[1]
        r2 = v[0]; c2 = v[1]
        if abs(r1 - r2) == 1: return p * pow(0.5, min(r1, r2))
        if abs(c1 - c2) == 1: return q * pow(0.5, r1)
        if r1 == r2 and c1 == c2: return 1.0
        return 0.0       

    def _p_move_succeeding(self, u: tuple, v: tuple, p: float, q: float): return 1 - self._p_move_failing(u, v, p, q)
        
    
    def _p_all_flawless(self, students: List[tuple], p: float, q: float):
        ans = 1.0
        for i in range(len(students) - 1): ans *= self._p_move_succeeding(students[i], students[i + 1], p, q)
        return ans
    
    def _p_caught_atleast_once(self, students: List[tuple], p: float, q: float):  return 1 - self._p_all_flawless(students, p, q)
       
students_path = [(0, 0), (1, 0), (2, 0), (2, 1)]  # Vertical movements then one horizontal
p_vertical = 0.6  # Probability of getting caught when passing vertically
q_horizontal = 0.3  # Probability of getting caught when passing horizontally

result = Solution()._p_caught_atleast_once(students_path, p_vertical, q_horizontal)
print(f"Probability of successfully passing the note: {result}")

students_path = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]  # Mostly horizontal, then vertical
p_vertical = 0.7  # Probability of getting caught when passing vertically
q_horizontal = 0.4  # Probability of getting caught when passing horizontally

result = Solution()._p_caught_atleast_once(students_path, p_vertical, q_horizontal)
print(f"Probability of successfully passing the note: {result}")

students_path = [(0, 0), (0, 1), (1, 1), (2, 1)]  # Mixed horizontal and vertical movements
p_vertical = 0.5  # Probability of getting caught when passing vertically
q_horizontal = 0.5  # Probability of getting caught when passing horizontally

result = Solution()._p_caught_atleast_once(students_path, p_vertical, q_horizontal)
print(f"Probability of successfully passing the note: {result}")


students_path = [(2, 2), (2, 3), (3, 3)]  # Horizontal followed by a vertical movement
p_vertical = 0.9  # Probability of getting caught when passing vertically
q_horizontal = 0.2  # Probability of getting caught when passing horizontally

result = Solution()._p_caught_atleast_once(students_path, p_vertical, q_horizontal)
print(f"Probability of successfully passing the note: {result}")