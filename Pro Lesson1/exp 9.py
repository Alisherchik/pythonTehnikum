try:
    spammer = (10, 12, 234)
    spammer.append(678)

except AttributeError as error:
    print("Ошибка отрибута - ", error)

except IndentationError:
    print("Ошибка блока")

except TypeError as type_error:
    print("Ошибка типа - ", type_error)

