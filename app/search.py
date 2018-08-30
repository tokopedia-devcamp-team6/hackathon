from app import app, Resource, db
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
          "per_page": 10,
          "current_page": page,
          "first_page_url": "/products/1",
          "last_page_url": "/products/10",
          "next_page_url": "products/{}".format(page+1),
          "data": results
          }
    return resp