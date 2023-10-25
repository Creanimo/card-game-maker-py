class FormAskFromDict():
    def __init__(self, formName: str, fieldDict: list[dict[str, str | None | int]]):
        print(formName)
        i = 1
        
        visibleMenu = []
        presetInputs = []

        for field in fieldDict:
            # handle visible fields with a label
            if field["label"]:
                print(str(i) + ": " + str(field["label"]) + " = " + str(field["input"]))
                visibleMenu.append(field)
                i += 1
            if not field["label"]:
                presetInputs.append(field)

        print(len(visibleMenu))

        while True:
            userInput = 0
            try:
                userInput: int = int(input("Make a selection: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
                
            if userInput <= len(visibleMenu):
                break
            else:
                print("Invalid input. Try again.")
                continue


        print(presetInputs)