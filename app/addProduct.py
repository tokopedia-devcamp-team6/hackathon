from app import app, Resource, db, request
from app import models as m

class AddProduct(Resource):
  def post(self):
    content = request.get_json()
    print(content)
    p = m.Produk(id=content['id'], nama=content['nama'], stok=content['stok'], harga=content['harga'], kategori_id=content['kategori_id'], produsen_id=content['produsen_id'], detail=content['detail'], gambar=content['gambar'], cakupan=content['cakupan'])
    db.session.add(p)
    db.session.commit()
    resp = {
      'message': 'add product {} success'.format(content['nama'])
    }
    return resp