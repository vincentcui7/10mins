from django import forms
from django.forms import ModelForm

def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")

def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")


class ProfileForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '你的真实姓名'}), label= '姓名', max_length=20)
    SEX_CHOICES = (
        ('性别', '性别'),
        ('男', '男'),
        ('女', '女'),
    )
    sex = forms.ChoiceField(label='', choices=SEX_CHOICES)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '********'}), label= '密码', max_length=20, validators = [word_validator])
    avatar = forms.FileField(label= '修改头像')


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages = {
            "required": 'wow, such words'
            },
        validators = [word_validator, comment_validator]
        )
