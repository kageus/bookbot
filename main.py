import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(len(words))

    char_count = {}
    for word in words:
        for letter in word:
            if letter.lower() in char_count:
                char_count.update({letter.lower(): char_count[letter.lower()] + 1})            
            else:
                if letter.lower() in string.ascii_lowercase: 
                    char_count[letter.lower()] = 1

    sorted_char_count = {}
    sorted_keys = sorted(char_count, key=char_count.get)
    sorted_keys.reverse()
    for w in sorted_keys:
        sorted_char_count[w] = char_count[w]
    

    # begin report
    
    print(f"--- Begin report of {f.name} ---")
    print(f"{len(words)} words found in the document")
    print(f"")

    for key, value in sorted_char_count.items():
        print(f"The {key} character was found {value} times")
    
    print("--- End report ---")