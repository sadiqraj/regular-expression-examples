#using\b
import re
st="iam learning python with naveen sir"
result=re.findall(r"\b\w.",st)
print(result)