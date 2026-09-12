from functools import reduce
from typing import Callable
class Solution:
    def is_operator(self, token: str) -> bool:
        return token in {'+', '-', '/', '*'}
    
    def map_operator(self, token: str) -> Callable[[int, int], int]:
        return {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "/": lambda x,y: int(x / y),
            "*": lambda x,y: x * y,
        }.get(token)


    def evalRPN(self, tokens: List[str]) -> int:
        accumulation = []
        for token in tokens:
            if self.is_operator(token):
                latest = accumulation.pop(-1)
                second_latest = accumulation.pop(-1)
                accumulation.append(reduce(self.map_operator(token), [second_latest, latest]))
            else:
                accumulation.append(int(token))
        return accumulation[-1]