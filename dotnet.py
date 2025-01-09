class Dotnet:
    def __init__(self):
        self.description = [".NET SDK is a tool used to create CLI, Desktop, Game and Web applications", "C# , F# , VB as Programming Language and SQL as database to create"]
        self.basic_command_set = {"create_app" : "dotnet new <TEMPLATE> -n <APP_NAME> [OPTIONS]"}
    def help(self):
        print("- - Type 'Exit' to Quit")
    def get_Command(self,command):
        if command.lower() == "help":
            help()
        if command not in self.basic_command_set.keys():
            print("Not found")

        else:
            print(self.basic_command_set[command])
    


def main():
    dotnet = Dotnet()
    print("------DOTNET TEACHER--------")
    for i in range(3):
        print()
    for elements in dotnet.description:
        print(elements)
    while True:
        command = input("dotnet Quest$$$ ")
        if command.lower() == "exit":
            break
        else:
            dotnet.get_Command(command)

if __name__ == "__main__":
    main()
