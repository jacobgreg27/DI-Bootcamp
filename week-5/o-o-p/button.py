class Button():
    def __init__(self,color,text):
        self.color = color
        self.text = text
    def click(self):
        print("The button was clicked")

submit_button = Button("Blue", "Submit")

submit_button.click(   )