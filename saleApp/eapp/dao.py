from eapp.models import Category, Product, User


def load_categories():
    return Category.query.all()

def load_products(cate_id=None, kw=None,page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    return query

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    import hashlib
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username == username,
                             User.password == password).first()