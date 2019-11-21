from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


engine = create_engine('mysql://root:root@192.168.241.130:3306/news_orm')  #获取连接
Base = declarative_base()  #定义基类

Session = sessionmaker(bind=engine)  #定义一个session绑定在engine

class News(Base):
	'''创建表'''
	__tablename__ = 'news'
	id = Column(Integer,primary_key=True) 
	title = Column(String(200), nullable=False)
	content = Column(String(2000), nullable=False)
	types = Column(String(10), nullable=False)
	image = Column(String(300))
	author = Column(String(20))
	view_count = Column(Integer)
	created_at = Column(DateTime)
	is_valid = Column(Boolean)


class OrmTest:
	def __init__(self):
		self.session = Session()

	def add_one(self):
		'''新增记录'''
		new_obj = News(
			title = '标题',
			content = '内容',
			types = '百家',
		)
		self.session.add(new_obj)
		self.session.commit()
		return new_obj

	def get_one(self):
		'''获取一条数据'''
		return self.session.query(News).get(1)

	def get_more(self):
		'''查询多条数据'''
		return self.session.query(News).filter_by(is_valid=True)

	def update_one_data(self, pk):
		'''修改一条数据'''
		new_obj = self.session.query(News).get(pk)
		if new_obj:
			new_obj.is_valid = 0
			self.session.add(new_obj)
			self.session.commit()
			return True
		return False

	def update_more_data(self):
		'''修改多条数据'''
		data_list = self.session.query(News).filter_by(is_valid=True)
		if data_list:
			for item in data_list:
				item.is_valid = 0
				self.session.add(item)
			self.session.commit()
			return True
		return False

	def delete_one_data(self, pk):
		'''删除一条数据'''
		new_obj = self.session.query(News).get(pk)
		self.session.delete(new_obj)
		self.session.commit()

	def delete_more_data(self):
		'''删除一条数据'''
		data_list = self.session.query(News).filter_by(is_valid=True)
		if data_list:
			for item in data_list:
				item.is_valid = 0
				self.session.delete(item)
			self.session.commit()
			return True
		return False

if __name__ == '__main__':
	'''
	news_obj = News()    
	news_obj.metadata.create_all(engine)   #创建表
	'''
	obj = OrmTest()

	#rest = obj.add_one()  #增加表记录
	'''
	rest = obj.get_one()  #查询一条数据
	if rest:
		print('ID:{0}=>{1}'.format(rest.id,rest.title))
	else:
		print('Not exist.')
	'''
	rest = obj.get_more()   #查询多条记录
	print(rest.count())
	for new_obj in rest:
		print('ID:{0}=>{1}'.format(new_obj.id,new_obj.title))

	#obj.update_one_data(2)	#修改一条数据

	#obj.update_more_data()  #修改多条数据

	#obj.delete_one_data(1)
	obj.delete_more_data()
