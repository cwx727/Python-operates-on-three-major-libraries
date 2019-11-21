from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@192.168.241.130:3306/net_news'
db = SQLAlchemy(app)


class News(db.Model):
	'''创建表'''
	__tablename__ = 'news'
	id = db.Column(db.Integer,primary_key=True) 
	title = db.Column(db.String(200), nullable=False)
	content = db.Column(db.String(2000), nullable=False)
	types = db.Column(db.String(10), nullable=False)
	image = db.Column(db.String(300))
	author = db.Column(db.String(20))
	view_count = db.Column(db.Integer)
	created_at = db.Column(db.DateTime)
	is_valid = db.Column(db.Boolean)

	def __repr__(self):
		return '<News %r>' % self.title

@app.route('/')
def index():
	'''新闻首页'''
	news_list = News.query.all()
	return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>/')
def cat(name):
	'''新闻类别'''
	#查询新闻类别为name的新闻数据
	news_list = News.query.filter(News.types == name)
	return render_template('cat.html', name=name, news_list=news_list)

@app.route('/detail/<int:pk>/')
def detail(pk):
	'''新闻详细信息'''
	new_obj = News.query.get(pk)
	return render_template('detail.html', new_obj=new_obj)


if __name__ == '__main__':
	#db.create_all()  #新建表

	app.run(debug=True)