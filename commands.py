# COMMANDS


# building in dictionary
# current resources in dictionary

class Command:
    def do(self):
        raise NotImplementedError

    def cancel(self):
        raise NotImplementedError


class Build(Command):
    #  TODO
    pass


class Destroy(Command):
    #  TODO
    pass


class Collect(Command):
    #  TODO
    pass


class SendWorker(Command):
    #  TODO
    pass

class Research(Command):
    #  TODO
    pass

