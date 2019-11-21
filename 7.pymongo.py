from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId


class TestMongo:
	def __init__(self):
		self.client = MongoClient('mongodb://192.168.241.130:27017')
		self.db = self.client['blog']

	def add_one(self):
		''' 新增数据 '''
		post = {
			'title' : '新的标题',
			'x' : 2,
			'content' : '博客内容...',
			'created_at' : datetime.now()
		}
		return self.db.blog.posts.insert_one(post)   #blog.posts为表名

	def get_one(self):
		''' 查询一条数据 '''
		return self.db.blog.posts.find_one()

	def get_more(self):
		''' 查询多条数据 '''
		return self.db.blog.posts.find({'x':2})  #查询x=2的记录

	def get_one_from_oid(self, oid):
		''' 查询指定ID的数据 '''
		obj = ObjectId(oid)
		return self.db.blog.posts.find_one({'_id': obj})

	def update(self):
		'''修改数据'''
		#修改一条数据
		res = self.db.blog.posts.update_one({'title':'first'}, {'$inc':{'x':3}})
		print(res.matched_count)
		print(res.modified_count)

		#修改多条数据
		res = self.db.blog.posts.update_many({}, {'$inc':{'x':1}})
		print(res.matched_count)
		print(res.modified_count)

	def delete(self):
		'''  删除数据 '''
		#删除一条数据
		res = self.db.blog.posts.delete_one({'title':'first'})
		print(res.deleted_count)
		#删除多条数据
		res = self.db.blog.posts.delete_many({'x':1})
		print(res.deleted_count)


if __name__ == '__main__':
	obj = TestMongo()
	#res = obj.add_one()   #新增数据
	# print(res.inserted_id)
	# res = obj.get_one()  #查询一条数据
	# print(res['_id'])
	# res = obj.get_more()   #查询多条数据
	# for item in res:
	# 	print(item['_id'])
	# res = obj.get_one_from_oid("5dcba0cb8f60d6c62ad1e9e6")  #通过id查询记录
	# print(res)
	#res = obj.update()
	res = obj.delete()

