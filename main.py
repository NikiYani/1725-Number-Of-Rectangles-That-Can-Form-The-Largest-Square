class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sidesSquares = []

        for i in range(0, len(rectangles)) :
            if rectangles[i][0] < rectangles[i][1] :
                sidesSquares.append(rectangles[i][0])
            else :
                sidesSquares.append(rectangles[i][1])

        max = 0
        for el in sidesSquares : 
            if max < el : 
                max = el

        countRes = 0
        for el in sidesSquares :
            if el == max :
                countRes += 1

        return countRes