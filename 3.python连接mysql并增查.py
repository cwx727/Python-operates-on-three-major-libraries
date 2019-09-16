import pymysql

class MysqlSearch:
	def __init__(self):
		self.get_conn()
		
	def get_conn(self):
		'''连接数据库'''
		try:
			self.conn = pymysql.connect(
				host = '192.168.241.130',
				user = 'root',
				passwd = 'root',
				db = 'news',
				port = 3306,
				charset = 'utf8'
				)

		except pymysql.Error as e:
			print('Error:%s' %e)

	def close_conn(self):
		'''关闭数据库'''
		try:
			if self.conn:
				self.conn.close()

		except pymysql.Error as e:
			print('Error:%s' %e)

	def get_one(self):
		'''查询一条数据'''
		sql = 'SELECT * FROM news WHERE types = %s ORDER BY create_at DESC;'
		cursor = self.conn.cursor()
		cursor.execute(sql, ('百家'))
		rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
		cursor.close()
		self.close_conn()
		return rest

	def get_more(self):
		'''查询全部数据'''
		sql = 'SELECT * FROM news WHERE types = %s ORDER BY create_at DESC;'
		cursor = self.conn.cursor()
		cursor.execute(sql, ('百家'))
		rest = [dict(zip([k[0] for k in cursor.description], row)) 
				for row in cursor.fetchall()]
		cursor.close()
		self.close_conn()
		return rest

	def get_more_by_page(self, page, page_size):
		'''分页查询指定页数的数据'''
		offset = (page-1) * page_size
		sql = 'SELECT * FROM news WHERE types = %s ORDER BY create_at DESC LIMIT %s, %s;'
		cursor = self.conn.cursor()
		cursor.execute(sql, ('百家', offset, page_size))
		rest = [dict(zip([k[0] for k in cursor.description], row)) 
				for row in cursor.fetchall()]
		cursor.close()
		self.close_conn()
		return rest		

	def add_one(self):
		'''添加一条数据'''
		try:
			sql = (
				"INSERT INTO news (title, content, types, is_valid) VALUES"
				"(%s, %s, %s, %s);"
			)
			cursor = self.conn.cursor()
			cursor.execute(sql, ('128核心的CPU跑分有多牛？AMD再创新纪录', '目前民用主流的处理器应该都在四核了，高端一些的达到16核也已经是非常梦幻的配置了。但是对于专业应用来讲，CPU的核心数就好像内存容量一样，永远是多多益善。最近，AMD的双路128核256线程EPYC处理器创造了跑分的新辉煌。', '新闻',1,))
			self.conn.commit()
			cursor.close()
		except:
			print('error')
			self.conn.rollback()
		self.close_conn()




def main():
	obj = MysqlSearch()
	#rest = obj.get_one()
	#print(rest['title'])
	#rest = obj.get_more()
	#print(rest)
	#rest = obj.get_more_by_page(1,1)
	#print(rest)
	obj.add_one()

if __name__ == '__main__':
	main()