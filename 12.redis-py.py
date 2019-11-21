import redis

class TestString:
	'''字符串'''

	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.241.130', port=6379,db=0)  #连接数据库

	def test_set(self):
		''' 设置值 '''
		res = self.r.set('user2', 'Amy')
		print(res)
		return res

	def test_get(self):
		''' 查询值 '''
		res = self.r.get('user2')
		print(res)
		return res

	def test_mset(self):
		''' 添加多个值 '''
		d = {'user3':'Bob', 'user4':'Bobx'}
		res = self.r.mset(d)
		print(res)
		return res

	def test_mget(self):
		l = ['user3', 'user4']
		res = self.r.mget(l)
		print(res)
		return res

	def test_del(self):
		''' 删除 '''
		res = self.r.delete('user3')
		print(res)

class TestList:
	'''列表操作'''
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.241.130', port=6379,db=0)  #连接数据库

	def test_push(self):
		'''lpush插入数据'''
		t = ('Amy','Tom2')
		res = self.r.lpush('l_eat',*t)  #不支持tuple，可以加*使t每个值都分别加入res
		print(res)
		t_tuple = ('Jonh','Tom')   
		for t in t_tuple:          
			res = self.r.lpush('l_eat',t)   #循环加入
		res = self.r.lrange('l_eat',0,-1)
		print(res)

	def test_pop(self):
		'''lpop移除'''
		res = self.r.lpop('l_eat')
		print(res)
		res = self.r.lrange('l_eat',0,-1)
		print(res)

class TestSet:
	'''集合'''
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.241.130', port=6379,db=0)  #连接数据库

	def test_sadd(self):
		'''新增'''
		l = ['Cat','Dog']
		res = self.r.sadd('zoo3', *l)
		print(res)
		res = self.r.smembers('zoo3')
		print(res)

	def test_srem(self):
		'''删除'''
		res = self.r.srem('zoo2','Dog')
		print(res)
		res = self.r.smembers('zoo2')
		print(res)

	def test_sinter(self):
		'''交集'''
		res = self.r.sinter('zoo2', 'zoo3')
		print(res)

	def test_sunion(self):
		'''并集'''
		res = self.r.sunion('zoo2', 'zoo3')
		print(res)



if __name__ == '__main__':
	'''字符串'''
	#obj = TestString()   
	#obj.test_set()
	#obj.test_get()
	#obj.test_mset()
	#obj.test_mget()
	#obj.test_del()

	'''列表'''
	#obj = TestList()
	#obj.test_push()
	#obj.test_pop()

	'''集合'''
	obj = TestSet()
	#obj.test_sadd()
	#obj.test_srem()
	#obj.test_sinter()
	obj.test_sunion()