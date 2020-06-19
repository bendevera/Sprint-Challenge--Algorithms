#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n) -> the counter is set to zero at the start of the algorithm. The while loop continues until the counter has been incremented to n^3 and each increment is n^2. A simple example is n = 10. The while loop would continue untill a is >= 10^3 (1000) but is incremented by 10^2 (100) each loop taking it only 10 loops to reach the value 1000. This example shows that the runtime complexity is O(n) and can be solved mathmatically by dividing the target value n^3 by the incrementor n^2 resulting in n.


b) O(n log(n)) -> There is an outer loop with runtime complexity of O(n), inside that loop is a while loop that sets a value (j) to 1 and runs until j is >= n. Within that while loop the j value is multiplied by 2 (doubling the value). Because the nature of doubling 1 until the desired value, it will take log(n) loops of the while loop to reach n. The runtime complexity of the whole algorithm is the product of the outer and inner loop resulting in O(n log(n)).
Example:
n = 8
j = 1

log(n) => 3

(three operations/loops)
j *= 2 -> 2
j *= 2 -> 4
j *= 2 -> 8


c) O(n) -> This recursive function makes a call to itself for all values in the range [0, n] (starting at value n and incrementing by -1 till reaching 0) making it a O(n) runtime complexity. 
Example:
n = 5
bunny(5) = 2 + bunny(4)
bunny(4) = 2 + bunny(3)
bunny(3) = 2 + bunny(2)
bunny(2) = 2 + bunny(1)
bunny(1) = 2 + bunny(0)
bunny(0) = 0

## Exercise II
To be honest this question is poorly phrased but I think I get the gist.

we are given n (some integer of the number of floors in the building) the goal is to find f (the floor at which eggs can be thrown off without breaking). I assume from the lack of instruction there is no given # of eggs. 

def save_eggs(n):
    return helper(n, n)

def helper(num_floors, curr_floor):
    if curr_floor == 0:
        return 0
    success = try_dropping_egg()
    if success:
        return curr_floor
    else:
        return helper(num_floors, curr_floor-1)


This algorithm has a runtime complexity of O(n). In the worst case a call will be maid for each floor in the range [0, n].
