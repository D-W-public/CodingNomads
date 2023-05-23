w =  "blabedi"
solution = ""
for idx in range(len(w)):
    if not idx % 2:
        solution = solution + w[idx].upper()
    else:
        solution = solution + w[idx].lower()
print(solution)