def print_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent.get(target)

    print(" -> ".join(reversed(path)))
