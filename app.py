from flask import Flask, render_template

app = Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'london, Ontario',
    'Salary': '$100,000'
  },
  {
    'id':1,
    'title': 'software engineer',
    'location': 'Toronto, Ontario',
    'Salary': '$120,000'
  },
  {
    'id':3,
    'title': 'Support Analyst',
    'location': 'Ottawa, Ontario',
    'Salary': '$110,000'
  },
  {
    'id':4,
    'title': 'Backend engineer',
    'location': 'kitchener, Ontario',
    'Salary': '$100,000'
  }
]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs= JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug= True)