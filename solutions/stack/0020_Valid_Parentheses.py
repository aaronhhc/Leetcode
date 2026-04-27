class Solution:
    def isValid(self, s: str) -> bool:
        #better version
        pairs = { ')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for bracket in s:
            if bracket in pairs:
                if not stack or stack.pop() != pairs[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack #pythonic
        '''
        MY VERSION
        brackets = []
        for br in s:
            if br == '(' or br == '[' or br == '{':
                brackets.append(br)
            elif br == ')':
                if brackets == [] or brackets.pop() != '(':
                    return False
            elif br == ']':
                if brackets == [] or brackets.pop() != '[':
                    return False
            elif br == '}':
                if brackets == [] or brackets.pop() != '{':
                    return False
        return len(brackets) == 0
        '''
