"""def cal(x):
    return (x*6)+2

x=int(input("Number = "))
output=cal(x)

print("Answer =", output)
"""
print("ICT GRADE")

"""Functions must include return can be recalled"""

def grade():
    hw=int(input("H/W score: "))
    am=int(input("A/M score: "))
    fe=int(input("F/E score: "))
    if hw + am + fe <= 50:
        x="fail"
    elif hw + am + fe >=150:
        x="Distinction"
    else:
        x="pass"
    return x

sn=["jack","tobi","luke","chris"]
for name in sn:
    print(name)
    fg = grade()
    print(name, fg)