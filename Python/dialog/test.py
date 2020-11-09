#!/usr/bin/env python3

import sys
import locale
import time

from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

d = Dialog(dialog="dialog")

button_names = {d.OK:     "OK",
                d.CANCEL: "Cancel",
                d.HELP:   "Help",
                d.EXTRA:  "Extra"}

code, tag = d.menu("Some text that will be displayed above the menu entries",
                   choices=[("Tag 1", "Item text 1"),
                            ("Tag 2", "Item text 2"),
                            ("Tag 3", "Item text 3")])

if code == d.ESC:
    d.msgbox("You got out of the menu by pressing the Escape key.")
else:
    text = "You got out of the menu by choosing the {} button".format(
        button_names[code])

    if code != d.CANCEL:
        text += ", and the highlighted entry at that time had tag {!r}".format(
        tag)

    d.msgbox(text + ".", width=40, height=10)

d.infobox("Bye bye...", width=30, height=10, title="This is the end")
time.sleep(2)

sys.exit(0)
