from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        # 这里的父类其实是视图里面继承的View类，这里的as_view方法是调用的user/views里面继承的View的
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)