"""
File:    lock_and_key.py
Author:  Sushant Sharma
Date:    10/12/2025
Section: 42
E-mail:  ssharm11@umbc.edu
Description:   Checks whether a given key opens a lock by verifying that each key cut and ping and pair adds up to apprx. 6.0
"""
def lock_and_key(key_cuts, lock_pinning, minimum):
    perfect_sum = 6.0

    if len(key_cuts) != len(lock_pinning):
        return False
    
    i = 0 
    while i < len (key_cuts):
        c = key_cuts[i]
        p = lock_pinning[i]
        total = c + p

        if abs(total - perfect_sum) > minimum:
            return False
        
        i += 1

    return True

# test cases 
if lock_and_key([2.1, 3.5, 2.7], [4.1, 2.5, 3.2], 0.25):
   print('Unlocked')
else:
   print('Still Locked')


if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2], 0.25):
   print('Unlocked')
else:
   print('Still Locked')


if lock_and_key([2.1, 3.5, 2.7, 1.7], [4.1, 2.5, 3.2, 3.2], 0.25):
   print('Unlocked')
else:
   print('Still Locked')    