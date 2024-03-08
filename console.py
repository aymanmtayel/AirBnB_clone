#!/usr/bin/env python3
#console file
import cmd
import shlex

class AirBnb(cmd.Cmd):
    """simple Airbnb clone console"""

    prompt = "(hbnb) "

    def do_quit(self, person):
        """quit the console"""
        return True

    def do_greet(self, line):
        """A function to greet a person"""
        names = shlex.split(line)
        for name in names:
            print("hi", name)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.calls[:]
        else:
            completions = [f for f in self.calls if f.startswith(text)]
        return completions

    def do_mysum(self, nums):
        total = sum(map(int, shlex.split(nums)))
        print(total)

    def do_EOF(self, line):
        """A function to End the console"""
        return True

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        AirBnb().onecmd(' '.join(sys.argv[1:]))
    else:
        AirBnb().cmdloop()
