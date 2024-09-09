from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    clear_entry(pass_entry)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]


    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers =  random.randint(2,4)

    password_letters = [random.choice(letters) for items in range(nr_letters)]
    password_symbols=[random.choice(symbols)for items in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for items in range(nr_numbers)]
    pass_list=password_symbols+password_letters+password_numbers

    random.shuffle(pass_list)
    password = ''.join(pass_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_entry(entry_widget):
    entry_widget.delete(0,END)
def clear():
    website_entered = website_entry.get()
    email_entered = email_entry.get()
    password = pass_entry.get()
    new_data={
        website_entered:{
            "email":email_entered,
            "password":password,
        }
    }

    if len(website_entered)==0 or len(password)==0:
        messagebox.showinfo(title="OOOPS!!!!",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as file:
                dt = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            dt.update(new_data)
            with open("data.json", mode='w') as file:
                json.dump(dt,file,indent=4)
        finally:
            clear_entry(website_entry)
            clear_entry(pass_entry)




def search():
    website=website_entry.get()
    try:
        with open("data.json",mode="r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="Data File Does Not Exist.")

    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}                    \nPasssword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #






window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

logo=PhotoImage(file="logo.png")

canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)


website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry=Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"piyushchavhan847@gmail.com")

pass_label=Label(text="Password:",width=21)
pass_label.grid(column=0,row=3)

pass_entry=Entry(width=21)

pass_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",borderwidth=0,highlightthickness=0,width=10,command=gen_pass)
generate_button.grid(column=2,row=3)

search_button=Button(text="Search",borderwidth=1,highlightthickness=0,width=10,command=search)
search_button.grid(column=2,row=1)

add_button=Button(text="Add",borderwidth=0,highlightthickness=0,width=33,command=clear)
add_button.grid(column=1,row=4,columnspan=2)





window.mainloop()