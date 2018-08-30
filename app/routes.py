from app import app, api, Resource
import os

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

class HelloWorld(Resource):
    def get(self):
        basedir = os.environ.get('DATABASE_URL')
        return {'message': basedir}

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)