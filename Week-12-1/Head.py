# --------------------------------------------------------------
# File:     Week-12-1/Head.py
# Project:  Python-Class-Demos
# Author:   Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Created:  4/05/2021
# Purpose:  Define a Head class that provides the properties
#           and methods to work with a "Head"
#
# --------------------------------------------------------------


# ---------------------------------------------------------------------
# Head Class
# ---------------------------------------------------------------------

class Head:
    """Minifig Head Class

    Properties: colour  string, hex RGBA colour in form #RRGGBBAA
                face    string, eg: smile, scared, frown, cry, etc
                hair    string, eg: hair or hat

    Methods:    getters, setters for properties
                __init__    constructor, instantiate object
                __str__     returns string
    """

    def __init__(self, shape=None, colour=None, face=None, hair=None):
        """
        Head constructor
        :param colour: string
        :param face: string
        :param hair: string
        :param shape: string
        """
        self._colour = colour
        self._face = face
        self._hair = hair
        self._shape = shape

    def __str__(self):
        """
        Convert the 'object' into a human readable string
        :return: string

        TODO: make sure that all properties are shown
        """
        return f"{self._colour} {self._face} face with {self._hair}"

    # We do not need a getter unless you want to use something like
    # current_colour = fig.face.colour()
    @property
    def colour(self):
        """
        Colour of head property
        :return: string
        """
        return self._colour

    @colour.setter
    def colour(self, value):
        """
        Colour of head setter
        :param value: string, Face colour as hex RGBA
        """
        self._colour = value

    @colour.deleter
    def colour(self):
        # TODO: Add PyDoc
        del self._colour

    @property
    def face(self):
        # TODO: Add PyDoc
        return self._face  # indicate "private" using the _

    @face.setter
    def face(self, face):
        # TODO: Add PyDoc
        self._face = face

    @face.deleter
    def face(self):
        # TODO: Add PyDoc
        del self._face

    @property
    def shape(self):
        # TODO: Add PyDoc
        return self._shape  # indicate "private" using the _

    @shape.setter
    def shape(self, shape):
        # TODO: Add PyDoc
        self._shape = shape

    @shape.deleter
    def shape(self):
        # TODO: Add PyDoc
        del self._shape


# ---------------------------------------------------------------------
# Body Class
# ---------------------------------------------------------------------

class Body:
    """
    Define the Minifig Body

    """

    def __init__(self, colour=None, shape=None, pattern=None,
                 accessories=None):
        """
        Construct the minifig body
        """
        if accessories is None:
            accessories = []
        self.shape = shape
        self.pattern = pattern
        self.colour = colour
        self.accessories = accessories

    def __str__(self):
        # TODO: create a proper list of accessories in the form
        # paintbrush and palette --or
        # no accessories -- or
        # boombox -- or
        # basket, fruit, and cane
        return f"{self.colour} {self.shape} body" \
               f" with a {self.pattern} pattern and {self.accessories}"

    @property
    def shape(self):
        # TODO: Add PyDoc
        return self._shape  # indicate "private" using the _

    @shape.setter
    def shape(self, shape):
        # TODO: Add PyDoc
        self._shape = shape

    @shape.deleter
    def shape(self):
        # TODO: Add PyDoc
        del self._shape

    @property
    def colour(self):
        """
        Colour of head property
        :return: string
        """
        return self._colour

    @colour.setter
    def colour(self, value):
        """
        Colour of head setter
        :param value: string, Face colour as hex RGBA
        """
        self._colour = value

    @colour.deleter
    def colour(self):
        # TODO: Add PyDoc
        del self._colour

    @property
    def pattern(self):
        # TODO: Add PyDoc
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        # TODO: Add PyDoc
        self._pattern = value

    @pattern.deleter
    def pattern(self):
        # TODO: Add PyDoc
        del self._pattern

    @property
    def accessories(self):
        # TODO: Add PyDoc
        return self._accessories

    @accessories.setter
    def accessories(self, value):
        # TODO: Add PyDoc
        self._accessories = value

    @accessories.deleter
    def accessories(self):
        # TODO: Add PyDoc
        del self._accessories


