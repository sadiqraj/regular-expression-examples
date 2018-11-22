#match

import re
st="raja is here"
result=re.match(r"raja",st)
print(result.group(0))