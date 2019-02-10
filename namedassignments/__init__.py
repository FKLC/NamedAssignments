class NamedAssignments:
    def __call__(self, name, function, *args, **kwargs):
        value = function(*args, **kwargs)
        setattr(NamedAssignments, name, value)
        return value
