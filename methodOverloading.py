class Parent:

    def call_me(self):
        print("I am the parent")


class Child(Parent):

    def call_me(self):
        print("I am the child")
        super().call_me()
