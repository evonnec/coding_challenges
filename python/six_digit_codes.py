"""
Given the max number of 6 digit codes
starting with 000000 and up to 999999
produce a distribution of the number of digits per element, for each element that appears in this universe
000000
000001
000002
expected output:
{1: 0.010%, 2: 2.79%, 3: 6.48%, 4: 32.76%, 5: 45.36%, 6: 15.12%}
solution here needs a multiplication step to produce percentages and not counts.
lucky for us they are just off by a factor of 10+
"""

def produce_distribution():
    keeping_track_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(0, 999999 + 1):
        num_chars = len(set(str(i).zfill(6)))
        keeping_track_dict[num_chars] += 1
	
    return keeping_track_dict
print(produce_distribution())