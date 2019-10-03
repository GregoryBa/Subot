from Chatbots import Chatbots
import tkinter as tk
from ChatbotTTS import ChatbotTTS

HEIGHT = 700
WIDTH = 1000
bot = Chatbots()
tts = ChatbotTTS()

class Main(object):
    user_input = ""
    responses = ""

    def __init__(self, master):
        # Generating the main frame for the GUI
        frame = tk.Frame(master, bg='#ffe6e6', bd=10, cursor='dot')
        frame.pack()

        # Generating a new canvas in the main frame,
        # This is going to be my main working space
        canvas = tk.Canvas(frame, height=HEIGHT, width=WIDTH, bg='#e0e0eb')
        canvas.pack()
        print("Sucessfully generated canvas")
        greeting = 'Hello! My name is Subot. How can I help you today?'
        self.message = tk.Label(frame, font="Calibri, 10", bd=0, justify="left", relief="solid", text=greeting)
        self.message.place(relx=0.05, rely=0.05, relwidth=0.95, relheight=0.4)
        tts.speak(greeting)

        self.train_button = tk.Button(frame, text="TRAIN", command=self.train_chatbot, font="Calibri, 14")
        self.train_button.place(relx=0.85, rely=0.05, relheight=0.1, relwidth=0.15)


        self.message_const = tk.Label(frame, font="Calibri, 30", justify="center", relief="solid", text="Chatbot response:")
        self.message_const.place(relx=0.05, rely=0.05, relwidth=0.8, relheight=0.1)

        self.user_entry = tk.Entry(frame, font=40, bg='#ffffff')
        self.user_entry.place(relx=0.05, rely=0.4, relwidth=0.8, relheight=0.1)

        self.enter_button = tk.Button(frame, text="ENTER", command=self.print_message, font="Calibri, 14")
        self.enter_button.place(relx=0.85, rely=0.4, relheight=0.1, relwidth=0.15)

        self.log_const = tk.Label(frame, font="Calibri, 30", justify="center", relief="solid", text="Info:")
        self.log_const.place(relx=0.05, rely=0.55, relwidth=0.8, relheight=0.1)
        self.log = tk.Label(frame, font="Calibri, 12", bd=0, justify="left", relief="solid")
        self.log.place(relx=0.05, rely=0.65, relwidth=0.8, relheight=0.3)

        self.exit_button = tk.Button(frame, text="EXIT", command=exit, font="Calibri, 14")
        self.exit_button.place(relx=0.85, rely=0.85, relheight=0.1, relwidth=0.15)

        self.label = tk.Label(frame, font="Calibri, 12", text="Accuracy:")
        self.label.place(relx=0.85, rely=0.55, relwidth=0.1, relheight=0.05)
        self.percentage_label = tk.Label(frame, font="Calibri, 12")
        self.percentage_label.place(relx=0.85, rely=0.6, relwidth=0.1, relheight=0.05)


    def train_chatbot(self):
        notif = "Training in progress... Please Wait"
        tts.speak(notif)
        try:
            self.log.config(text=notif)
            bot.train_model()
            notif = "Training completed. Subot is ready for a conversation."
            self.log.config(text=notif)
            tts.speak(notif)
        except:
            error = "Error while training the model. Check if intents.json are in the same directory \n and is in the correct format"
            self.log.config(text=error)
            tts.speak(error)

    def print_message(self):
        global user_input
        global responses
        user_input = self.user_entry.get()
        print("User entry is: " + user_input)
        try:
            response = bot.chat(user_input)
            try:
                self.percentage_label.config(text=bot.get_results_index())
            except:
                self.log.config(text="Couldn't fetch the accuracy's percentage")
            tts.speak(response)
            self.message.config(text=response)
        except:
            error = "Program is not trained. Please go through training process first."
            self.log.config(text=error)
            tts.speak(error)



# Create window
root = tk.Tk()
print("Creating GUI window completed!")

# Create menu
menu = tk.Menu(root)
root.config(menu=menu)

subMenu1 = tk.Menu(menu)
menu.add_cascade(label="File", menu=subMenu1)
subMenu1.add_command(label="New intents...")
subMenu1.add_command(label="Edit intents")

subMenu2 = tk.Menu(menu)
menu.add_cascade(label="Help", menu=subMenu2)
subMenu2.add_command(label="Edit intents")
subMenu2.add_command(label="Edit intents")
root.title("Subot")

c = Main(root)

root.mainloop()
print("Initializing widgets...")