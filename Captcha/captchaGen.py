import tkinter as tk
from captcha.image import ImageCaptcha
from tkinter.filedialog import asksaveasfilename
from PIL import Image

root = tk.Tk()
root.geometry("350x450")
root.title("Generator")


# function to create the captcha
def generate_captcha():
    global img
    captcha_obj = ImageCaptcha(height=150, width=250)
    captcha_obj.write(chars=captcha_text.get(), output='_captcha.png')

    img = tk.PhotoImage(file='_captcha.png')
    captcha_lb.config(image=img)

# function to save the captcha
def save_captcha():
    file_name = asksaveasfilename(defaultextension=".png")
    if file_name:
        img = Image.open('_captcha.png')
        img.save(file_name)
        img.show(file_name)


main_frame = tk.Frame(root)

# text label
captcha_text_lb = tk.Label(main_frame, text='Gibt den Captcha-text ein', font=('Bold', 12))
captcha_text_lb.pack(pady=10)

# input Field
captcha_text = tk.Entry(main_frame, font=('Bold', 12))
captcha_text.pack(padx=5)

# Button generate
generate_btn = tk.Button(main_frame, text='Generate Captcha', font=('Bold', 15), bg='#1877f2', fg='white',
                         command=generate_captcha)
generate_btn.pack(pady=10, padx=5)

captcha_lb = tk.Label(main_frame)
captcha_lb.place(x=20, y=180)

# Button save
save_btn = tk.Button(main_frame, text='Save Captcha', font=('Bold', 15), bg='#1877f2', fg='white', command=save_captcha)
save_btn.place(x=80, y=380, width=150)

main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(height=450, width=300)

root.mainloop()
