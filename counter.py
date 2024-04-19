words = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design"

counter = {}
for word in words:
    counter[word] = counter.get(word, 0) + 1

result = sorted(counter.items(), key=lambda k: k[1], reverse=True)
print(result)
