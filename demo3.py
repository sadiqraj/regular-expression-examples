#start and end
import re
st="raja is from sathya raja is student of naveen sir"
result=re.match("raja",st)
print(result.end())