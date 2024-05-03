import re

def main():
    fhandle = open("file.txt", "r")
    counted_words = {}
    max_name = ''
    max_count = 0

    for line in fhandle:
        words = re.split(r"[.,;\s]\s*", line)
        for word in words:
            if word:
                if word in counted_words.keys():
                    counted_words[word] += 1
                else:
                    counted_words[word] = 1
                if counted_words[word] > max_count:
                    max_name = word
                    max_count = counted_words[word]

    for key, value in counted_words.items():
        print(key, value)

    print('Most repeated word:', max_name)
    print('Number of repeats:', max_count)

    fhandle.close()

main()
