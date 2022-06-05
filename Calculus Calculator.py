from tkinter import *
import math
from fractions import Fraction
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Related Rates Two Step")
root.geometry("800x800")

mb = Menubutton(root, text="Options Menu", bg="black", fg="white")
mb.menu = Menu(mb)  # initilizate the menu than you need to add in the menu button
mb["menu"] = mb.menu
# create a survey pop up
def popup():
    yes_no_option = messagebox.askyesno("Do you like the service?")
    if yes_no_option == False:
        input_box = Toplevel(root)
        input_box.title("Survey")
        new_label = Label(input_box, text="What can we do better? ")
        new_label.grid(row=0,column=0)

        user_response = Entry(input_box)
        user_response.grid(row=1,column=0)
        def response():
            new_response = Label(input_box, text="Thank you! we will try to implement that!")
            new_response.grid(row=3,column=0)
        send = Button(input_box, text="Click When done!", fg="white", bg="blue", command=response)
        send.grid(row=2,column=0)


popupp = Button(root, text="Survey", command=popup, bg="black", fg="yellow")
popupp.grid(row=15,column=0)
# re-size
re_size = Label(root, text="Resize Screen", fg="black", bg="white").grid(row=1,column=4)
vertical = Scale(root, from_=300, to=1500)
vertical.grid(row=1,column=3)
horizontal = Scale(root, from_=300, to=1500, orient=HORIZONTAL)
horizontal.grid(row=2,column=4)
def slide():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
change_button = Button(root, text="Re-Size", command=slide, fg="yellow", bg="blue", relief=SUNKEN, padx=10, pady=10)
change_button.grid(row=3,column=4)

# add commands to the menu4
def derivative():
    top = Toplevel(root)
    top.title("Velocity, Acceleration and Position!")
    first = Label(top, text="Welcome to Velocity, Acceleration and Position Calculator")
    first.grid(row=0, column=0)
    info = Label(top, text="Enter the position below,no number = 0⬇")
    info.grid(row=1, column=0)

    def calculated():
        fourth = int(x4.get())
        third = int(x3.get())
        second = int(x2.get())
        first = int(x1.get())

        empty = []
        empty1 = []
        if (fourth != 0):
            new_val = (fourth * 4)
            derivative = str(new_val) + 't^3 + '
            empty.append(derivative)
            new_val_acceleration = (new_val * 3)
            acceleration_1 = str(new_val_acceleration) + 't^2 + '
            empty1.append(acceleration_1)

        if third != 0:
            second_val = (third * 3)
            derivative1 = str(second_val) + 't^2 + '
            empty.append(derivative1)
            new_val_acceleration2 = (second_val * 2)
            acceleration_2 = str(new_val_acceleration2) + 't + '
            empty1.append(acceleration_2)

        if second != 0:
            third_val = (second * 2)
            derivative2 = str(third_val) + 't + '
            empty.append(derivative2)
            new_val_acceleration3 = (third_val * 1)
            acceleration_3 = str(new_val_acceleration3)
            empty1.append(acceleration_3)

        if first != 0:
            fourth_val = (first * 1)
            derivative3 = str(fourth_val)

            empty.append(derivative3)

        velocity = Label(top, text='Below is Velocity Equation ⬇')
        velocity.grid(row=2, column=1)
        new = Label(top, text="".join(empty))
        new.grid(row=3, column=1)

        acceleration = Label(top, text='Below is Acceleration ⬇')
        acceleration.grid(row=4, column=1)
        a = Label(top, text="".join(empty1))
        a.grid(row=5, column=1)

        def values():
            fourth = int(x4.get())
            third = int(x3.get())
            second = int(x2.get())
            first = int(x1.get())
            const = int(c.get())
            t = int(t_v.get())
            # position
            position = (fourth * (t ** 4)) + (third * (t ** 3)) + (second * (t ** 2)) + (first * t) + const
            position_label = Label(top, text="At t = " + str(t) + ": the answer is " + str(
                position) + " (For Position)").grid(row=9, column=1)

            process = Label(top, text="In order to do derivatives use powerule. ").grid(row=12, column=1)

            process2 = Label(top, text="Multiply the value you wrote in the text box by the exponenet").grid(row=13,
                                                                                                             column=1)

            process3 = Label(top, text="Example: multiply " + str(
                fourth) + " by 4 and then subtract the exponenet by one.").grid(row=14, column=1)

            # Velocity Function
            vel = ((fourth * 4) * (t ** 3)) + ((third * 3) * (t ** 2)) + ((second * 2) * (t ** 1)) + first
            velocity_label = Label(top, text="At t = " + str(t) + ": the answer is " + str(vel) + " (Velocity)").grid(
                row=10, column=1)
            # Acceleration
            acceleration = ((fourth * 4 * 3) * (t ** 2)) + ((third * 3 * 2) + (t)) + second
            acceleration_label = Label(top, text="At t = " + str(t) + ": the answer is " + str(
                acceleration) + " (acceleration)").grid(row=11, column=1)

        vals = Label(top, text="Enter t value given(will solve for all)")
        vals.grid(row=6, column=1)
        t_v = Entry(top)
        t_v.grid(row=7, column=1)

        t_val = Button(top, text="Click once t value is entered", padx=10, pady=10, fg="white", bg="black",
                       command=values)
        t_val.grid(row=8, column=1)

    x_4 = Label(top, text="t^4⬇")
    x_4.grid(row=2, column=0)
    x4 = Entry(top)
    x4.grid(row=3, column=0)

    x_3 = Label(top, text="t^3⬇")
    x_3.grid(row=4, column=0)
    x3 = Entry(top)
    x3.grid(row=5, column=0)

    x_2 = Label(top, text="t^2⬇")
    x_2.grid(row=6, column=0)
    x2 = Entry(top)
    x2.grid(row=7, column=0)

    x_1 = Label(top, text="t⬇")
    x_1.grid(row=8, column=0)
    x1 = Entry(top)
    x1.grid(row=9, column=0)

    constantt = Label(top, text="Constant⬇ ")
    constantt.grid(row=10, column=0)
    c = Entry(top)
    c.grid(row=11, column=0)

    calculate = Button(top, text="Click once done", padx=20, pady=20, bg="black", fg="white", command=calculated)
    calculate.grid(row=12, column=0)


