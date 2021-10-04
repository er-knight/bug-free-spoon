class TodoList:
    def __init__(self) -> None:
        self.todo_ids  = set() # ordered set
        self.todo_list = {}    # { id: title }

    def get_valid_id(self) -> int:
        for i, v in enumerate(self.todo_ids, start=1):
            if i != v:
                return i 

        return len(self.todo_ids) + 1

    def add_todo(self, todo_title: str) -> bool:
        todo_id = self.get_valid_id()
        self.todo_list[todo_id] = todo_title
        self.todo_ids.add(todo_id)

    def show_todos(self) -> None:
        for todo_id in self.todo_ids:
            print(f"[{todo_id}] {self.todo_list[todo_id]}")

    def mark_done(self, todo_id: int) -> bool:
        self.todo_list.pop(todo_id, None)
        self.todo_ids.discard(todo_id)


if __name__ == "__main__":

    todo_list = TodoList()

    todo_list.add_todo("write todo app")
    todo_list.add_todo("take some sleep")
    todo_list.add_todo("call rishab shukla")

    todo_list.show_todos()

    todo_list.mark_done(todo_id=2)
    print("\nmarked 2nd todo as done\n")

    todo_list.show_todos()

    # [1] write todo app
    # [2] take some sleep
    # [3] call rishab shukla

    # marked 2nd todo as done

    # [1] write todo app
    # [3] call rishab shukla
