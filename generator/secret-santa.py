import random
import numpy as np
from cryptography.fernet import Fernet

def fernet_key():
    return Fernet.generate_key().decode('utf-8')

def fernet_encrypt(text, key):
	return Fernet(key).encrypt(text.encode('utf-8')).decode('utf-8')


def secret_santa(participants, exclusions):
    N = len(participants)
    A = np.ones((N, N), dtype=int) - np.eye(N, dtype=int)
    for i, j in exclusions:
        A[i][j] = 0

    def assign_santa(assigned, remaining):
        if not remaining:
            return assigned
        
        giver = len(assigned)
        random.shuffle(remaining)
        
        for receiver in remaining:
            if A[giver][receiver]:
                result = assign_santa(assigned + [receiver], [r for r in remaining if r != receiver])
                if result:
                    return result
        
        # Pairing not possible with the given assignments, return None and backtrack
        return None

    # Start algorithm with no assignment and all remaining participants
    solution = assign_santa([], list(range(N)))
    if solution:
        return [(participants[g], participants[r]) for g, r in enumerate(solution)]
    else:
        print("No solution exists with the given exclusions")
        return None


def compute_exclusions(participants, exclusion_map):
    exclusions = []
    for i, p in enumerate(participants):
        if exclusion_map[p]:
            exclusions += [(i, participants.index(x)) for x in exclusion_map[p]]
    return exclusions



participants = ["Alice", "Bob", "Charlie"]
exclusion_map = { "Alice": ["Bob"] }

random.seed(0)
random.shuffle(participants)
exclusions = compute_exclusions(participants, exclusion_map)
solution = secret_santa(participants, exclusions)

key = fernet_key()
if solution:
    print(f'Key:\n{key}\n\n')
    [print(f'{g}\n{fernet_encrypt(r, key)}\n') for (g, r) in solution]