def blank():
    top = Toplevel(root)
    top.title("Optimization Can")
    first = Label(top, text="Optimization of a can (cylindrical) given volume.").grid(row=0, column=0)
    note = Label(top, text="Note: This is for minimum amount needed to construct. Also for finding radius ! ").grid(
        row=1, column=0)

    volume = Label(top, text="Put given volume below (Dont add the pi if pi is in volume⬇) ⬇").grid(row=2, column=0)
    v = Entry(top)
    v.grid(row=3, column=0)

    volume_2 = Label(top,
                     text="Put given volume below(Only put if the volume in the question does not have a pi ⬇)").grid(
        row=6, column=0)
    v2 = Entry(top)
    v2.grid(row=7, column=0)

    def optimization():
        volume = int(v.get())
        step_1 = volume / 2
        optimization = round(step_1 ** (1 / 3), 1)
        new_label = Label(top, text="The answer is: " + str(optimization)).grid(row=5, column=0)

    def optimization2():
        pi = math.pi
        volume = int(v2.get())
        step_0 = volume / pi
        step_1 = step_0 / 2
        optimization3 = round(step_1 ** (1 / 3), 5)
        new_label = Label(top, text="The answer is: " + str(optimization3)).grid(row=9, column=0)

    press = Button(top, text="Press when Complete", bg="black", fg='white', padx=20, pady=10, command=optimization)
    press.grid(row=4, column=0)

    press2 = Button(top, text="Press When Complete", bg="black", fg="white", padx=20, pady=10, command=optimization2)
    press2.grid(row=8, column=0)


