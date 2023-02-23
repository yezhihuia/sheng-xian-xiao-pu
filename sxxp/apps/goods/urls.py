from django.conf.urls import url
from apps.goods.views import IndexView, DetailView, ListView, ActionView

urlpatterns = [
    url(r'^index$', IndexView.as_view(), name='index'),  # 首页
    url(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
    url(r'^action/(?P<index>\d+)$', ActionView.as_view(), name='action'), # 首页促销活动页面
    url(r'^$', IndexView.as_view(), name='index'),  # 首页  对应什么都不输入的情况，但是乱输则访问不了
]
