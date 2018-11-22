import re
st="this is raja"
result=re.search(r"raja",st)
print(result)
print(result.group(0))