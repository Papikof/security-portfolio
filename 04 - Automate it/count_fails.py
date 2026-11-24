with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            words = line.split()
            print(words[10])
        
        