class Legs:
    def __init__(self, colour=None, size=None, pattern=None,
                 description=None):
        # TODO: Add PyDoc
        self.colour = None
        self.description = None
        self.pattern = None
        self.size = None  # may be normal, or short

    def __str__(self):
        # TODO: Add PyDoc
        return f"{self.size} {self.description} legs which are" \
               f" {self.colour} with a {self.pattern}"

    @property
    def colour(self):
        """
        Colour of head property
        :return: string
        """
        return self._colour

    @colour.setter
    def colour(self, value):
        """
        Colour of head setter
        :param value: string, Face colour as hex RGBA
        """
        self._colour = value

    @colour.deleter
    def colour(self):
        # TODO: Add PyDoc
        del self._colour

    @property
    def pattern(self):
        # TODO: Add PyDoc
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        # TODO: Add PyDoc
        self._pattern = value

    @pattern.deleter
    def pattern(self):
        # TODO: Add PyDoc
        del self._pattern

    @property
    def size(self):
        # TODO: Add PyDoc
        return self._size

    @size.setter
    def size(self, value):
        # TODO: Add PyDoc
        self._size = value

    @size.deleter
    def size(self):
        # TODO: Add PyDoc
        del self._size

    @property
    def description(self):
        # TODO: Add PyDoc
        return self._description

    @description.setter
    def description(self, value):
        # TODO: Add PyDoc
        self._description = value

    @description.deleter
    def description(self):
        # TODO: Add PyDoc
        del self._description


class MiniFig:
    def __init__(self, name=None):
        """
        Compose the MiniFig of a Head, Body and Legs instance

        TODO: Add more details
        """
        self._head = Head()
        self._body = Body()
        self._legs = Legs()
        self.name = name

    def __str__(self):
        # TODO: Add PyDoc
        return f"The {self.name} MiniFig has a {self.head} on a" \
               f" {self.body} with {self.legs}"

    @property
    def name(self):
        # TODO: Add PyDoc
        return self._name

    @name.setter
    def name(self, name):
        # TODO: Add PyDoc
        self._name = name

    @property
    def head(self):
        # TODO: Add PyDoc
        return self._head

    @head.setter
    def head(self, head):
        # TODO: Add PyDoc
        self._head = head

    @property
    def body(self):
        # TODO: Add PyDoc
        return self._body

    @body.setter
    def body(self, body):
        # TODO: Add PyDoc
        self._body = body

    @property
    def legs(self):
        # TODO: Add PyDoc
        return self._legs

    @legs.setter
    def legs(self, legs):
        # TODO: Add PyDoc
        self._legs = legs


def main():
    print("Testing Head, Body and Legs Classes")
    a_head = Head(shape="standard", colour="red",
                  face="smile", hair=None)
    print(f"Head: {a_head}")

    a_body = Body(colour="blue", shape="standard", pattern="dungarees",
                  accessories=[])
    print(f"Body: {a_body}")

    a_legs = Legs(colour="green", pattern=None)
    print(f"Legs: {a_legs}")

    print("Testing MiniFig Class")
    crash_test_dummy = MiniFig()
    crash_test_dummy.head = a_head
    crash_test_dummy.body = a_body
    crash_test_dummy.legs = a_legs
    print(f"Our dummy: {crash_test_dummy}")

    # Modify the CTD's face and body
    crash_test_dummy.head.face = "scared"
    crash_test_dummy.body.colour = "pink"
    print(f"Modified dummy: {crash_test_dummy}")

    crash_test_dummy.head.shape = "block"
    crash_test_dummy.head.hair = "black ball cap"
    print(f"Modified Head: {crash_test_dummy.head}")

    crash_test_dummy.name = "Crash Test Dummy"
    print(f"Modified dummy: {crash_test_dummy}")


if __name__ == "__main__":
    main()
