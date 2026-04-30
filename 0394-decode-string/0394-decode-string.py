class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # 1. Get the encoded string
                sub = ""
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop() # pop '['
                
                # 2. Get the number (handle multiple digits)
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                # 3. Push the decoded part back
                stack.append(sub * int(num))
        
        return "".join(stack)
