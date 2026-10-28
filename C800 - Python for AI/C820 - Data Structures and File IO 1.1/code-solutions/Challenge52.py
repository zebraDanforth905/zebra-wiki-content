tasks = [
    "desk_cleaned", "floor_dirty", "window_cleaned",
    "chair_dirty", "board_cleaned", "door_dirty"
]

dirty = [task for task in tasks if "dirty" in task]
print(dirty)

cleaned = [task.replace("dirty", "cleaned") for task in dirty]
print(cleaned)
