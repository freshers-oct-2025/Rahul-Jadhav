from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        self.completed = False 

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title != "":
            self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if description != "":
            self.__description = description

    @abstractmethod
    def display(self):
        pass

    def get_task(self):
        return {"title": self.__title, "description": self.__description}


class PersonalTask(Task):
    def __init__(self, title, description):
        print("Creating Personal Task...")
        super().__init__(title, description)

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"[Personal] {self.title}: {self.description} [{status}]")


class ProfessionalTask(Task):
    def __init__(self, title, description):
        print("Creating Professional Task...")
        super().__init__(title, description)

    def display(self):
        status = " Completed" if self.completed else " Pending"
        print(f"[Professional] {self.title}: {self.description} [{status}]")


class ToDo:
    def __init__(self):
        self.personal_tasks = []
        self.professional_tasks = []

    def add_task(self, task, category):
        if category == 'personal':
            self.personal_tasks.append(task)
            print(f"Personal task '{task.title}' added successfully!")
        elif category == 'professional':
            self.professional_tasks.append(task)
            print(f"Professional task '{task.title}' added successfully!")

    def remove_task(self, title, category):
        task_list = self.personal_tasks if category == 'personal' else self.professional_tasks
        for task in task_list:
            if task.title == title:
                task_list.remove(task)
                print(f"Task '{title}' removed from {category} list.")
                return
        print("Task not found.")

    def mark_completed(self, title, category):
        task_list = self.personal_tasks if category == 'personal' else self.professional_tasks
        for task in task_list:
            if task.title == title:
                task.completed = True
                print(f"Task '{title}' marked as completed in {category} list!")
                return
        print("Task not found.")

    def clear_all(self, category):
        if category == 'personal':
            self.personal_tasks.clear()
            print("All personal tasks cleared!")
        else:
            self.professional_tasks.clear()
            print("All professional tasks cleared!")

    def show_tasks(self, category=None):
        if category:  
            task_list = self.personal_tasks if category == 'personal' else self.professional_tasks
            if not task_list:
                print(f"No {category} tasks available.")
                return
            print(f"\n--- {category} Tasks ---")
            for i, task in enumerate(task_list, 1):
                print(f"{i}. ", end="")
                task.display()
        else:
            print("\n--- All Tasks ---")
            if not self.personal_tasks and not self.professional_tasks:
                print("No tasks available.")
                return
            if self.personal_tasks:
                print("\nPersonal Tasks:")
                for i, task in enumerate(self.personal_tasks, 1):
                    print(f"{i}. ", end="")
                    task.display()
            else:
                print("\nNo Personal Tasks.")
            if self.professional_tasks:
                print("\nProfessional Tasks:")
                for i, task in enumerate(self.professional_tasks, 1):
                    print(f"{i}. ", end="")
                    task.display()
            else:
                print("\nNo Professional Tasks.")


class Main:
    def main():
        todo = ToDo()

        while True:
            print("\n--- Task Type Menu ---")
            print("1. Personal Task")
            print("2. Professional Task")
            print("3. Show All Task")
            print("4. Exit")
            task_choice = input("Enter your choice: ")

            if task_choice == '1' or task_choice == '2':
                category = 'personal' if task_choice == '1' else 'professional'

                while True:
                    print(f"\n--- {category} Task Menu ---")
                    print("1. Show All Tasks")
                    print("2. Add a Task")
                    print("3. Remove a Task")
                    print("4. Mark Task Completed")
                    print("5. Clear All Tasks")
                    print("6. Go Back")
                    op_choice = input("Enter your choice: ")

                    if op_choice == '1':
                        todo.show_tasks(category)
                    elif op_choice == '2':
                        title = input("Enter Task Title: ")
                        desc = input("Enter Task Description: ")
                        task = PersonalTask(title, desc) if category == 'personal' else ProfessionalTask(title, desc)
                        todo.add_task(task, category)
                    elif op_choice == '3':
                        title = input("Enter task title to remove: ")
                        todo.remove_task(title, category)
                    elif op_choice == '4':
                        title = input("Enter task title to mark complete: ")
                        todo.mark_completed(title, category)
                    elif op_choice == '5':
                        todo.clear_all(category)
                    elif op_choice == '6':
                        break
                    else:
                        print("Invalid choice!")
            
            elif task_choice == '3':
                todo.show_tasks()
            elif task_choice == '4':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Main.main()
