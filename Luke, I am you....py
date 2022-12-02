"""
Luke Skywalker has family and friends. Help him remind them
who is who. Given a string with a name, return the relation of
that person to Luke.
"""


def i_am_your(member):
    dict_def = {"Darth Vader": "father", "Leia": "sister",
                "Han": "brother in law", "R2D2": "droid"}
    print(f"Luke, i am your {dict_def[member]}")


who = "Darth Vader"
i_am_your(who)
