std={}
same={}
for _ in range(int(input())):
        name = input()
        score = float(input())
        std[name]=score

max_grade=0
for grade in std:
    sample=std[name]
    if sample>max_grade:
        max_grade=sample
        max_name=name
print(f"max:{max_grade},name:{max_name}")
min_grade=max_grade

for name in std:
    sample=std[name]
    if sample < min_grade:
        min_grade=sample
        min_name=name


if min_name in std:
     del std[min_name]
min_grade=max_grade

for name in std:
    sample=std[name]
    if sample < min_grade:
        min_grade=sample
        min_name=name
for name in std:
    if std[name]==min_grade:
        same[name]=std[name]
#print(f"min:{min_grade},name:{min_name}")
print(same)        
