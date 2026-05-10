#Student mark analyzer

marks = [78, 85, 62, 90, 55]

print("All marks:",marks)
print("First mark:",marks[0])
print("Last marks", marks[-1])
print("First three marks:",marks[:4:])
print("Last two marks:",marks[-2:])

marks.append(88)
print("Marks after adding a new mark:",marks)

marks.insert(2,90)
print("Marks after inserting a mark at index 2:",marks)

marks.remove(62)
print("Marks after removing a mark:",marks)

removed_mark = marks.pop()
print("Removed mark:",removed_mark)
print("Marks after popping the last mark:",marks)

print("Total marks", sum(marks))
print("Average mark:", sum(marks)/len(marks))



print("Highset mark", max(marks))
print("Lowest mark", min(marks))

if 78 in marks:
    print("78 is in the marks list.")
else:
    print("78 is not in the marks list.")

marks.sort()
print("Marks after sorting:",marks)













