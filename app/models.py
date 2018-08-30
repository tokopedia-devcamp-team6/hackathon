from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Kategori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(20), index=True, nullable=False)
    detail = db.Column(db.String(254), nullable=False)

class Produsen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(80), index=True, nullable=False)
    nama usaha = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(254), index=True, nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    telepon = db.Column(db.String(14), nullable=False)
    waktu_mulai = db.Column(db.DateTime, index=True)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))

class Pembeli:
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(254), index=True, nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    telepon = db.Column(db.String(14), nullable=False)

class Produk:
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(80), index=True, nullable=False)
    stok = db.Column(db.Integer, index=True, nullable=False)
    harga = db.Column(db.Integer, index=True, nullable=False)
    detail = db.Column(db.String(254), nullable=False)
    gambar = db.Column(db.String(254), index=True, nullable=False)
    cakupan = db.Column(db.String(50), index=True, nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))
    produsen_id = db.Column(db.Integer, db.ForeignKey('produsen.id'))

class Pesanan:
    id = db.Column(db.Integer, primary_key=True)
    jumlah = db.Column(db.Integer, index=True, nullable=False)
    waktu_butuh = db.Column(db.DateTime, index=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(30), index=True, nullable=False)
    produk_id = db.Column(db.Integer, db.ForeignKey('produk.id'))
    pembeli_id = db.Column(db.Integer, db.ForeignKey('pembeli.id'))