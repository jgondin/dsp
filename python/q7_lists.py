# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    for i in words:
        if len(i) >=2 and (i[0]==i[-1]):
            count += 1
    return(count)
    #raise NotImplementedError


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    xpart =[]
    tail = []
    for w in words:
        if w[0] =='x':
            xpart.append(w)
        else:
            tail.append(w)
    xpart.sort()
    tail.sort()

    return(xpart + tail)
    #raise NotImplementedError


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    tmp = tuples
    for i in range(len(tuples)):
        for j in range(i,len(tuples)):
            if tmp[i][1] > tmp[j][1]:
                tmp[i], tmp[j] = tmp[j], tmp[i] 
    
    return(tmp)
    #raise NotImplementedError


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    if len(nums) <1:
        return(nums)

    tmp = nums[1]
    i = 1
    while i < len(nums):
        tmp=nums[i]
        if tmp == nums[i-1]:
            nums.pop(i)
            i -= 1
        i += 1
    return(nums)
    #raise NotImplementedError


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    if list1==[]:
        return(list2)
    elif list2==[]:
        return(list1)
    if list1[0] < list2[0]:
        list = [list1.pop(0)]
        list += linear_merge(list1, list2)
        return(list)
    else:
        list = [list2.pop(0)]
        list += linear_merge(list1, list2)
        return(list) 

            
    #raise NotImplementedError

# match_ends
answer = match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print('Your  answer: %d' % answer)
print('Right answer: 3 \n')

answer = match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print('Your  answer: %d' % answer)
print('Right answer: 2\n')

answer =  match_ends(['aaa', 'be', 'abc', 'hello'])
print('Your  answer: %d' % answer)
print('Right answer: 1\n')

# front_x
print('Your answer:')
print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print('Right answer: \n[\'xaa\', \'xzz\', \'axx\', \'bbb\', \'ccc\']\n')

print('Your answer:')
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print('Right answer: \n[\'xaa\', \'xcc\', \'aaa\', \'bbb\', \'ccc\']\n')

print('Your answer:')
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
print('Right answer: \n[\'xanadu\', \'xyz\', \'aardvark\', \'apple\', \'mix\']\n')

# sort_last
answer = sort_last([(1, 3), (3, 2), (2, 1)])
print('Your answer:')
print(answer)
print('Right answer: \n[(2, 1), (3, 2), (1, 3)]\n')

answer =  sort_last([(2, 3), (1, 2), (3, 1)])
print('Your answer:')
print(answer)
print('Right answer:\n[(3, 1), (1, 2), (2, 3)]\n')

answer = sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
print(answer)
print('Right answer:\n[(2, 2), (1, 3), (3, 4, 5), (1, 7)]\n')
    

#remove_adjacent
answer = remove_adjacent([1, 2, 2, 3])
print('Your answer:')
print(answer)
print('Right answer: \n[1, 2, 3]\n')

answer = remove_adjacent([2, 2, 3, 3, 3])
print('Your answer:')
print(answer)
print('Right answer: \n[2, 3]\n')

answer = remove_adjacent([3, 2, 3, 3, 3])
print('Your answer:')
print(answer)
print('Right answer: \n[3, 2, 3]\n')

answer = remove_adjacent([])
print('Your answer:')
print(answer)
print('Right answer: \n[]')
    
#linear_merge
answer = linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print('Your answer:')
print(answer)
print('Right answer: \n[\'aa\', \'bb\', \'cc\', \'xx\', \'zz\']\n')

answer =  linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print('Your answer:')
print(answer)
print('Right answer: \n[\'aa\', \'bb\', \'cc\', \'xx\', \'zz\']\n')

answer = linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
print('Your answer:')
print(answer)
print('Right answer: \n[\'aa\', \'aa\', \'aa\', \'bb\', \'bb\']')

