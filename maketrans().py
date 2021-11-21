txt = "Hello Sam!"

mytable = txt.maketrans("S", "R")

print(txt.translate(mytable))
#Hello Ram!
