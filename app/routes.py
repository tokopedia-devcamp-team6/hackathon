from app import app, api, Resource, db
from app.models import User, Kategori, Produk, Produsen, Pembeli, Pesanan
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
        # produsen
        # k = Produsen(id=1, nama_lengkap='Debby Bycraft', nama_usaha='IDACORP, Inc.', email='dbycraft0@linkedin.com', alamat='489 Shelley Park', telepon='2566873785', waktu_mulai='2014-11-02', kategori_id=4)
        # db.session.add(k)
        # k = Produsen(id=2, nama_lengkap='Annissa Nobriga', nama_usaha='Norfolk Souther Corporation', email='dbycraft0@linkedin.com', alamat='489 Shelley Park', telepon='2566873785', waktu_mulai='2014-11-02', kategori_id=2)
        # db.session.add(k)
        # k = Produsen(id=3, nama_lengkap='Carney Hartright', nama_usaha='Fate Therapeutics, Inc.', email='chartright2@php.net', alamat='20521 Maryland Drive', telepon='2222006289', waktu_mulai='2016-08-04', kategori_id=1)
        # db.session.add(k)
        # k = Produsen(id=4, nama_lengkap='Frans Trappe', nama_usaha='Minerals Technologies Inc.', email='ftrappe3@typepad.com', alamat='98749 Vidon Terrace', telepon='6777203858', waktu_mulai='2018-01-14', kategori_id=4)
        # db.session.add(k)
        # k = Produsen(id=5, nama_lengkap='Stephanus Battle', nama_usaha='B. Riley Financial, Inc.', email='sbattle4@google.cn', alamat='71 Park Meadow Lane', telepon='1655273371', waktu_mulai='2015-11-14', kategori_id=3)
        # db.session.add(k)

        # pembeli
        k = Pembeli(id=1, nama_lengkap='Gwyn Papen', email='dbycraft0@linkedin.com', alamat='489 Shelley Park', telepon='2566873785')
        db.session.add(k)
        db.session.commit()

        # k = Pembeli(id=2, nama_lengkap='Jdavie Smallpeice', email='jsmallpeice1@theatlantic.com', alamat='1022 Maryland Court', telepon='9961742868')
        # db.session.add(k)
        # k = Pembeli(id=3, nama_lengkap='Matilda Bartleet', email='mbartleet2@engadget.com', alamat='8300 Thackeray Park', telepon='7652037342')
        # db.session.add(k)
        # k = Pembeli(id=4, nama_lengkap='Mata Sybbe', email='msybbe3@globo.com', alamat='9931 Shopko Drive', telepon='2368210098')
        # db.session.add(k)
        # k = Pembeli(id=5, nama_lengkap='Clemmy Lace', email='clace4@scientificamerican.com', alamat='84 Veith Center', telepon='9877101617')
        # db.session.add(k)

        # pesanan
        # k = Pesanan(id=1, produk_id=3, jumlah=6, waktu_butuh='10/1/2018', status='accepted', pembeli_id=3)
        # db.session.add(k)
        # k = Pesanan(id=2, produk_id=4, jumlah=7, waktu_butuh='9/13/2018', status='requested', pembeli_id=3)
        # db.session.add(k)
        # k = Pesanan(id=3, produk_id=1, jumlah=11, waktu_butuh='9/22/2018', status='accepted', pembeli_id=2)
        # db.session.add(k)
        # k = Pesanan(id=4, produk_id=1, jumlah=9, waktu_butuh='10/16/2018', status='requested', pembeli_id=5)
        # db.session.add(k)
        # k = Pesanan(id=5, produk_id=2, jumlah=9, waktu_butuh='10/13/2018', status='accepted', pembeli_id=4)
        # db.session.add(k)

        # produk
        # k = Produk(id=1, stok=4, harga=13931, kategori_id=3, produsen_id=4, detail='abon', gambar='/srcabon-ayam-2.jpg', cakupan='semarang')
        # db.session.add(k)
        # k = Produk(id=2, stok=11, harga=29801, kategori_id=3, produsen_id=5, detail='abon', gambar='/src/abon-ayam.jpg', cakupan='semarang')
        # db.session.add(k)
        # k = Produk(id=3, stok=14, harga=18005, kategori_id=3, produsen_id=1, detail='abon', gambar='/src/abon-sapi.jpg', cakupan='semarang')
        # db.session.add(k)
        # k = Produk(id=4, stok=5, harga=32426, kategori_id=1, produsen_id=4, detail='buah', gambar='/src/alpukat.jpeg', cakupan='bandung')
        # db.session.add(k)
        # k = Produk(id=5, stok=11, harga=14016, kategori_id=1, produsen_id=4, detail='buah', gambar='/src/apel-hijau.jpg', cakupan='jakarta')
        # db.session.add(k)

        return {'message': 'added'}

class Product(Resource):
    def get(self, page):
        products = Kategori.query.paginate(page, 2, False).items
        products = [prod.serialize for prod in products]
        print(products)
        return {
                "per_page": "10",
                "current_page": page,
                "first_page_url": "/products/1",
                "last_page_url": "/products/10",
                "next_page_url": "products/",
                "data": "blank"
                }

api.add_resource(HelloWorld, '/hello')
api.add_resource(Users, '/users')
api.add_resource(Product, '/products/<int:page>')
api.add_resource(Generate, '/seed')


if __name__ == '__main__':
    app.run(debug=True)