# link prediction to label
f=open("tf-model/labels.txt", "r")
contents=f.readlines()
f.close()

final_labels = []
for i in range(len(contents)):
    split_line = contents[i].split(" ")
    final_labels.append(split_line)

print(type(final_labels))
print(final_labels[0][1])
