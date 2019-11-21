from mongoengine import connect, Document, EmbeddedDocument, DynamicDocument,\
StringField, IntField, FloatField, ListField,EmbeddedDocumentField


connect('students', host='mongodb://192.168.241.130/students')

SEX_CHOICES = (
	('male', '男'),
	('female', '女')
	)

class Grade(EmbeddedDocument):  #EmbeddedDocument嵌套的文档
	''' 成绩 '''
	name = StringField(required=True)
	score = FloatField(required=True)

class Student(DynamicDocument):    #表字段固定用Student(Document)，不固定用DynamicDocument
	'''学生'''
	name = StringField(max_length=32, required=True)
	age = IntField(required=True)
	sex = StringField(choices=SEX_CHOICES, required=True)
	grade = FloatField()
	address = StringField()
	grades = ListField(EmbeddedDocumentField(Grade))

	meta = {
		'collection' : 'students',  #指定collection名
		'ordering' : ['-age']  #排序-age倒序，+age正序
		}  


class TestMongoEngine:

	def add_one(self):
		''' 添加一条数据 '''
		chinese = Grade(name='语文', score=90)
		math = Grade(name='数学',score=100)
		stu_obj = Student(
			name = '张三2',
			age = 15,
			sex = 'male',
			grades = [chinese,math]
		)
		stu_obj.remark = 'remark'   #该字段未在Student中定义
		stu_obj.save()
		return stu_obj

	def get_one(self):
		''' 查询一条数据 '''
		return Student.objects.first()

	def get_more(self):
		''' 查询多条数据 '''
		return Student.objects.all()

	def get_from_oid(self, oid):
		''' 根据ID来获取数据 '''
		return Student.objects.filter(pk=oid).first()

	def update(self):
		''' 修改数据 '''
		#修改多条数据
		#return Student.objects.filter(sex='male').update(inc__age=10)
		#修改一条数据
		return Student.objects.filter(sex='male').update_one(inc__age=10)

	def delete(self):
		''' 删除数据 '''
		#删除一条数据
		#return Student.objects.filter(sex='male').first().delete()
		#删除多条数据
		return Student.objects.filter(sex='male').delete()		


if __name__ == '__main__':
	obj = TestMongoEngine()
	# res = obj.add_one()   #新增一条数据
	# print(res.pk)
	# res = obj.get_one()  #查询一条数据
	# print(res.id)
	# print(res.name)
	# rows = obj.get_more()   #查询多条数据
	# for row in rows:
	# 	print(row.name)
	# res = obj.get_from_oid('5dce376ed64a6544a1f5ef5e') #根据ID来获取数据
	# print(res.id)
	# print(res.name)
	# res = obj.update()  #修改数据
	# print(res)
	res = obj.delete()  #删除数据
	print(res)