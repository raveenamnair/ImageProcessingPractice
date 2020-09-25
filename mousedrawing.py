from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import translate
import image as i
from alphabets import *

canvas_width = 600
canvas_height = 200


def activate_paint(e):
    global lastx, lasty
    c.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(event):
    # color = 'black'
    # x1, y1 = (event.x - 1), (event.y - 1)
    # x2, y2 = (event.x + 1), (event.y + 1)
    # c.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    global lastx, lasty
    x, y = event.x, event.y
    c.create_line((lastx, lasty, x, y), width=5, tag="line")

    draw.line((lastx, lasty, x, y), fill='black', width=5)
    lastx, lasty = x, y


def save():
    filename = "image_trial.png"
    image1.save(filename)
    print("Image got saved")


def clear():
    c.delete("line")


def showresults():
    r = i.starttest("image_trial.png")
    c.create_text(300, 140, text=r, fill="yellow", font=("Arial", 50))


master = Tk()
master.title('Painting in Python')
image = ImageTk.PhotoImage(Image.open('Screen Shot 2020-07-09 at 2.34.54 PM.png'))
l = Label(master, image=image)
l.pack()

c = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
# saving canvas part for image
image1 = Image.new('RGB', (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)

# to make the paper layout
c.create_line(25, 25, 500, 25)
c.create_line(25, 65, 500, 65, dash=(4, 2))
c.create_line(25, 100, 500, 100)
word = translate.getword("leaf")
c.create_text(300, 65, text=word, fill="yellow", font=("utf-8", 100))

# c.pack(expand=YES, fill=BOTH)
# c.bind('<B1-Motion>', paint)
c.bind('<1>', activate_paint)
c.pack(expand=YES, fill=BOTH)

btn_save = Button(text='save', command=save)
btn_save.pack()

btn_results = Button(text='results', command=showresults)
btn_results.pack()
btn_exit = Button(text="exit", command=exit)
btn_exit.pack(side=LEFT)
btn_clear = Button(text="clear", command=clear)
btn_clear.pack()

message = Label(master, text="Press and Drag to draw")
message.pack(side=BOTTOM)
master.mainloop()
