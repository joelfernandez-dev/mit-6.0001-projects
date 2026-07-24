# Problem Set 4A
# Name: Joel David Fernandez Carrizales
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]

    else:
        firstChar = sequence[:1]
        restOfSequence = sequence[1:]
        restPerms = get_permutations(restOfSequence) #rest Permutations stored in a list

        result = []
        for perms in restPerms:
            for i in range(len(perms)+1):
                newPerm = perms[:i] + firstChar + perms[i:]
                if newPerm not in result:
                    result.append(newPerm)

        return result





if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'aab'
    print('Input:', example_input)
    #print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    


