from itertools import permutations, chain
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = chain.from_iterable(permutations(tiles, r) for r in range(1, len(tiles)+1))
        return len(set(possibilities))