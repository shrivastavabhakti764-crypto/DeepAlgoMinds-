class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[]
        neg=[]
        p=0
        n=0
        for i in nums:
            if i >0:
                pos.append(i)
            else:
                neg.append(i)
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                ans.append(pos[p])   
                p+=1
            else:
                ans.append(neg[n])
                n+=1 
        return ans                              

