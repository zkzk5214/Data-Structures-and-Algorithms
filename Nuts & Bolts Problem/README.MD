Quick Sort Way: We can use quick sort technique to solve this. 
We represent mason jars and screw top lids in character array for understanding the logic.

MJ represented as array of character
char M[] = {‘@’, ‘#’, ‘$’, ‘%’, ‘^’, ‘&’}

STL represented as array of character
char S[] = {‘$’, ‘%’, ‘&’, ‘^’, ‘@’, ‘#’}

This algorithm first performs a partition by picking last element of S array as pivot, rearrange the array of M and returns the partition index ‘i’ such that all M smaller than M[i] are on the left side and all M greater than M[i] are on the right side. Next using the M[i] we can partition the array of S. Partitioning operations can easily be implemented in O(n). This operation also makes M and S array nicely partitioned. Now we apply this partitioning recursively on the left and right sub-array of M and S.

As we apply partitioning on M and S both so the total time complexity will be Θ(2*nlogn) = Θ(nlogn) on average.

Here for the sake of simplicity we have chosen last element always as pivot. 
We can do randomized quick sort too.
