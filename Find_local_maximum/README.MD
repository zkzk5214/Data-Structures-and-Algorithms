## Divide-And-Conquer  

Given an (unsorted) array of numbers in an array, a local maximum is at index i if A[i] is larger than A[i − 1] and A[i + 1]. 
(The last and first elements only need be larger than the previous and next elements respectively.) 
Give an algorithm with running time O(log n) to find a local maximum in an array of length n where no entries are repeated.  

Note: Brief but precise description of the algorithm is required (try less than 6 sentences if you can, but don’t fret if you go over). 

## Solution:  
We have the following  

Observation If we start at ANY element, keep moving to ANY larger adjacent element if there exists one, and stop when all adjacent elements are smaller, 
it is obvious that our path must end at a local maximum. Furthermore, since elements are distinct, the numbers on the path strictly increase, 
so we never visit the same element more than once, which means the path must end at some point.  

Our algorithm first pick the center element A[⌊n/2⌋], and check if it is a local maximum. If it is, output it,
and stop. If it is not, there must exists a larger neighbor. If A[⌊n/2⌋−1] > A[⌊n/2⌋], recursively search for a 
local maximum in A[0,...,⌊n/2⌋−1]. Otherwise, search for a local maximum in A[⌊n/2⌋+1,n−1]. We only look at one half, even when both neighbors are larger. 
At the base case, we have a list of just one element, which will be a local maximum.
  
The algorithm is correct in all cases. When A[⌊n/2⌋] is a local maximum, the algorithm outputs it. If A[⌊n/2⌋]
is not, suppose we are in the case that the algorithm chooses to search A[0, . . . , ⌊n/2⌋−1] (same argument for
the other case). By our ealier observation, there must exists a local maximum in that half 
(consider the path starting with A[⌊n/2⌋] → A[⌊n/2⌋−1], the path must end in that half, thus a local maximum exists there).

 Furthermore, exactly one end of this half list is not an end element of the original list, that is A[⌊n/2⌋−1], but
 we know A[⌊n/2⌋−1]>A[⌊n/2⌋], so if A[⌊n/2⌋−1] is a local maximum in the half list, it is a local maximum in the original list.
   
The running time is O(logn), since we at each level we solve one problem of size n/2, plus constant work
(comparing the middle elements to neighbors). T(n)=T(n/2)+O(1), T(n)=O(log n).
