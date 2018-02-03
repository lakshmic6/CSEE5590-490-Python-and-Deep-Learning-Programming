wordstring =input("Enter a string: ")

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append((w,wordlist.count(w)))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")