from django import forms

os_lists = (
    (1,'CentOS 7'),
    (2,'CentOS 6'),
    (3,'Ubuntu 17'),
    (4,'WindowsServer2012'),
    (5,'WindowsServer2008'),
    (6,'WindowsServer2003'),
)


class deployVmForm(forms.Form):
    VM_name = forms.CharField(
        label='VirtualMachine Name',
        max_length=32,
        required=True,
        widget=forms.TextInput()
    )

    OS_type = forms.ChoiceField(
        label='OS Type',
        widget=forms.Select,
        choices=os_lists
    )
