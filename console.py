#!/usr/bin/env python3
#console file
import cmd
import shlex

class HelloWorld(cmd.Cmd):
    """simple console11111"""

    calls = ["ayman", "Mahmoud", "Tayel"]
    prompt = "python is fun: "
    intro = "Simple console"

    def do_greet(self, person):
        """A function to greet a person"""

        names = person.split(" ")
        for name in names:
            if name == " ":
                continue
            if name:
                print("hi", name)

    def do_greet2(self, line):
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
        HelloWorld().onecmd(' '.join(sys.argv[1:]))
    else:
        HelloWorld().cmdloop()
