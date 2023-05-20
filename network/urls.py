
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .Routes import views,Buy_sale

urlpatterns = [
    path("community", views.index, name="community"),
    path("index", views.index, name="index"),
    path("n/login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("n/register", views.register, name="register"),
    path("n/n/<str:username>", views.profile, name='profile'),
    path("n/following", views.following, name='following'),
    path("n/saved", views.saved, name="saved"),
    path("n/createpost", views.create_post, name="createpost"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:post_id>/comments", views.comment, name="comments"),
    path("n/post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    
    path('pet/pet_list', Buy_sale.pet_list, name='pet_list'),
    path('pet/buy/<int:pet_id>/', Buy_sale.buy_pet, name='buy_pet'),
    path('pet/sell/', Buy_sale.sell_pet, name='sell_pet'),
    path('pet/sell/', Buy_sale.sell_pet, name='sell_pet'),
    
    path('', Buy_sale.pet_home, name='pet_home'),
    path('gallery', Buy_sale.gallery, name='gallery'),
    path('about', Buy_sale.about, name='about'),
    path('sale', Buy_sale.sale, name='sale'),
    path('buyed', Buy_sale.buyed, name='buyed'),
    path('services', Buy_sale.services, name='services'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

