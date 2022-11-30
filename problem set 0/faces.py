def main():
    faces = input("enter a text with an emoji symbol\n")
    convert(faces)
   
def convert(text):
    message = text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")
    print(message)
                 
main()