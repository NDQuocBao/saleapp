from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from eapp import db, app
from eapp.models import Product, Category, UserRole
from flask_login import current_user, logout_user #current_user luu doi tuong user dang dang nhap.
from flask import redirect

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class ProductView(AdminView):
    column_list = ['id','name','price','active','category_id']
    column_searchable_list = ['name']
    column_filters = ['id','name','price']
    can_export = True
    edit_modal = True #chỉnh sửa không cần chuyển màn hình
    column_editable_list = ['name'] #sửa nhanh trường
    page_size = 6

    def is_accessible(self):
        return current_user.is_authenticated # = true khi dang nhap -> dang nhap roi moi cho xem

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self) -> bool:
        return current_user.is_authenticated

admin = Admin(app=app, name="E-Commerce's Admin")

admin.add_view(AdminView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(LogoutView(name="Đăng xuất"))
