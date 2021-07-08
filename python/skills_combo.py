"""
the problem was given
a group of players with some skill level from 1->1000 in a list called skills , with len(skills) <= 20
minLevel to select (select players with a skill level of more than or equal to minLevel) — positive int
maxLevel to select (select players with a skill level of less than or equal to maxLevel) — positive int (could be up to 1000)
minPlayers a min. number of players to choose from the group skills who fit the criteria (so min up to the len(skills)
provide the total number of combinations of players you can choose.
e.g.
skills = [4, 8, 5, 6] (each int represents a player with that skill level)
minPlayers = 2
minLevel = 7
maxLevel = 8
this should return 0
another example:
skills = [4, 8, 5, 6]
minPlayers = 2
minLevel = 5
maxLevel = 7
this should return 1

combinations formula: to choose p players from m players = C (m, p) = m! / (p! * (m - p)!)

also itertools.combinations takes (iterable, r) which returns r subsequences of elements from input iterable
https://docs.python.org/3/library/itertools.html#itertools.combinations
"""
from itertools import combinations

def num_combinations(
	skills: list,
	minPlayers: int,
	minLevel: int,
	maxLevel: int,
):
	eligible_player_indices = [index for index, skill in enumerate(skills) if maxLevel >= skill >= minLevel]
	result = 0
	for combination_length in range(minPlayers, len(eligible_player_indices) + 1):
		min_player_combinations = combinations(
			iterable=eligible_player_indices,
			r=combination_length,
		)
		combination_list = list(min_player_combinations)
		result += len(combination_list)
	return result

print(num_combinations([4, 8, 5, 6], 2, 7, 8))
assert num_combinations([4, 8, 5, 6], 2, 7, 8) == 0
print(num_combinations([4, 8, 5, 6], 2, 5, 7))
assert num_combinations([4, 8, 5, 6], 2, 5, 7) == 1