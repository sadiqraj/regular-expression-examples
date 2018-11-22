#exact only domine name using"()":
import re
st="sadiq000@gmail.com sadiqraj8282@yahoo.com sadiqrajpython@co.in"
result=re.findall(r"@\w+.\w+",st)
print(result)