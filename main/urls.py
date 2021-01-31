from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from business.views import (
    BusinessSignUpView,
    UserSignUpView,
    SignUpView,
    profile,
    setbusiness,
    updatesetbusiness

    
    
)

from blog.views import (
    BlogListView,
    BlogCreateView,
    blog_single,
    BlogUpdateView,
    BlogDeleteView,
    BlogCommentDeleteView
    
)
from blog.amaizingview import(
    AmaizingListView,
    AmaizingCreateView,
    AmaizingUpdateView,
    AmaizingDeleteView,
    amaizing_single,
    BlogCommentDeleteView,
    BlogAnonyCommentDeleteView
)


from business.bview import (
    ProductCreateView,
    ServiceCreateView,
    RestaurantCreateView,
    ProductUpdateView,
    ServiceUpdateView,
    RestaurantUpdateView,
    ProductDeleteView,
    ServiceDeleteView,
    RestaurantDeleteView,
    product_listview,
    service_listview,
    restaurant_listview,
    BusinessCommentDeleteView

)
from home import views as hviews
from django.conf.urls import handler404, handler500
from django.views.static import serve
urlpatterns = [
    path('', include('home.urls')),
    path('alphamin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/',SignUpView.as_view(), name='signup'),
    path('accounts/signup/business/', BusinessSignUpView.as_view(), name='business_signup'),
    path('accounts/signup/juser/', UserSignUpView.as_view(), name='justuser_signup'),
    path('setbusiness/<str:username>/', setbusiness, name='set-business' ),
    path('setbusiness/<str:code>/update/', updatesetbusiness, name='update-set-business' ),
    path('accounts/usr/profile/', profile, name='profile' ),
        path('password-reset/',
            auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), 
            name='password_reset'),    
    path('password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
            name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset-confirm.html'), 
            name='password_reset_confirm'),
    path('password-reset_complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
            name='password_reset_complete')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += url(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})

#Blog urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/new/', BlogCreateView.as_view(), name='create-blog'),
    url(r'^blog/(?P<id>\d+)/$', blog_single, name='blog-single'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/comment/<int:pk>/detele', BlogCommentDeleteView.as_view(), name='bcomment-delete')
]

#Wow that's Amaizing urls
urlpatterns += [
    path('Amaizing/', AmaizingListView.as_view(), name='amaizing'),
    path('Amaizing/new/', AmaizingCreateView.as_view(), name='create-amaizing'),
    url(r'^Amaizing/(?P<id>\d+)/$', amaizing_single, name='amaizing-single'),
    path('Amaizing/<int:pk>/update', AmaizingUpdateView.as_view(), name='amaizing-update'),
    path('Amaizing/<int:pk>/delete', AmaizingDeleteView.as_view(), name='amaizing-delete'),
    path('Amaizing/comment/<int:pk>/detele', BlogCommentDeleteView.as_view(), name='acomment-delete'),
    path('Amaizing/anonycomment/<int:pk>/detele', BlogAnonyCommentDeleteView.as_view(), name='anycomment-delete')
]

#business create,update,delete views

urlpatterns += [
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('service/new/', ServiceCreateView.as_view(), name='service-create'),
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant-create'),
    #end of create
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),

]
 
urlpatterns += [
    path('pr/<str:username>/', product_listview, name='sb-product'),
    path('sv/<str:username>/', service_listview, name='sb-service'),
    path('rs/<str:username>/', restaurant_listview, name='sb-food'),
    path('bs/comment/<int:pk>/detele', BusinessCommentDeleteView.as_view(), name='bscomment-delete')
     
    
]
handler404 = hviews.error_404
handler500 = hviews.error_500

