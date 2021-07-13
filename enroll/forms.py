from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# Sign Up form
class SignUpRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {'email':'Email'}
    
# Edit user profile    
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
        'date_joined', 'last_login']
        labels = {'email':'Email'}

# Edit Admin profile form
class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}