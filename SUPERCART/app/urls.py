from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    # [ ]Home Page
    path('', views.home.as_view(), name="home"),

    # [ ] show product to home page means on click show that product
    path('product-detail/<int:id>',
         views.product_detail.as_view(), name='product-detail'),

    # [ ] specially for mobile page we can also create cloths and more product page like this
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    # [ ] login page and registration system generated
    path('accounts/login', auth_views.LoginView.as_view(template_name='login.html',
                                                        authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistration.as_view(),
         name='customerregistration'),


    # [ ] CHANGE PASSWORD PAGE
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',
                                                                  form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name="passwordchangedone"),

    # [ ] LOGOUT PAGE
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # [ ]PASSWORD RESET SIMILARTY SYSTEM GENERATED
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                 form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),



    path('add-to-card/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plusCart, name='pluscart'),
    path('minuscart/', views.minusCart, name='minuscart'),
    path('removecart/', views.removeCart, name='removecart'),



    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.AddressView.as_view(), name='address'),

    path('showcart/', views.showcart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('404/', views.PageNotFound, name='404 error'),
    path('checkout/', views.checkout, name='checkout'),
    path('cancleorder/<int:id>', views.cancleorder.as_view(), name='cancleorder'),
    path('returnorder/<int:id>', views.returnorder.as_view(), name='returnorder'),
    path('cancleorderdata/<int:id>', views.cancleorderdata.as_view(), name='cancleorderdata'),
    path('returnorderdata/<int:id>',
         views.returnorderdata.as_view(), name='returnorderdata'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