def trig():
    top = Toplevel(root)
    top.title("Trig Basic")
    t = Label(top, text="Welcome to Basic Trigonometry").grid(row=0, column=0)

    angle = Label(top, text="Degree to Radians, Degree below ⬇").grid(row=1, column=0)
    a = Entry(top, borderwidth=5)
    a.grid(row=2, column=0)

    fracc = Label(top, text="Radians to Degree, don't add pi ⬇ ").grid(row=0, column=1)

    x = Label(top, text="Numerator ⬇").grid(row=1, column=1)
    n1 = Entry(top)
    n1.grid(row=2, column=1)

    b = Label(top, text="Denominator ⬇ ").grid(row=3, column=1)
    d1 = Entry(top)
    d1.grid(row=4, column=1)

    co = Label(top, text=" Find Coterminal ⬇").grid(row=0,column=2)
    z = Label(top, text="Enter Angle ⬇").grid(row=1,column=2)
    angle_val = Entry(top)
    angle_val.grid(row=2,column=2)
    def angle_to_radians():
        angle = int(a.get())
        decimal = angle / 180
        d = str(decimal)
        f = Fraction(decimal)

        decimal_val = Label(top, text="Answer(Decimal): " + d + "π")
        decimal_val.grid(row=4, column=0)
        fraction_val = Label(top, text="Answer(Fraction): " + str(f) + "π")
        fraction_val.grid(row=5, column=0)

        process = Label(top, text="In order to convert " + str(
            angle) + "° into radians divide by 180 and then multiply by pi.").grid(row=6, column=0)

    def r_d():
        n = int(n1.get())
        d = int(d1.get())

        f = (n * 180) / d
        answer5 = Label(top, text="Answer: " + str(f) + " °").grid(row=6, column=1)

    def view_images(): # pack the view images
        top1 = Toplevel(top)
        top1.title("SohCahToa")
        # initiate images
        soh_cah_toa = ImageTk.PhotoImage(Image.open("Images/SohCahToah.png")) # SohCahToa
        s_c_t = Label(top1, image=soh_cah_toa)
        s_c_t.pack() # three buttons below so columnspan 3

        holder = Button(top1, text="w")
        holder.grid(row=0,column=0)

    def unit_circle(): # pack the unit circle
        top1 = Toplevel(top)
        top1.title("Unit Circle")
        # initiate images
        imagez = ImageTk.PhotoImage(Image.open("Images/UnitCircle.png"))  # SohCahToa
        im = Label(top1, image=imagez)
        im.pack()
        holder = Button(top1, text="w")
        holder.grid(row=0, column=0)

    def triangle(): # pack special right triangle
        top1 = Toplevel(top)
        top1.title("Special Triangle")
        # initiate images
        imagez = ImageTk.PhotoImage(Image.open("Images/SpecialTriangle.png"))  # SohCahToa
        im = Label(top1, image=imagez)
        im.pack()
        holder = Button(top1, text="w")
        holder.grid(row=0, column=0)
    # Coterminal angles
    def coterminal():
        angle_value = int(angle_val.get())
        place_holder = angle_value
        if angle_value < 360 and angle_value >= 0:
            answer = Label(top, text="Answer: " + str(angle_value) + "°")
            answer.grid(row=4, column=2)
        elif angle_value > 360:
            while place_holder > 360:
                place_holder -= 360
            answer = Label(top, text="Answer " + str(place_holder) + "°")
            answer.grid(row=4,column=2)
        elif angle_value < 0:
            while place_holder < 0:
                place_holder += 360
            answer = Label(top, text="Answer " + str(place_holder) + "°")
            answer.grid(row=4, column=2)

        quadrant = ""  # initiate empty variable
        if place_holder >= 0 and place_holder <= 90:  # initiate if else vals for different quadrants
            quadrant += "Quadrant 1"
        elif place_holder > 90 and place_holder <= 180:
            quadrant += "Quadrant 2"
        elif place_holder > 180 and place_holder <= 270:
            quadrant += "Quadrant 3"
        elif place_holder > 270 and place_holder <= 360:
            quadrant += "Quadrant 4"
        # Quadrant label
        quadrant_answer = Label(top, text=quadrant)
        quadrant_answer.grid(row=5,column=2)
    press = Button(top, bg="black", fg="white", text="Press when done", padx=10, pady=10, command=angle_to_radians)
    press.grid(row=3, column=0)
    press2 = Button(top, bg="black", fg="white", text="Press when done", padx=10, pady=10, command=r_d)
    press2.grid(row=5, column=1)
    press3 = Button(top, bg="black", fg="white", text="SohCahToa", padx=10, pady=10, command=view_images)
    press3.grid(row=7, column=0) # SohCahToa
    press4 = Button(top, bg="black", fg="white", text="UnitCircle", padx=10, pady=10, command=unit_circle)
    press4.grid(row=7, column=1) # unit circle
    press5 = Button(top, bg="black", fg="white", text="Triangle", padx=10, pady=10, command=triangle)
    press5.grid(row=7, column=2) # triangle
    press6 = Button(top, bg="black", fg="white", text="Press when Done", padx=10, pady=10, command=coterminal)
    press6.grid(row=3,column=2)
