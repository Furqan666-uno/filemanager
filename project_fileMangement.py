import os

def create_file(filename):
    try:
        with open('filename','x') as f: # x = open the file for writing, but it will give error if the file already exists 
            print(f"File {filename} created successfully.")
    except FileExistsError:
        print(f"File {filename} already exist")
    except Exception as e:
        print("Something went wrong")

def view_all_files():
    files= os.listdir()
    if not files:
        print("No file found")
    else:
        print("Files in directory are: \n")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} has been removed")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Something went wrong")

def read_file(filename):
    try:
        with open('filename','r') as f:
            content=f.read()
            print(f"Content of {filename} is: \n{content}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Something went wrong")

def edit_file(filename):
    try:
        with open('filename','a') as f: # a = overwriting the existing content
            content= input("Enter text you want to add")
            f.write(f"\n {content}")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Something went wrong")

def main():
    while True:
        print("Welcome to file manager")
        print("1.Create File")
        print("2.View All Files")
        print("3.Delete File")
        print("4.Read File")
        print("5.Edit File")
        print("6.Exit")
        choice= input("Enter your choice: ")
        
        if choice=='1':
            filename= input("Enter the name of file you want to create: ")
            create_file(filename)

        elif choice=='2':
            view_all_files()

        elif choice=='3':
            filename= input("Enter the name of file you want to delete: ")
            delete_file(filename)
            
        elif choice=='4':
            filename= input("Enter the name of file you want to read: ")
            delete_file(filename)
         
        elif choice=='5':
            filename= input("Enter the name of file you want to edit: ")
            delete_file(filename)

        elif choice=='6':
            print("Closing the App......")

        else:
            print("Invalid Input")

if __name__=="__main__":
    main()