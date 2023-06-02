# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

name = input("Please enter your name: ")

text = f"""
Hello {name},

I hope this letter finds you well. I will not make it to this years conference, 
due to the rising cost of litteraly everything.
Take care {name}"""

def write_letter(name,text):
    
    print(text)

write_letter(name, text)