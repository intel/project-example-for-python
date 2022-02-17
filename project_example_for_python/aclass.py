class MiscClass:
    @classmethod
    def load(cls1):
        """
        I heard you like classmethods so I put a classmethod in your
        classmethod dawg
        """

        class MyClass:
            @classmethod
            def classception(cls2):
                return type("NewClass", (cls1, cls2,), {"FEED": "FACE"})

        return MyClass
