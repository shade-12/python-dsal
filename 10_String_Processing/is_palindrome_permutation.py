def is_palindrome_permutation(s):
    """
    Determine if a string is a permutation of a palindrome.
    """
    store = dict()
    alpha_count = 0
    for c in s:
        if c.isalpha():
            alpha_count += 1
            if c.lower() in store:
                del store[c.lower()]
            else:
                store[c.lower()] = 1
    
    if alpha_count % 2 == 0:
        return len(store) == 0
    else:
        return len(store) == 1

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palindrome_permutation(palin_perm))
print(is_palindrome_permutation(not_palin_perm))