mb.menu.add_command(label="Derivative", command=derivative)
mb.menu.add_command(label="Optimization Can", command=blank)
mb.menu.add_command(label="Trig", command=trig)
mb.grid(row=0, column=0)

myLabel = Label(root, text="Do not put any units")
myLabel.grid(row=0, column=0)

specify = Label(root, text="Find Surface Area of Sphere ⬇")
specify.grid(row=1, column=0)

secify2 = Label(root, text="Finding Surface Area of Cube (change) ⬇ ")
secify2.grid(row=1, column=1)

# velocity derivative
dv_dt = Entry(root)
dv_dt.grid(row=3, column=0)
dv_dt_label = Label(root, text="Enter DV/DT below ⬇")
dv_dt_label.grid(row=2, column=0)

# radius
r_label = Label(root, text="Enter Radius below ⬇")
r_label.grid(row=4, column=0)
r = Entry(root)
r.grid(row=5, column=0)

# instant velocity
instant = Label(root, text="Enter volume of sphere at instant below ⬇ ")
instant.grid(row=6, column=0)
inst = Entry(root)
inst.grid(row=7, column=0)

# area
area = Label(root, text="Enter DV/DT Volume ⬇")
area.grid(row=2, column=1)
a = Entry(root)
a.grid(row=3, column=1)

side = Label(root, text="Enter Side Length ⬇")
side.grid(row=4, column=1)
s = Entry(root)
s.grid(row=5, column=1)

volume = Label(root, text="Enter volume of cube at instant ⬇")
volume.grid(row=6, column=1)
v = Entry(root)
v.grid(row=7, column=1)

quit = Button(root, text="Exit", command=root.quit)
quit.grid(row=13, column=0)


def answer():
    rate = int(dv_dt.get())
    radius = int(r.get())
    pi = math.pi
    dr_dt = rate / ((4 * pi) * (radius ** 2))

    new_label = Label(root, text="The DR/DT = " + str(dr_dt))
    new_label.grid(row=10, column=0)

    final = (((8 * pi) * radius) * (dr_dt))
    answer = Label(root, text="The final answer: " + str(final))
    answer.grid(row=11, column=0)


def answer2():
    pi = math.pi
    rate = int(dv_dt.get())
    volume = int(inst.get())

    holder = volume / ((4 / 3) * pi)
    radius1 = (holder ** (1 / 3))  # unrounded
    radius = round(radius1, 7)

    dr_dt = rate / ((4 * pi) * (radius ** 2))
    final = (((8 * pi) * radius) * (dr_dt))
    answer = Label(root, text="The final answer: " + str(final))
    answer.grid(row=12, column=0)


def answer3():
    dv_dt = int(a.get())
    inst = int(v.get())

    s1 = (inst ** (1 / 3))
    s = round(s1, 7)  # finds the side

    ds_dt1 = (dv_dt / (3 * (s ** 2)))
    ds_dt = round(ds_dt1, 7)

    da_dt = ((12 * s) * ds_dt)
    answer = Label(root, text="The final answer: " + str(da_dt))
    answer.grid(row=12, column=1)


def answer4():
    dv_dt = int(a.get())
    s1 = int(s.get())

    ds_dt1 = (dv_dt / (3 * (s1 ** 2)))
    ds_dt = round(ds_dt1, 7)

    da_dt = ((12 * s1) * ds_dt)

    answer = Label(root, text="The final answer: " + str(da_dt))
    answer.grid(row=12, column=1)


