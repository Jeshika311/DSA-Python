class father:
    def show_father_traits(self):
        print("Father Traits:")
        print("- Has great physical and mental strength.")
        print("- Believes in discipline and hard work.")
        print("- Provides valuable life lessons.")
        print("- Always takes responsibility for the family.")
        print("- Can solve complex problems effectively.")

class mother:
    def show_mother_traits(self):
        print("Mother Traits:")
        print("- Always caring and loving.")
        print("- Handles every situation calmly.")
        print("- Manages multiple tasks efficiently.")
        print("- Understands emotions deeply.")
        print("- Always supports and encourages.")

class child(father,mother):
    def show_child_traits(self):
        print("Child Traits: \n")
        print("Father traits + Mother traits")
        self.show_father_traits()
        self.show_mother_traits()

child1 = child()
child1.show_child_traits()