class StudentsDataException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"Data Error: {self.message}"

class BadLine(StudentsDataException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Bad Line: {self.message}"


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"File is empty: {self.message}"


def get_students(filename):
    students = []
    try:
        for line in open(filename, 'rt'):
            if line == '\n':
                raise BadLine
            else:
                student_name = f"{line.split()[0]} {line.split()[1]}"
                if not student_name in students:
                    students.append(student_name)
    except:
        raise FileEmpty
    return students


def get_students_name_points(filename, students):
    students_dict = {}
    for student in students:
        points = 0
        try:
            for line in open(filename, 'rt'):
                student_name = f"{line.split()[0]} {line.split()[1]}"
                if student == student_name:
                    points += float(line.split()[2])
        except:
            raise FileEmpty(f"{filename} is empty")
        students_dict[student] = points
    return students_dict
    

if __name__ == '__main__':
    try:
        while(True):
            filename = input("Enter the file name of the student list or X to exit: ")
            if filename == 'X':
                print('See you next time.')
                break
            else:
                students = sorted(get_students(filename))
                student_dict = get_students_name_points(filename, students)
                for student_info in student_dict.items():
                    print(f"{student_info[0]}\t {student_info[1]}")
    except:
        print("Error reading data from file")
        exit(1)

