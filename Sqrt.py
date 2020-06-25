class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        arr = [i for i in str(A)]
        l = len(arr)
        aot = []
        if l%2 == 0:
            for i in range(0,l-1,2):
                aot.append(arr[i]+arr[i+1])
        if l%2 == 1:
            aot.append(int(arr[0]))
            for i in range(1,l-1,2):
                aot.append(arr[i]+arr[i+1])
        ans = ""
        div = 0
        rem = ""
        for i in range(11):
            if i*i>int(aot[0]):
                ans = str(i-1)
                div = 2*(i-1)
                rem = str(int(aot[0])-int(ans)**2)
                break
        for i in range(1,len(aot)):
            for x in range(11):
                if (div*10+x)*x>int(rem+aot[i]):
                    ans = ans + str(x-1)
                    rem = str(int(rem+aot[i])-((div*10+(x-1))*(x-1)))
                    div = div*10+2*(x-1)
                    break
        return ans
