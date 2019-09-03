from tkinter import *

from common.constants.game_content import game_dict


class generate_windows:
    """
    two windows: login window and match window,client use this two
    """

    def __init__(self):
        pass

    def login_windows(self) -> list:
        """
        this windows for input login info,
        """
        # init frame
        frame = Tk()
        # set title
        frame.title("login")
        # set label
        Label(frame, text="if not fill name and age,server will generate one").grid(row=0, column=1)
        Label(frame, text="id:").grid(row=1, column=0)
        Label(frame, text="name:").grid(row=2, column=0)
        Label(frame, text="url:").grid(row=3, column=0)
        # set StringVar
        stringVar_id = StringVar()
        stringVar_name = StringVar()
        stringVar_url = StringVar()
        stringVar_url.set("gameserver.goodyhao.top")
        # set text
        Entry(frame, width=40, textvariable=stringVar_id).grid(row=1, column=1)
        Entry(frame, width=40, textvariable=stringVar_name).grid(row=2, column=1)
        Entry(frame, width=40, textvariable=stringVar_url).grid(row=3, column=1)
        # set button
        Button(frame, text="ok", width=10, command=lambda: frame.destroy()).grid(row=4, column=0)
        Button(frame, text="cancel", width=10, command=lambda: exit()).grid(row=4, column=1)
        frame.mainloop()
        # get and return info
        user_id = stringVar_id.get()
        name = stringVar_name.get()
        url = stringVar_url.get()
        return [user_id, name, url]

    def match_window(self):
        """
        the window for choose game_id
        """
        # init frame
        frame = Tk()
        # result
        label_intro = Label(frame, text="which one do you want?")
        label_intro.grid(row=0)
        stringvar_id = StringVar()
        label_result = Label(frame, textvariable=stringvar_id)
        label_result.grid(row=1)
        # set title
        frame.title("match")
        # set button
        num = 2
        for game_id in game_dict.keys():
            # set button
            button = Button(frame, text=game_id, width=10, command=lambda: stringvar_id.set(game_id))
            # set position
            button.grid(row=num)
            num += 1

        # set end button
        Button(frame, text="ok", width=10, command=lambda: frame.destroy()).grid(row=num)
        frame.mainloop()
        return stringvar_id.get()
