from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import random
from stegano import lsb

#--------------------------------------------------------------------------------------------------
root = Tk()
root.title("CipherPix - Hide Text in Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#1e1e2f")
#--------------------------------------------------------------------------------------------------

def showImage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(), 
        title='Select Image File', 
        filetypes=[("PNG file", "*.png"), ("JPG file", "*.jpg"),("JPEG file", "*.jpeg"), ("All files", "*.*")]
    )
    img = Image.open(filename)
    img = img.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img
#--------------------------------------------------------------------------------------------------

def generate_image_based_on_length(text_length):
    # Define image paths based on length ranges
    animal_images = ["images/i10.jpeg", "images/i11.jpeg", "images/i12.jpeg", "images/i13.jpeg", "images/i14.jpeg", "images/i15.jpeg", "images/i16.jpeg", "images/i17.jpeg", "images/i18.jpeg", "images/i19.jpeg"]
    scenery_images = ["images/j10.jpeg", "images/j11.jpeg", "images/j12.jpeg", "images/j13.jpeg", "images/j14.jpeg", "images/j15.jpeg", "images/j16.jpeg", "images/j17.jpeg", "images/j18.jpeg", "images/j19.jpeg"]
    abstract_images = ["images/k10.jpeg", "images/k11.jpeg", "images/k12.jpeg", "images/k13.jpeg", "images/k14.jpeg", "images/k15.jpeg", "images/k16.jpeg", "images/k17.jpeg", "images/k18.jpeg", "images/k19.jpeg"]
    food_images = ["images/l10.jpeg", "images/l11.jpeg", "images/l12.jpeg", "images/l13.jpeg", "images/l14.jpeg", "images/l15.jpeg", "images/l16.jpeg", "images/l17.jpeg", "images/l18.jpeg", "images/l19.jpeg"]
    space_images = ["images/m10.jpeg", "images/m11.jpeg", "images/m12.jpeg", "images/m13.jpeg", "images/m14.jpeg", "images/m15.jpeg", "images/m16.jpeg", "images/m17.jpeg", "images/m18.jpeg", "images/m19.jpeg"]
    underwater_images = ["images/n10.jpeg", "images/n11.jpeg", "images/n12.jpeg", "images/n13.jpeg", "images/n14.jpeg", "images/n15.jpeg", "images/n16.jpeg", "images/n17.jpeg", "images/n18.jpeg", "images/n19.jpeg"]
    skyscraper_images = ["images/o10.jpeg", "images/o11.jpeg", "images/o12.jpeg", "images/o13.jpeg", "images/o14.jpeg", "images/o15.jpeg", "images/o16.jpeg", "images/o17.jpeg", "images/o18.jpeg", "images/o19.jpeg"]
    patterns_images = ["images/p10.jpeg", "images/p11.jpeg", "images/p12.jpeg", "images/p13.jpeg", "images/p14.jpeg", "images/p15.jpeg", "images/p16.jpeg", "images/p17.jpeg", "images/p18.jpeg", "images/p19.jpeg"]
    cartoon_images = ["images/q10.jpeg", "images/q11.jpeg", "images/q12.jpeg", "images/q13.jpeg", "images/q14.jpeg", "images/q15.jpeg", "images/q16.jpeg", "images/q17.jpeg", "images/q18.jpeg", "images/q19.jpeg"]
    person_images = ["images/r10.jpeg", "images/r11.jpeg", "images/r12.jpeg", "images/r13.jpeg", "images/r14.jpeg", "images/r15.jpeg", "images/r16.jpeg", "images/r17.jpeg", "images/r18.jpeg", "images/r19.jpeg"]
    default_image = random.choice(animal_images + scenery_images + abstract_images + food_images + space_images + underwater_images + skyscraper_images + patterns_images + cartoon_images + person_images)
    
    # Select a random image based on text length
    if text_length <= 2:
        return random.choice(animal_images) if animal_images else default_image
    elif text_length <= 4:
        return random.choice(scenery_images) if scenery_images else default_image
    elif text_length <= 6:
        return random.choice(abstract_images) if abstract_images else default_image
    elif text_length <= 8:
        return random.choice(food_images) if food_images else default_image
    elif text_length <= 10:
        return random.choice(space_images) if space_images else default_image
    elif text_length <= 12:
        return random.choice(underwater_images) if underwater_images else default_image
    elif text_length <= 14:
        return random.choice(skyscraper_images) if skyscraper_images else default_image
    elif text_length <= 16:
        return random.choice(patterns_images) if patterns_images else default_image
    elif text_length <= 18:
        return random.choice(cartoon_images) if cartoon_images else default_image
    elif text_length <= 20:
        return random.choice(person_images) if person_images else default_image
    else:
        return default_image  # Use default image for lengths greater than 20
    
