from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),

    # Dealers
    path('get_dealers/', views.get_dealerships, name='get_dealers'),

    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # Dealer details
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # Dealer reviews + sentiment
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),

        path(route='add_review', view=views.add_review, name='add_review'),
]
