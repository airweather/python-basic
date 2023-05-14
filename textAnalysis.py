h_fp = open("Hamlet_by_Shakespeare.txt","r")

word_dict = dict()

for line in h_fp.readlines() :
    for word in line.strip().split():
        word = word.strip(" .,;?[]\"\':-").lower()

        if word_dict.get(word) is not None:
            count = word_dict[word]
        else:
            count = 0
        word_dict[word] = count + 1

# sorted() : 키 값으로 정렬
# key와 value값 변경
word_r_dict = {v:k for(k, v) in word_dict.items()}
word_dict = {k:v for(v,k) in sorted(word_r_dict.items(), reverse=True)}

for key in word_dict:
    if word_dict[key] >= 100:
        print("["+key+"]", str(word_dict[key])+ "회")

h_fp.close()