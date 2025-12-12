List = ["apple", "pizza"]
Set={'peach','chips','pizza'}

for i in range(len(List)):
    Set.discard(List[i])

print(Set)