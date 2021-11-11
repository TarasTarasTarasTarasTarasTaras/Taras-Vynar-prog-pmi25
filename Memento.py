class Memento():
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Caretaker():
    def __init__(self):
        self.__snapshots_undo = []
        self.__snapshots_redo = []

    def add_snapshot_undo(self, snapshot: Memento):
        self.__snapshots_undo.append(snapshot)

    def add_snapshot_redo(self, snapshot: Memento):
        self.__snapshots_redo.append(snapshot)

    def get_undo_state(self):
        return self.__snapshots_undo[-1].get_state()

    def get_redo_state(self):
        return self.__snapshots_redo[-1].get_state()

    def pop_snapshot_undo(self):
        return self.__snapshots_undo.pop()

    def pop_snapshot_redo(self):
        return self.__snapshots_redo.pop()

    def size_snapshot_undo(self):
        return len(self.__snapshots_undo)

    def size_snapshot_redo(self):
        return len(self.__snapshots_redo)