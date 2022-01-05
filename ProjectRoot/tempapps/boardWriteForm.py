from django import forms

class boardWriteForm(forms.Form):
    # <input type="text"를 생성.label은 타이틀로 사용.
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', "style":"width:100px;"}), label='작성자', max_length=10)
    user_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "style":"width:200px;"}), label='패스워드', min_length=4, max_length=12)
    # 가장 기본적인 input태그를 생성. 타이틀은 변수명과 동일하게 (title)로 표시된다.
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='제목')
    # 여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성.
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', "rows":"5"}), label='내용')
    # 기본적인 input 태그를 성상하되 type='email'로 생성.
    addfile = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="첨부파일", required=False)