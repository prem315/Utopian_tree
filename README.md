# Utopian_tree

Problem Statement

The Utopian Tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. 
Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

Input Format 
The first line contains an integer, T, the number of test cases. 
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.

Constraints 
1 <= T <= 10 
0 <= N <= 60

Output Format 
For each test case, print the height of the Utopian Tree after N cycles.

Sample Input #00:

2
0
1
Sample Output #00:

1
2
Explanation #00: 
There are 2 test cases. When N = 0, the height of the tree remains unchanged. When N = 1, i.e. after 1st cycle, the tree doubles its height as it's planted at the onset of spring.

Sample Input: #01:

2
4
3
Sample Output: #01:

7
6
Explanation: #01: 
There are 2 testcases.

N = 4:the height of the tree after 4th cycle = 7
N = 3: 
the height of the tree after 1st cycle = 2
the height of the tree after 2nd cycle = 3
the height of the tree after 3rd cycle = 6
