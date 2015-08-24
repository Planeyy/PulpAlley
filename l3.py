def forFunction():
    squares = []
    for x in range(10):
        squares.append(x**2)
        return squares

if __name__ == "__name__":
    import shelve
    with shelve.open("db.shelf", 'c') as f:
        f["first"] = forFunction()
    with shelve.open("db.shelf") as f:
        print(f["first"])