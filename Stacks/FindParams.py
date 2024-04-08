# find open/closed parans, brackets, etc.
def isClosed(s: str) -> bool:
    open_stack = []
    matching = {"(": ")",
            "[": "]",
            "{": "}"}
 
    for c in s:
        if c in matching:
            # if c is an opening bracket, add to open_stack 
            open_stack.append(c)
        else:
            # c is a closing bracket
            
            # if open_stack is empty then return False
            if not open_stack:
                # no open bracket to match 
                return False

            # get the most recent opening bracket
            previous_opening = stack.pop()
            if matching[previous_opening] != c:
                # if closing match in map not equal to current closed 
                return False

    # valid string only if stack is empty
    return not stack

s="{([]){}}"
isClosed(s)
