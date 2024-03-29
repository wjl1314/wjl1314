# coding:utf-8

'''
   学生信息库
'''


class StudentsInfo(object):
    def __init__(self, students):
        self.students = students

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        for id_, value in self.students.items():
            print('学号：{}, 姓名:{}, 年龄:{}, 性别:{}, 班级:{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students

    def add(self, **kwargs):
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return

        id_ = max(students) + 1

        self.students[id_] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'sex': kwargs['sex'],
            'class_number': kwargs['class_number']
        }

    def adds(self, new_student):
        for student in new_student:
            check = self.check_user_info(**student)
            if check != True:
                print(check, student.get('name'))
                continue
            self.add(**student)

    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def delete(self, student_id):
        if student_id not in self.students:
            print('{} 并不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息更新完毕')

    def search_users(self, **kwargs):
        values = list(self.students.values())
        key = None
        value = None
        result = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs['sex']
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            print('没有发现搜索的关键字')
            return

        for user in values:
            if user[key] == value:
                result.append(user)
        return result

    def check_user_info(self, **kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '缺少学生年龄'
        if 'sex' not in kwargs:
            return '缺少学生性别'
        if 'class_number' not in kwargs:
            return '缺少学生班级'
        return True


students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
}

if __name__ == '__main__':
    pass
