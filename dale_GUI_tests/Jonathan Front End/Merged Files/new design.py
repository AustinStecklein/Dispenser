import tkinter as tk


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        #Declare Image Objects
        number1 = tk.PhotoImage(file = 'home.gif')

        #App Container
        number_frame = tk.LabelFrame(self)
        number_frame.place(x = 795, y = 475, anchor = "se", width = 250, height=100)



        number1_button = tk.Button(number_frame, 
                                    #text = "number1", 
                                    image = number1,
                                    background="Red", 
                                    width = 50, 
                                    height = 50)
        number1_button.pack(anchor = "se")








if __name__ == "__main__":
    root = tk.Tk()
    root.title('Dispenser')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    #Sets Size of Program and ensures the Program stays the same height and width
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)

    #End of Program
    root.mainloop()