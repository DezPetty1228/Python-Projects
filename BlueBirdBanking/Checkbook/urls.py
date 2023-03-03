from django.urls import path
from . import views

urlpatterns = [
    # sets url path to home page index.html.
    path('', views.home, name='index'),
    # sets the path to create new account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets the url path to balance sheet page Balance sheet,html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to add new transactions page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]
