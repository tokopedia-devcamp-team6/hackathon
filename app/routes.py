from app import app, api, Resource, db
from app.models import User, Kategori, Produk
import os

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

class HelloWorld(Resource):
    def get(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        u = User(username='susan', email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        return {'message': 'john', 'message2': 'susan'}


class Users(Resource):
    def get(self):
        users = User.query.all()
        emails = []
        for u in users:
            emails.append(u.email)
        return {'data': emails}


class Generate(Resource):
    def get(self):
        k = Kategori(id=1, nama='Perikanan', detail='Produk hasil sumber daya laut')
        db.session.add(k)
        db.session.commit()
        k = Kategori(id=2, nama='Peternakan', detail='Produk hasil sumber daya ternak')
        db.session.add(k)
        db.session.commit()
        k = Kategori(id=3, nama='Pertanian', detail='Produk hasil sumber daya tani')
        db.session.add(k)
        db.session.commit()
        return {'message': 'added'}

class Product(Resource):
    def get(self, page):
        products = Kategori.query.paginate(page, 2, False).items
        total = len(Produk.query.all())
        products = [prod.serialize for prod in products]
        resp = {
                "per_page": total,
                "current_page": page,
                "first_page_url": "/products/1",
                "last_page_url": "/products/10",
                "next_page_url": "products/{}".format(page+1),
                "data": products
                }
        return resp

api.add_resource(HelloWorld, '/hello')
api.add_resource(Users, '/users')
api.add_resource(Product, '/products/<int:page>')
api.add_resource(Generate, '/seed')


if __name__ == '__main__':
    app.run(debug=True)