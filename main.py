# Import Standard Libraries

# Import Third-Party Libraries

# Import Local Libraries
from modules.leaders import LeaderPortraits
from modules.loadingscreens import LoadingScreens


class MainProgram:
    def __init__(self) -> None:
        self.path_to_project: str = "/run/media/pawbeans/Project Drive/Projects/Hearts of Iron IV/furs-of-iron/"

    def run(self) -> None:

        #print("Path to Project?")
        #path_to_project = input(">> ")

        print("What do you want to do?")
        print("1. Convert, Resize and Register Leader Portraits")
        print("2. Convert, Resize and Register Loading Screens (WIP)")

        option = input(">> ")

        if option == "1":
            print("Converting, resizing and registering leader portraits...")
            path_to_project = self.path_to_project
            leader_portraits = LeaderPortraits(path_to_project)
            leader_portraits.process_images()

        elif option == "2":
            print("Converting, resizing and registering loading screens...")
            path_to_project = self.path_to_project
            loading_screens = LoadingScreens(path_to_project)
            loading_screens.process_images()

if __name__ == "__main__":
    MainProgram().run()
