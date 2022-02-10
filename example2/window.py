from server import create_server
from client import create_client

import tkinter


tk = tkinter.Tk()

s = create_server()
sock = create_client()

name = tkinter.StringVar()
text = tkinter.StringVar()

name.set('linux-pc')
text.set('')
tk.title('MonsterChat')
tk.geometry('300x400')

log = tkinter.Text(tk)
nick = tkinter.Entry(tk, textvariable=name)
msg = tkinter.Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand=True)
nick.pack(side='bottom', fill='x', expand=True)
log.pack(side='top', fill='both', expand=True)


def loop_proc():
    log.see(tkinter.END)
    s.setblocking(False)

    try:
        message = s.recv(128).decode()
        log.insert(tkinter.END, message + '\n')

    except BlockingIOError:
        tk.after(1, loop_proc)
        return

    tk.after(1, loop_proc)
    return


def send_proc(event):
    name_r = name.get()
    text_r = text.get()
    sock.sendto(f'{name_r}: {text_r}'.encode('utf-8'), ('255.255.255.255', 11719))
    text.set('')


msg.bind('<Return>', send_proc)
tk.after(1, loop_proc)
tk.mainloop()
