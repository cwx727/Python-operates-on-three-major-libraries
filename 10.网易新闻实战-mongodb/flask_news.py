from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form

from datetime import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo_news',
    'host': '192.168.241.130',
    'port': 27017
	}
db = MongoEngine(app)


NEWS_TYPES = (
	('推荐','推荐'),
	('百家','百家'),
	('本地','本地'),
	('图片','图片')
	)

class News(db.Document):
	'''新闻模型'''
	title = db.StringField(required=True, max_length=200)
	content = db.StringField(required=True, choice=NEWS_TYPES)
	news_type = db.StringField(required=True)
	img_url = db.StringField()
	is_valid = db.BooleanField(default=True)
	created_at = db.DateTimeField(default=datetime.now())
	updated_at = db.DateTimeField(default=datetime.now())

	meta = {
		'collection':'news',
		'ordering':['-created_at']
	}

@app.route('/')
def index():
	news_list = News.objects.filter(is_valid=True)
	return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>')
def cat(name):
	news_list = News.objects.filter(is_valid=True, news_type=name)
	return render_template('cat.html', news_list=news_list)

@app.route('/detail/<pk>')
def detail(pk):
	new_obj = News.objects.filter(pk=pk).first_or_404()   #如果不存在，报错404
	return render_template('detail.html', new_obj=new_obj)

if __name__ == '__main__':
	app.run(debug=True)