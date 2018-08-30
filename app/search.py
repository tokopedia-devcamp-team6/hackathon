from app import app, api, Resource, db
from app import models as m

class SearchProduct(Resource):
  def get(self, search, page):
    products = m.Produk.query
    products = products.filter(m.Produk.nama.like('%' + search + '%'))
    products = products.all()
    # products = products.pagination(page, 10, False).items
    print(type(products))
    total = len(products)
    results = [prod.serialize for prod in products]
    resp = {
          "total": total,
          "data": results
          }
    return resp

class ProductByCategory(Resource):
  def get(self, kategoriId):
    products = m.Produk.query.filter(m.Produk.kategori_id == kategoriId).all()
    total = len(products)
    results = [prod.serialize for prod in products]
    resp = {
          "total": total,
          "data": results
          }
    return resp
    