#--------------------------------------------------------------------------------------------------

def update_image_based_on_text(event=None):
    text_length = len(text1.get(1.0, END).strip())
    generated_image_path = generate_image_based_on_length(text_length)
    img = Image.open(generated_image_path)
    img = img.resize((250, 250), Image.LANCZOS)
    img_display = ImageTk.PhotoImage(img)
    lbl.configure(image=img_display, width=250, height=250)
    lbl.image = img_display
#--------------------------------------------------------------------------------------------------

def Hide():
    global secret
    message = text1.get(1.0, END).strip()
    text_length = len(message)
    if text_length == 0:
        notification_label.config(text="Please enter some text!")
        return
    # Generate image path based on text length
    generated_image_path = generate_image_based_on_length(text_length)
    # Hide the message text within the generated image
    secret = lsb.hide(generated_image_path, message)
    # Display notification to the user
    notification_label.config(text="Data hidden successfully! You can now save the image.")
#--------------------------------------------------------------------------------------------------

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)
#--------------------------------------------------------------------------------------------------

def save():
    os.makedirs("secrets_manager", exist_ok=True)
    secret.save("secrets_manager/hidden.png")
    notification_label.config(text="Image saved successfully in secrets_manager folder.")
#--------------------------------------------------------------------------------------------------

# Icon
image_icon = PhotoImage(file="static/logo.png")
root.iconphoto(False, image_icon)
#--------------------------------------------------------------------------------------------------

# Logo and Title
logo = PhotoImage(file="static/logosm.png")
Label(root, image=logo, bg="#1e1e2f").place(x=10, y=0)
Label(root, text="CipherPix", bg="#1e1e2f", fg="white", font="Helvetica 26 bold").place(x=100, y=20)
#--------------------------------------------------------------------------------------------------

# Image Frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=RIDGE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)
#--------------------------------------------------------------------------------------------------

# Text Entry Frame
frame2 = Frame(root, bd=3, bg="#f4f4f9", width=340, height=280, relief=RIDGE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Arial 16", bg="#f4f4f9", fg="#333333", relief=FLAT, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2, command=text1.yview)
scrollbar1.place(x=320, y=0, height=300)
text1.configure(yscrollcommand=scrollbar1.set)

# Bind the text widget to call update_image_based_on_text on every key release
text1.bind("<KeyRelease>", update_image_based_on_text)

# Button Frame for Image Actions
frame3 = Frame(root, bd=3, bg="#1e1e2f", width=330, height=100, relief=RIDGE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="Arial 14 bold", command=showImage, bg="#4CAF50", fg="white", relief=RAISED, activebackground="#45a049").place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="Arial 14 bold", command=save, bg="#4CAF50", fg="white", relief=RAISED, activebackground="#45a049").place(x=180, y=30)
Label(frame3, text="Select Image File", bg="#1e1e2f", fg="#c0c0c0", font="Arial 10 bold").place(x=20, y=5)

# Button Frame for Steganography Actions
frame4 = Frame(root, bd=3, bg="#1e1e2f", width=330, height=100, relief=RIDGE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="Arial 14 bold", command=Hide, bg="#2196F3", fg="white", relief=RAISED, activebackground="#1e88e5").place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="Arial 14 bold", command=Show, bg="#2196F3", fg="white", relief=RAISED, activebackground="#1e88e5").place(x=180, y=30)
Label(frame4, text="Hide or Reveal Text", bg="#1e1e2f", fg="#c0c0c0", font="Arial 10 bold").place(x=20, y=5)

# Notification Label
notification_label = Label(root, text="", bg="#1e1e2f", fg="lightgreen", font="Arial 12 italic")
notification_label.place(x=20, y=470)

root.mainloop()