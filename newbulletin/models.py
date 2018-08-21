from newbulletin import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    headline = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)    
    publisher = db.Column(db.String(50), nullable = False)
    something = db.Column(db.String(1), nullable = False)
    main_site = db.Column(db.String(50), nullable = False)
    date_posted = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"News ('{self.headline}' by '{self.publisher}')"

