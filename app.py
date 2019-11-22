from flask import Flask, render_template
from elasticapm.contrib.flask import ElasticAPM
app = Flask(__name__)
app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'FlaskApp',
          'SECRET_TOKEN': 'd910fe18cd0fde99ee282685cc7046e14a8491df474b85c8',         
          'SERVER_URL': 'http://localhost:8200'
}
apm = ElasticAPM(app)

@app.route('/')
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run()

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/divbyzero')
def divbyzero():
    num = 2 / 0
    return "hello world - " + str(num)

@app.errorhandler(500)
def internal_error(error):
 return render_template('500.html'), 500