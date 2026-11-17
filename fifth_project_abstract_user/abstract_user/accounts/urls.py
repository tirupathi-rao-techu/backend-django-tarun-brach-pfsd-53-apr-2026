from django.urls import path
# from .views import register_view, login_view, dashboard_view, logout_view,send_test_mail, verify_otp_view, resent_otp_view, change_password_view
from .views import *
urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("", dashboard_view),
    path("logout/", logout_view),
    path("sent-mail/", send_test_mail),
    path("verify-otp/<int:id>/", verify_otp_view, name="verify-otp"),
    path("resend-otp/<int:id>/", resent_otp_view, name="resend-otp"),
    path("change-password/", change_password_view, name="change-password"),
    path("forgot-password/", forgot_password_view, name="forgot-password"),
    path("reset-password/<uid>/<token>/", reset_password_view, name="reset-password")
    
]