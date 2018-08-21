from flask import render_template, redirect, request, url_for, flash
from newbulletin import app, db
import json, os
from newbulletin.models import News

posts = []

@app.route("/")
@app.route("/home")
def home():
    if len(posts) == 0:
        get_posts()
        export_csv()
    return render_template('index.html', posts = posts, title = 'News Bulletin')

@app.route("/about")
def hello():
    return render_template('about.html',title = 'Updated Title',something = 'Just something for trying')

@app.route("/api")
def api():
    if len(posts) == 0:
        get_posts()
        export_csv()
    return render_template('api.html',title = 'API', posts = posts)

@app.errorhandler(404)
def page_not_found(e):
    next_page = request.url
    temp_url = next_page.split('/')
    if 'www.' in temp_url[-1] or 'http:' in temp_url[-1]:
        if 'http:' not in temp_url[-1]:
            return redirect('http://'+str(temp_url[-1]))
        else:
            return redirect(str(temp_url[-1]))
    return redirect(url_for('home'))

def get_posts():
    json_file = os.path.join(app.static_folder, 'json/output.json')
    with open(json_file, 'r') as f:
        global posts
        posts = json.load(f)
        print(posts[0]['headline'])


def export_csv():
    if News.query.first() == None:
        csv_file = os.path.join(app.static_folder, 'csv/news_bulletin666200b.csv')
        with open(csv_file, 'r', encoding = 'utf-8') as f:
            while True:
                lines = f.readline()
                if lines:
                    data = lines.replace('"','').replace('\n', "").split(',')
                    temp_post = News(id = data[0], headline = data[1] , link = data[2], publisher = data[3]
                        , something = data[4], main_site = data[5] , date_posted = data[6])
                    print(temp_post)
                    posts.append(temp_post)
                    db.session.add(temp_post)
                else:
                    break
            db.session.commit()
