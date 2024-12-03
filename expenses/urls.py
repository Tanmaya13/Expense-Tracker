from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView
from expenses.views import ExpenseManagerViewSet

urlpatterns = [
    path('manage/', ExpenseManagerViewSet.as_view(), name='expense_manage')
]
#  = (
#     [
#         path('manage/', ExpenseManagerViewSet.as_view(), name='expense_manage'),
#         # path('items/<item_id>/', ItemDetailsViewSet.as_view(), name='item_details'),
#         # path('get_jwt_token/', TokenObtainPairView.as_view(), name='login'),
#     ],
# )