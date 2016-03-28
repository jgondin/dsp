# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    assert isinstance(count, int) and (count >=0), 'Invalid input!'
    if count >=10:
        return('many')
    
    return(str(count))
    #raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    assert isinstance(s, str), 'Invalid input.'
    if len(s) <= 2:
        return('')
    new_s = s[0:2] + s[-2:]

    return(new_s)
    #raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    new_s = s[0]
    for i in range(1, len(s)):
        if s[i] == new_s[0]:
            new_s += '*'
        else:
            new_s += s[i]

    
    return(new_s) 
    
    #raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    part = a[0:2]
    a = b[0:2] + a[2:]
    b = part + b[2:]
    
    a_b = a + ' ' + b
    return(a_b)

    #raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) <  3:
        return(s)

    if s[-3:]=='ing':
        return(s + 'ly')
    else:
        return(s + 'ing')
            
    #raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """   
    if ('not' not in s) or ('bad' not in s):
        return(s)

    char = ''
    i0 = s.index('not')
    i1 = s.index('bad')
    if i0 > i1:
       return(s)
    
    s = s[:i0] + 'good' + s[(i1 + 3):]
    return(s) 
    #raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    ia = len(a)
    ib = len(b) 
    if ia%2 == 0:
        ia = int(ia / 2)  
    else:
        ia = int(ia / 2 ) + 1
    
    if ib%2 == 0:
        ib = int(ib / 2)
    else:
        ib = int(ib / 2) + 1

    
    a_front = a[:ia]
    b_front = b[:ib]
    a_back = a[ia:]
    b_back = b[ib:]
    
    return(a_front + b_front + a_back + b_back) 
    #raise NotImplementedError

# donuts
print('Your  answer: Number of donuts: %s'  % donuts(4))
print('Right answer: Number of donuts: 4')
print('Your  answer: Number of donuts:  %s' % donuts(9))
print('Right answer: Number of donuts: 9')
print('Your  answer: Number of donuts:  %s' % donuts(10))
print('Right answer: Number of donuts: many')
print('Your  answer: Number of donuts:  %s' % donuts(99))
print('Right answer: Number of donuts: many')
    
# both_ends
print('Your  answer: ' + both_ends('spring'))
print('Right answer: spng')
print('Your  answer: ' + both_ends('Hello'))
print('Right answer: Helo')
print('Your  answer: ' + both_ends('a'))
print('Right answer: ')
print('Your  answer: ' + both_ends('xyz'))
print('Right answer: xyyz')

# fix_start
print('Your  answer: ' + fix_start('babble'))
print('Right answer: ba**le')
print('Your  answer: ' + fix_start('aardvark'))
print('Right answer: a*rdv*rk')
print('Your  answer: ' + fix_start('google'))
print('Right answer: goo*le')
print('Your  answer: ' + fix_start('donut'))
print('Right answer: donut')

# mix_up
print('Your  answer: ' + mix_up('mix', 'pod'))
print('Right answer: pox mid')
print('Your  answer: ' + mix_up('dog', 'dinner'))
print('Right answer: dig donner')
print('Your  answer: ' + mix_up('gnash', 'sport'))
print('Right answer: spash gnort')
print('Your  answer: ' + mix_up('pezzy', 'firm'))
print('Right answer: fizzy perm')

# verbing    
print('Your  answer: ' + verbing('hail'))
print('Right answer: hailing')
print('Your  answer: ' + verbing('swiming'))
print('Right answer: swimingly')
print('Your  answer: ' + verbing('do'))
print('Right answer: do')

# not_bad
print('Your  answer: ' + not_bad('This movie is not so bad'))
print('Right answer: This movie is good')
print('Your  answer: ' + not_bad('This dinner is not that bad!'))
print('Right answer: This dinner is good!')
print('Your  answer: ' + not_bad('This tea is not hot'))
print('Right answer: This tea is not hot')
print('Your  answer: ' + not_bad("It's bad yet not"))
print('Right answer: It\'s bad yet not')

# from_back
print('Your  answer: ' + front_back('abcd', 'xy'))
print('Right answer: abxcdy')
print('Your  answer: ' + front_back('abcde', 'xyz'))
print('Right answer: abcxydez')
print('Your  answer: ' + front_back('Kitten', 'Donut'))
print('Right answer: KitDontenut')

  
