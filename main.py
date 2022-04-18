import string
import random
from random import randint

# alter table to add columns

with open("alterTable.txt", "w") as archivo:
    archivo.write("ALTER TABLE dbo.Course\n")
    archivo.write("ADD C4 VARCHAR(50),\n")
    for i in range(5, 100):
        archivo.write(f"C{i} VARCHAR(50),\n")
    for i in range(100, 200):
        archivo.write(f"C{i} int,\n")
    archivo.write("C200 int;")

ids = [1045, 1050, 2021, 2042, 3141, 4022, 4041]
# update table
with open("update7.txt", "w") as archivo:
    for i in ids:
        archivo.write("UPDATE dbo.Course\n")
        archivo.write("SET ")

        for j in range(4, 100):
            archivo.write(f"C{j} = ")
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")

        for j in range(100, 201):
            archivo.write(f"C{j} = ")
            if j != 200:
                archivo.write(f"{randint(0, 10)}, ")
            else:
                archivo.write(f"{randint(0, 10)}")

        archivo.write(f"\nWHERE CourseID = {i};\n")


# insert into table
with open("insert500_1.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(35000, 35500):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 35499:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_2.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(35500, 36000):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 35999:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_3.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(36000, 36500):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 36499:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_4.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(36500, 36993):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 36992:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_5.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(36993, 37000):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 36999:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_6.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(37000, 37500):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 37499:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_7.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(37500, 38000):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 37999:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_8.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(38000, 38500):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 38499:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_9.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(38500, 39000):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 38999:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_10.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(39000, 39500):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 39499:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("insert500_11.txt", "w") as archivo:
    archivo.write("INSERT INTO dbo.NewCourse(")
    archivo.write("CourseID, Title, Credits, ")
    for i in range(4, 200):
        archivo.write(f"C{i},")
    archivo.write("C200)\n")
    archivo.write("VALUES ")
    for i in range(39500, 39993):
        archivo.write(
            f"({i}, N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', {randint(0, 10)}, ")
        for _ in range(96):
            archivo.write(
                f"N'{''.join(random.choice(string.ascii_letters) for i in range(10))}', ")
        for _ in range(100):
            archivo.write(f"{randint(0, 10)}, ")
        if i != 39992:
            archivo.write(f"{randint(0, 10)}),\n")
        else:
            archivo.write(f"{randint(0, 10)});")

with open("dto.txt", "w") as archivo:
    for i in range(4, 100):
        archivo.write(f"public string C{i} ")
        archivo.write("{ get; set; }\n")
    for j in range(100, 201):
        archivo.write(f"public int C{j} ")
        archivo.write("{ get; set; }\n")
