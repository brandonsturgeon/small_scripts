# http://codegolf.stackexchange.com/questions/112549/bleeeet-bleeeet-bl-bleet/
# 88 bytes

# Begin
import re
s=re.sub
def f(i):print s(r"e\b","t",s("Be","Bl",s(r"\be","B",s("\w","e",i))))
# End

# Test
f("Hello, World!")
