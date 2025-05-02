def permute_string(s: str) -> list[str]:
    """
    Generates all permutations of a given string using backtracking.
    """
    result = []
    n = len(s)
    s_list = list(s) # Convert string to list for easier swapping

    def backtrack(index):
        # Base case: If we've considered all characters, we found a permutation
        if index == n:
            result.append("".join(s_list))
            return

        # Recursive step: Try swapping the character at 'index' with every character
        # from 'index' to the end of the string
        for i in range(index, n):
            # Choose: Swap characters
            s_list[index], s_list[i] = s_list[i], s_list[index]
            
            # Explore: Recurse for the next index
            backtrack(index + 1)

            # Unchoose (Backtrack): Swap back to restore the original order
            # for the next iteration of the loop
            s_list[index], s_list[i] = s_list[i], s_list[index] # Swap back

    backtrack(0) # Start the backtracking process from the first character
    return result

# Example usage:
my_string = "ABC"
permutations = permute_string(my_string)
print(f"Permutations of '{my_string}':")
for p in permutations:
    print(p)

my_string_2 = "12"
permutations_2 = permute_string(my_string_2)
print(f"\nPermutations of '{my_string_2}':")
for p in permutations_2:
    print(p)