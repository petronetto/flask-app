from flask import render_template

class Home(object):
    @classmethod
    def get(cls):
        return render_template('main.html')
