#File = open("TextFile.txt", 'r')
#words = File.read()
#words = words.split()
#print(range(words)
#file.close()

file = open("TextFile.txt", 'r')
words = file.read()

# Split the contents into words and count them
word_list = words.split()
word_count = len(word_list)

# Close the file
file.close()

# Print the word count
print(word_count)