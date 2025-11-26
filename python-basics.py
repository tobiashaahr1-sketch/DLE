# %% opgave 1

print ("hello world")


# %% opgave 2
navn = "Tobias"
alder = 27
temperatur = 21.5
studerende = True
print (f"Mit navn er {navn}, jeg er {alder} år gammel, temperaturen er {temperatur} grader, og det er {studerende}, at jeg er studerende.")

# %% opgave 3
a = float(input("Indtast et tal for a: ")) 
b = float(input("Indtast et tal for b: "))

summen = a+b
forskellen = a - b
produktet = a * b

print ("Summen af a + b = ", summen)
print ("forskellen af a - b =",forskellen)
print ("produktet af a *b", produktet)

if b != 0:
    print("Kvotienten a / b =", a / b)
else:
    print("Kan ikke dividere med 0.")

# Sammenligninger
print("a > b:", a > b)
print("a == b:", a == b)


