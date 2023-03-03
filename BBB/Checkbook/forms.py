from django.forms import ModelForm
from django.forms.utils import ErrorList

from .models import Account, Transaction


# Creates Account Form based on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction Model
class TransactionForm(ModelForm):
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.initial_deposit = None

    class Meta:
        model = Transaction
        fields = '__all__'
