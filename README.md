# 1725. Number Of Rectangles That Can Form The Largest Square

Companies
You are given an array rectangles where rectangles[i] = [li, wi] </br>
represents the ith rectangle of length li and width wi. </br>

You can cut the ith rectangle to form a square with a side length of k if </br>
both k <= li and k <= wi. For example, if you have a rectangle [4,6], </br>
you can cut it to get a square with a side length of at most 4. </br>

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles. </br>

Return the number of rectangles that can make a square with a side length of maxLen. </br>

## Example 1:

Input: rectangles = [[5,8],[3,9],[5,12],[16,5]] </br>
Output: 3 </br>
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5]. </br>
The largest possible square is of length 5, and you can get it out of 3 rectangles. </br>

## Example 2:

Input: rectangles = [[2,3],[3,7],[4,3],[3,7]] </br>
Output: 3 </br>

## Constraints:

1 <= rectangles.length <= 1000 </br>
rectangles[i].length == 2 </br>
1 <= li, wi <= 109 </br>
li != wi </br>
