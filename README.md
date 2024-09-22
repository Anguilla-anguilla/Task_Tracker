# Task Tracker

Simple tool for managing your tasks directly from the command line.

## Installation

*Prerequisites:*
- Python 3.6 or higher

*Clone the Represetory*

```git clone https://github.com/Anguilla-anguilla/Task_Tracker.git```

```cd Task_Tracker```

## Usage

### Adding a task

To add a new task, use the *'add'* command followed by the task description.

``` python task.py add "New task" ```

### Listing tasks

To list all tasks, use the *'list'* command followed by status (*'done'*/*'in-progress'*/*'not-done'*) or *'all'*.

``` python task.py list all ```

``` python task.py list in-progress ```

### Updating task description

To change the description, use the *'update'* command followed by ID and a new task description.

``` python task.py update 3 "New description" ```

### Marking a task

To mark a task, use the *'mark'* command followed by the task ID and new status.

``` python task.py mark 1 done ```

``` python task.py mark 8 in-progress ```

``` python task.py mark 4 not-done ```

### Deleting a task

To delete a task, use the *'delete'* command followed by the task ID.

``` python task.py delete 5 ```

To delete all tasks, use *'clear'* command.

``` python task.py clear ```

[Project URL](https://roadmap.sh/projects/task-tracker)