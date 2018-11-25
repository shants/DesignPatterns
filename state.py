from abc import ABCMeta, abstractmethod

class IState():
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle(self, context):
        raise NotImplemented("not implemented")

    def work(self, context):
        raise NotImplemented("not implemented")

class State1(IState):
    def handle(self, context):
        self.work()
        # can change state if want to
        #context.set_state()

    def work(self):
        print("State1")

class State2(IState):
    def handle(self, context):
        self.work()
        # context.set_state()

    def work(self):
        print("State2")


class Context():
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def do(self):
        self._state.handle(self)


if __name__ == "__main__":
    c = Context()
    c.set_state(State1())
    c.do()