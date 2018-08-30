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

    @property
    def serialize(self):
        resp  = {
            "id": self.id,
            "body": self.body,
            "timestamp": self.timestamp,
            "user_id": self.user_id
        }
        return resp

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Kategori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(20), index=True, nullable=False)
    detail = db.Column(db.String(254), nullable=False)

    @property
    def serialize(self):
        resp  = {
            'id' : self.id,
            'nama' : self.nama,
            'detail' : self.detail
        }
        return resp

class Produsen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(80), index=True, nullable=False)
    nama_usaha = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(254), index=True, nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    telepon = db.Column(db.String(14), nullable=False)
    waktu_mulai = db.Column(db.DateTime, index=True)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))

    @property
    def serialize(self):
        resp  = {
            "id": self.id,
            "nama_lengkap": self.nama_lengkap,
            "nama_usaha": self.nama_usaha,
            "email": self.email,
            "alamat": self.alamat,
            "telepon": self.telepon,
            "waktu_mulai": self.waktu_mulai,
            "kategori_id": self.kategori_id
        }
        return resp

class Pembeli(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(254), index=True, nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    telepon = db.Column(db.String(14), nullable=False)

    @property
    def serialize(self):
        resp  = {
            "id": self.id,
            "nama_lengkap": self.nama_lengkap,
            "email": self.email,
            "alamat": self.alamat,
            "telepon": self.telepon
        }
        return resp

class Produk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(80), index=True, nullable=False)
    stok = db.Column(db.Integer, index=True, nullable=False)
    harga = db.Column(db.Integer, index=True, nullable=False)
    detail = db.Column(db.String(254), nullable=False)
    gambar = db.Column(db.String(254), index=True, nullable=False)
    cakupan = db.Column(db.String(50), index=True, nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'))
    produsen_id = db.Column(db.Integer, db.ForeignKey('produsen.id'))

    @property
    def serialize(self):
        resp  = {
            "id": self.id,
            "nama": self.nama_lengkap,
            "stok": self.stoknama_usaha,
            "harga": self.harga,
            "detail": self.detail,
            "gambar": self.gambar,
            "cakupan": self.cakupan,
            "kategori_id": self.kategori_id,
            "produsen_id": self.produk_id
        }
        return resp

class Pesanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jumlah = db.Column(db.Integer, index=True, nullable=False)
    waktu_butuh = db.Column(db.DateTime, index=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(30), index=True, nullable=False)
    produk_id = db.Column(db.Integer, db.ForeignKey('produk.id'))
    pembeli_id = db.Column(db.Integer, db.ForeignKey('pembeli.id'))

    @property
    def serialize(self):
        resp  = {
            "id": self.id,
            "jumlah": self.jumlah,
            "waktu_butuh": self.waktu_butuh,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status,
            "produk_id": self.produk_id,
            "pembeli_id": self.pembeli_id
        }
        return resp