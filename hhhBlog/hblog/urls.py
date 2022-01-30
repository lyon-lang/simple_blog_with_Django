from django.urls import path
from .views import Home, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView, AboutView, WorkWithMeView, ContactView, SearchView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail" ),
    path('add_post/', AddPostView.as_view(), name="add_post" ), 
    path('add_category/', AddCategoryView.as_view(), name="add_category" ),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post" ),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post" ),
    path('category/<str:cats>/', CategoryView, name="category" ),
    path('category_list/', CategoryListView, name="category_list" ),
    path('like/<int:pk>', LikeView, name="like_post" ),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment" ),
    path('about/', AboutView.as_view(), name="about" ),
    path('work_with_me/', WorkWithMeView.as_view(), name="work_with_me" ),
    path('contact/', ContactView.as_view(), name="contact" ),
    path('search/', SearchView, name="search" ),
    
    
]