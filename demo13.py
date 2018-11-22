#return the first two charecters of each word
import re
st="iam learning python with naveen sir"
result=re.findall(r"\w\w",st)
print(result)