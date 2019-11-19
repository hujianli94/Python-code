#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
from notebook import Note, Notebook


class Menu:
    '''
    display menu and respond to choices when run.
    '''

    def __init__(self):
        self.notebook = Notebook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_memu(self):
        print("""
        Notebook Menu
        
        1.show all notes
        2.search notes
        3.Add Note
        4.Modify Note
        5.Quit
        """)

    def run(self):
        '''display the menu and respond to choice.'''
        while True:
            self.display_memu()
            choice = input("Please Enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} is not valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes()

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_memo(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == '__main__':
    Menu1 = Menu()
    Menu1.run()