def clicked():
    pi = math.pi

    def ans1():  # note put before
        rad = int(r.get())
        a1 = int(a.get())

        dr_dt1 = a1 / (2 * pi * rad)
        dr_dt = round(dr_dt1, 7)

        c = (2 * pi * dr_dt)

        ans = Label(top, text="The answer is: " + str(c))
        ans.grid(row=10, column=0)
        return

    def ans2():
        pi = math.pi
        da_dt = int(a.get())
        ar = int(a2.get())
        # find radius
        r = ar ** 0.5

        dr_dt1 = da_dt / (2 * pi * r)
        dr_dt = round(dr_dt1, 7)

        # find dc/dt circumfernece
        dc_dt = (2 * pi * dr_dt)

        ans = Label(top, text="The answer is: " + str(dc_dt))
        ans.grid(row=11, column=0)

    def ans3():
        area = int(i.get())  # grab input box data
        da_t = int(da_dt.get())  # DA/ Dt
        side = (area ** 0.5)  # square root

        ds_dt1 = da_t / (2 * side)
        ds_dt = round(ds_dt1, 5)
        dp_dt = ds_dt * 4

    def ans4():
        da_t = int(da_dt.get())
        s = int(side.get())

        ds_dt1 = da_t / (2 * s)
        ds_dt = round(ds_dt1, 7)
        dc_dt = ds_dt * 4
        ans = Label(top, text="The answer is: " + str(dc_dt))
        ans.grid(row=12, column=1)

    top = Toplevel(root)  # add root to work
    # global myLabel
    myLabel = Label(top, text="Do not put any units")
    myLabel.grid(row=0, column=0)
    circumference = Label(top, text="Rate of Change for Circumference(Circle) ⬇ ")
    circumference.grid(row=1, column=0)

    area = Label(top, text="Enter change in Area ⬇ (No, pi just value) ")
    area.grid(row=2, column=0)
    a = Entry(top)
    a.grid(row=3, column=0)

    area2 = Label(top, text="Enter Area at the Time ⬇")
    area2.grid(row=4, column=0)
    a2 = Entry(top)
    a2.grid(row=5, column=0)

    radius = Label(top, text="Enter Radius ⬇")
    radius.grid(row=6, column=0)
    r = Entry(top)
    r.grid(row=7, column=0)

    label2 = Label(top, text="Rate of Change for Perimeter(square) ⬇")
    label2.grid(row=1, column=1)

    rate = Label(top, text="Enter change in Area ⬇")
    rate.grid(row=2, column=1)
    da_dt = Entry(top)
    da_dt.grid(row=3, column=1)

    instz = Label(top, text="Enter Area at the time ⬇")
    instz.grid(row=4, column=1)
    i = Entry(top)
    i.grid(row=5, column=1)

    sd = Label(top, text="Enter side length ⬇")
    sd.grid(row=6, column=1)
    side = Entry(top)
    side.grid(row=7, column=1)

    r_c = Button(top, text="Press given radius + change in Area", command=ans1, padx=20, pady=10, bg="black",
                 fg="white")
    r_c.grid(row=8, column=0)

    a_c = Button(top, text="Press Given Area + Change in Area", padx=20, pady=10, bg="black", fg="white", command=ans2)
    a_c.grid(row=9, column=0)

    a_a = Button(top, text="Press given Area + Change in Area ⬇",
                 padx=20, pady=10, bg="black", fg="white", command=ans3)
    a_a.grid(row=8, column=1)

    c_s = Button(top, text="Press given Change in Area + Side Length ⬇", padx=20, pady=10, bg="black", fg="white",
                 command=ans4)

    c_s.grid(row=9, column=1)


myLabel.grid(row=1, column=0)

click = Button(root,
               text="Click if only given DV/DT and Radius",
               padx=20,
               pady=20,
               command=answer,
               bg="black",
               fg="white")
click.grid(row=8, column=0)

click2 = Button(root,
                text="Click if only given volume at instant and DV/DT",
                padx=20,
                pady=20,
                command=answer2,
                bg="black",
                fg="white")
click2.grid(row=9, column=0)

click3 = Button(root,
                text="Click given instant + DV/DT",
                padx=20,
                pady=20,
                command=answer3,
                bg="black",
                fg="White")
click3.grid(row=8, column=1)

click4 = Button(root,
                text="Click given side + DV/DT ",
                padx=20,
                pady=20,
                command=answer4,
                bg="black",
                fg="white")
click4.grid(row=9, column=1)

click5 = Button(root, text="Click for Related Rates Part 2", command=clicked, bg="blue", fg="Yellow", bd=4)
click5.grid(row=10, column=1)

root.mainloop()