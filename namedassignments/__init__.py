class NamedAssignments:
    def __new__(cls, name, function, *args, **kwargs):
        value = function(*args, **kwargs)
        setattr(NamedAssignments, name, value)
        return value
