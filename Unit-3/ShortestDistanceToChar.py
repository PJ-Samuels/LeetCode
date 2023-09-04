class Solution:
    def shortestToChar(self, s: str, c: str):
      # Write a recursive function to handle two pointer solution while updating the distance.
      def helper(i, distance):
        # Set the basecase: Out of bound or previous distance away from c was smaller.
        if i < 0 or i > len(s) - 1 or res[i] <= distance:
          return 

        # Set the distance for index and recursively call left and right of index.
        res[i] = distance
        helper(i + 1, distance + 1)
        helper(i - 1, distance + 1)
      
      # Call the recursive function at each point where we find c in string
      res = [len(s) for i in range(len(s))]
      for i, char in enumerate(s):
        if char == c:
          helper(i, 0)
      
      # Return the result
      return res
def main():
  print()
main()