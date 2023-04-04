from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MyEntry:
    # constructor
    def __init__(self, root):
        # create a frame as child to root window
        self.f = Frame(root, height=750, width=500)

        # let the frame will not shrink
        self.f.propagate(0)

        # attach the frame to root window
        self.f.pack()

        # labels
        self.l1 = Label(text='O₂ (%)')
        self.l2 = Label(text='CO (%)')
        self.l3 = Label(text='CH₄ (%)')
        self.l4 = Label(text='CO₂ (%)')
        self.l5 = Label(text='H₂ (%)')
        self.l6 = Label(text='N₂ (%)')
        self.l12 = Label(text='C₂H₆ (%)')
        self.l13 = Label(text='C₂H₄ (%)')
        self.l7 = Label(text='% Excess N₂')
        self.l8 = Label(text='Effective Inert')
        self.l9 = Label(text='Effective Combustibles')
        self.l10 = Label(text='Total Combustibles')
        self.l11 = Label(text='R')
        self.l14 = Label(text='Count')
        self.l15 = Label(text='Design and Developed by CSIR - CIMFR Dhanbad', fg= "blue")
        self.l16 = Label(text='O₂ = Oxygen')
        self.l17 = Label(text='CO = Carbon Monoxide')
        self.l18 = Label(text='CH₄ = Methane')
        self.l19 = Label(text='CO₂ = Carbon dioxide')
        self.l20 = Label(text='H₂ = Hydrogen')
        self.l21 = Label(text='N₂ = Nitrogen')
        self.l22 = Label(text='C₂H₆ = Ethane')
        self.l23 = Label(text='C₂H₄ = Ethylene')
        self.btn1 = Button(self.f, text="CALCULATE", fg="red")
        self.btn2 = Button(self.f, text="RESET", fg="red", command=self.clear_text)
        self.btn1.bind('<Button-1>', self.calcall)
        self.lbl2 = Label(text="").place(x=260, y=160)
        self.counter = 0

        # list to store values
        self.lst1 = []
        self.lst2 = []
        self.lst3 = []
        self.lst4 = []
        self.lst5 = []
        self.lst6 = []
        self.lst7 = []
        self.lst8 = []
        self.lst9 = []
        self.lst10 = []
        self.lst11 = []
        self.lst12 = []
        self.lst13 = []

        # create entry widget
        self.e1 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e2 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e3 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e4 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e5 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e6 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e7 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e8 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e9 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e10 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e11 = Entry(self.f, width=10, fg='blue', font=('Arial', 14), state='disabled')
        self.e12 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e13 = Entry(self.f, width=10, fg='blue', font=('Arial', 14))
        self.e14 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e15 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e16 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e17 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e18 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e19 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e20 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e21 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e22 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))
        self.e23 = Entry(self.f, width=5, fg='blue', font=('Arial', 10))

        # place the labels and entry widgets

        self.l1.place(x=50, y=30)
        self.l14.place(x=300, y=30)
        self.e14.place(x=350, y=30)
        self.l2.place(x=50, y=60)
        self.l3.place(x=50, y=90)
        self.l4.place(x=50, y=120)
        self.l5.place(x=50, y=150)
        self.l12.place(x=50, y=180)
        self.l13.place(x=50, y=210)
        self.btn1.place(x=90, y=240)
        self.btn2.place(x=190, y=240)
        self.l6.place(x=50, y=280)
        self.l7.place(x=50, y=320)
        self.l8.place(x=50, y=360)
        self.l9.place(x=50, y=400)
        self.l10.place(x=50, y=440)
        self.l11.place(x=50, y=480)
        self.e1.place(x=140, y=30)
        self.e2.place(x=140, y=60)
        self.e3.place(x=140, y=90)
        self.e4.place(x=140, y=120)
        self.e5.place(x=140, y=150)
        self.e12.place(x=140, y=180)
        self.e13.place(x=140, y=210)
        self.e6.place(x=250, y=280)
        self.e7.place(x=250, y=320)
        self.e8.place(x=250, y=360)
        self.e9.place(x=250, y=400)
        self.e10.place(x=250, y=440)
        self.e11.place(x=250, y=480)
        self.l15.place(x=70, y=510)
        self.l16.place(x=50, y=540)
        self.l17.place(x=230, y=540)
        self.l18.place(x=50, y=570)
        self.l19.place(x=230, y=570)
        self.l20.place(x=50, y=600)
        self.l21.place(x=230, y=600)
        self.l22.place(x=50, y=630)
        self.l23.place(x=230, y=630)

    def clear_text(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')
        self.e10.delete(0, 'end')
        self.e11.delete(0, 'end')
        self.e12.delete(0, 'end')
        self.e13.delete(0, 'end')
        self.e14.delete(0, 'end')
        self.counter = 0
        self.lst1.clear()
        self.lst2.clear()
        self.lst3.clear()
        self.lst4.clear()
        self.lst5.clear()
        self.lst6.clear()
        self.lst7.clear()
        self.lst8.clear()
        self.lst9.clear()
        self.lst10.clear()
        self.lst11.clear()
        self.lst12.clear()
        self.lst13.clear()
        plt.close('all')
        self.lbl2 = Label(text="                                                                        ").place(x=260, y=160)

       # self.e14.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e6.configure(state="disabled")
        self.e7.configure(state="disabled")
        self.e8.configure(state="disabled")
        self.e9.configure(state="disabled")
        self.e10.configure(state="disabled")
        self.e11.configure(state="disabled")

    def graph(self, lst1, lst2):
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot(lst1,lst2)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        pass

    def calcall(self, event):
        self.counter += 1
        str1 = self.e1.get()
        str2 = self.e2.get()
        str3 = self.e3.get()
        str4 = self.e4.get()
        str5 = self.e5.get()
        str12 = self.e12.get()
        str13 = self.e13.get()
        str14 = self.e14.get()
        lbl_identify = ''
        i = 0
        try:
            val1 = float(str1)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for O2").place(x=260, y=160)
        try:
            val2 = float(str2)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for CO").place(x=260, y=160)
        try:
            val3 = float(str3)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for CH4").place(x=260, y=160)
        try:
            val4 = float(str4)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for CO2").place(x=260, y=160)
        try:
            val5 = float(str5)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for H2").place(x=260, y=160)

        try:
            val12 = float(str12)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for C2H6").place(x=260, y=160)
        try:
            val13 = float(str13)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter decimal values only for C2H4").place(x=260, y=160)
        try:
            val14 = int(str14)
        except:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="Please Enter Numbers only for Count").place(x=260, y=160)
        if val2 > 3 and val5> 5:
            i = 1
            lbl_identify = 'lbl2'
            self.lbl2 = Label(text="                                                                        ").place(
                x=260, y=160)

            self.lbl2 = Label(text="USBM method is not valid.").place(x=260, y=160)

        def clr_lbl2():
            if lbl_identify !='':
                self.lbl2.destroy()

        if i == 1:
            return False
        else:
            oxy = 100 - (val1 + val2 + val3 + val4 + val5 + val12 + val13)
            ex_nitro = oxy - 3.8 * val1
            eff_inert = ex_nitro + 1.5 * val4
            eff_comb = val3 + 1.25 * val5 + 0.4 * val2 + 0.6 * val12 + 0.54 * val13
            total_comb = val2 + val3 + val5 + val12 + val13
            res = val3/total_comb

            # appending the list
            self.lst1.append(val1)
            self.lst2.append(val2)
            self.lst3.append(val3)
            self.lst4.append(val4)
            self.lst5.append(val5)
            self.lst12.append(val12)
            self.lst13.append(val13)
            self.lst6.append(oxy)
            self.lst7.append(ex_nitro)
            self.lst8.append(eff_inert)
            self.lst9.append(eff_comb)
            self.lst10.append(total_comb)
            self.lst11.append(res)
            self.e6.configure(state="normal")
            self.e7.configure(state="normal")
            self.e8.configure(state="normal")
            self.e9.configure(state="normal")
            self.e10.configure(state="normal")
            self.e11.configure(state="normal")
            self.e6.insert(0, "{:.2f}".format(oxy))
            self.e7.insert(0,"{:.2f}".format(ex_nitro))
            self.e8.insert(0,"{:.2f}".format(eff_inert))
            self.e9.insert(0,"{:.2f}".format(eff_comb))
            self.e10.insert(0,"{:.2f}".format(total_comb))
            self.e11.insert(0,"{:.2f}".format(res))

            if self.counter == val14:
                f, ax = plt.subplots(1)
                stat_lst1 = [0, 10, 20, 30, 40, 50, 60, 66, 62, 40, 10.2, 0]
                stat_lst2 = [5, 5, 5, 5, 5, 5, 5, 5, 9, 13, 18.8, 22.0]
                r1 = [0, 35]
                r2 = [15.3, 5]
                r11 = [35, 88.23]
                r12 = [5, 13.2]
                r3 = [0, 42]
                r4 = [18.5, 5]
                r13 = [42, 90]
                r14 = [5, 11.3]
                r5 = [10.2, 49]
                r6 = [18.8, 5]
                r15 = [49, 91.5]
                r16 = [5, 9.5]
                r7 = [40, 56]
                r8 = [13, 5]
                r17 = [56, 92.5]
                r18 = [5, 8.5]
                r9 = [58.8, 62]
                r10 = [9.55, 5]
                r19 = [62, 93]
                r20 = [5, 7.8]
                r23 = [66, 94]
                r24 = [5, 6.8]
                r21 = [0, 100]
                r22 = [114, 0]
                # r11 = [66, 72.5, 69, 62]
                # r12 = [5, 5, 8, 9]
                self.counter = 0

                plt.plot(stat_lst1, stat_lst2, color='blue', linewidth=2)
                plt.plot(r1, r2, color='green', linestyle='dashed')
                plt.plot(r11, r12, color='green', linestyle='dashed')

                plt.plot(r3, r4, color='green', linestyle='dashed')
                plt.plot(r13, r14, color='green', linestyle='dashed')
                # plt.plot(self.lst8, self.lst9, color='red',  linestyle='dashed', linewidth=2, markersize=12)
                plt.plot(r5, r6, color='green',  linestyle='dashed')
                plt.plot(r15, r16, color='green', linestyle='dashed')
                plt.plot(r7, r8, color='green',  linestyle='dashed')
                plt.plot(r17, r18, color='green', linestyle='dashed')
                plt.plot(r9, r10, color='green',  linestyle='dashed')
                plt.plot(r19, r20, color='green', linestyle='dashed')
                plt.plot(r21, r22, color='black', linewidth=0.5)
                plt.plot(r23, r24, color='green', linestyle='dashed')

                plt.plot(r11, r12, color='green', linestyle='dashed')
                plt.plot(r13, r14, color='green', linestyle='dashed')
                plt.plot(r15, r16, color='green', linestyle='dashed')
                plt.plot(r17, r18, color='green', linestyle='dashed')
                plt.plot(r19, r20, color='green', linestyle='dashed')
                plt.plot(r21, r22, color='black', linewidth=0.5)
                plt.plot(r23, r24, color='green', linestyle='dashed')

                ax.plot(stat_lst1, stat_lst2, linewidth=2)
                ax.plot(r1, r2, color='green', linestyle='dashed')
                ax.plot(r11, r12, color='green', linestyle='dashed')
                ax.plot(r3, r4, color='green',  linestyle='dashed')
                ax.plot(r13, r14, color='green', linestyle='dashed')
                lst_remove_annote = []
                for numc in range(val14):
                    # if lst_remove_annote != []:
                    #     for annot in lst_remove_annote:
                    #         annot.remove()
                    ax.plot(self.lst8[numc], self.lst9[numc], color='red', marker='o', linestyle='dashed', linewidth=2, markersize=8)
                    ann = ax.annotate(numc+1, xy=(self.lst8[numc], self.lst9[numc]), xytext=(self.lst8[numc] + 1, self.lst9[numc]-1))
                               #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
                    lst_remove_annote.append(ann)
                ax.plot(r5, r6, color='green',  linestyle='dashed')
                ax.plot(r15, r16, color='green', linestyle='dashed')
                ax.plot(r7, r8, color='green', linestyle='dashed')
                ax.plot(r17, r18, color='green', linestyle='dashed')
                ax.plot(r9, r10, color='green', linestyle='dashed')
                ax.plot(r19, r20, color='green', linestyle='dashed')
                ax.plot(r21, r22, color='black', linewidth=0.5)
                ax.plot(r23, r24, color='green', linestyle='dashed')

                ax.plot(r11, r12, color='green', linestyle='dashed')
                ax.plot(r13, r14, color='green', linestyle='dashed')
                ax.plot(r15, r16, color='green', linestyle='dashed')
                ax.plot(r17, r18, color='green', linestyle='dashed')
                ax.plot(r19, r20, color='green', linestyle='dashed')
                ax.plot(r21, r22, color='black', linewidth=0.5)
                ax.plot(r23, r24, color='green', linestyle='dashed')

                # inserting textpyinstaller --onefile -w ScriptName.py
                plt.text(3, 8, 'Explosive mixtures', fontsize=12, color='Red')
                plt.text(35, 2, 'Non-explosive mixtures', fontsize=12, color='green')
                plt.text(16, 22, 'Explosive when mixed with air', fontsize=12, color='brown')
                plt.text(82, 22, 'Impossible mixtures', fontsize=10, color='black')
                plt.text(11, 9.5, 'R=1.0', fontsize=7)
                plt.text(18, 10, 'R=0.8', fontsize=7)
                plt.text(25, 11.1, 'R=0.6', fontsize=7)
                plt.text(36, 11, 'R=0.4', fontsize=7)
                plt.text(52, 8.3, 'R=0.2', fontsize=7)
                plt.text(63, 7, 'R=0.0', fontsize=7)
                res2 = "{:.2f}".format(res)

                # plt.plot(self.lst8, self.lst9)
                plt.xlabel('Effective Inert Percent, %')
                # naming the y axis
                plt.ylabel('Effective Combustible Percent, %')

                # giving a title to my graph
                plt.title('USBM Explosibility Diagram')
                # scale_factor = 5

                #ax.xaxis.tick_top()
               # ax.set_xlabel([0,10,20,30,40,50,60,70])
               # ax.xaxis.set_label_position('top')
                ax.set_ylim(0,25)
                ax.set_xlim(0,100)
                # ax.set_ylim(ymin=0)
                plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
                plt.yticks([5,10,15,20,25])
                plt.show()
                    # self.graph(self.lst8, self.lst9)

        # print(str1, str2, str3, str4, str5, self.counter, self.lst1, self.lst8)


# create root window
root = Tk()
root.wm_attributes('-toolwindow', 'True')
root.title(string="                                                              GAS-EXPLO")

# create an object to MyButton class
mb = MyEntry(root)

# the root window handles the mouse click event
root.mainloop()