#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		high = len(S)-1
		low = 0
		while low<high:
		    if S[low]==S[high]:
		        low += 1
		        high -= 1
		    else:
		        return 0
	    return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends