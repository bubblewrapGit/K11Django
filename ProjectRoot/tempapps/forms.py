from django import forms
from django.forms import widgets
from django.http import request
'''
장고에서 제공하는 Form기능을 사용하려문 우선 forms.Form 클래스를 상속한다.
각 변수명은 해당 input태그의 name속성값으로 사용된다.
태그 생성시 required 속성이 포함되어 기본적인 빈값 검증을 하게 된다.
'''
class QuestionForm(forms.Form):
    # <input type="text"를 생성.label은 타이틀로 사용.
    user_id = forms.CharField(label='아이디', max_length=10)
    # 가장 기본적인 input태그를 생성. 타이틀은 변수명과 동일하게 (title)로 표시된다.
    title = forms.CharField()
    # 여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성.
    content = forms.CharField(widget=forms.Textarea)
    # 기본적인 input 태그를 성상하되 type='email'로 생성.
    email = forms.EmailField()
    # <input type="checkbox" 를 생성. 
    my_check = forms.BooleanField(required=False)
    # required=False => 유효성 검증을 하지 않는다.

    ############################################################################################
    data01 = ['유비','관우','장비']
    data02 = [
        ('red','빨강'),('green','녹색'),('blue','파랑'),('black','검정')
    ]
    
    #<input type="text" name="form1" required id="id_form1">
    form1 = forms.CharField(widget=forms.TextInput)
    #<input type="number" name="form2" required id="id_form2">
    form2 = forms.CharField(widget=forms.NumberInput)
    #<input type="password" name="form3" required id="id_form3">
    '''
    추가적인 속성을 부여할때는 위젯에 attrs을 기술한다.
    '''
    form3 = forms.CharField(
        widget=forms.PasswordInput(attrs={'size':30})
    )
    #<textarea name="form4" cols="40" rows="10" required id="id_form4">
    form4 = forms.CharField(widget=forms.Textarea)
    '''
    select태그를 표현한다. (1개 선택)
    choices : select태그의 option태그를 구성하는 데이터로 사용한다.
        순서대로 value와 text로 사용된다.
    initial : 해당 태그의 default값으로 사용된다.
        주로 수정에서 활용하면 된다.
        
    <select name="form5" id="id_form5">
        <option value="red">빨강</option>
        ....
        <option value="blue" selected>파랑</option>
    </select>
    '''
    form5 = forms.ChoiceField(
        widget=forms.Select,
        choices=data02,
        initial='blue'   # 디폴트값(없을시 첫번째목록)
    )
    '''
    select태그를 표현하는 것은 5번과 동일하지만 multiple 속성을 부여하여
    2개 이상의 항목을 선택할 수 있게 한다.
    또한 default값을 표현하기 위해 2개 이상의 항목을 선택할 수 있어야 함으로
    리스트를 사용해야 한다.
    (멀티 선택)
    '''
    form6 = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=data02,
        initial=['black','green']
    )
    '''
    <div id="id_form7">
        <div>
            <label for="id_form7_0">
                <input type="radio" name="form7" value="red" required id="id_form7_0">빨강
            </label>
        </div>
        <div>
            <label for="id_form7_1">
                <input type="radio" name="form7" value="green" required id="id_form7_1">녹색
            </label>
        </div>
    </div>
    라디오 버튼을 표현한다.(1개 선택)
    '''
    form7 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=data02,
        initial = 'blue'
    )
    '''
    체크박스를 표현한다.(멀티 선택)
    추가적인 속성을 부여할때는 attrs={'class':'red'} 와 같이 기술한다.
    '''
    form8 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class':'red'}),
        choices=data02,
        initial=['black', 'green'],
    )
    
    # 파일 <input type="file" name="form9" required="" id="id_form9">
    form9 = forms.CharField(
        widget=forms.FileInput(attrs={'class': 'blue'}), 
        label="첨부파일", 
    )

# 게시판의 글쓰기 페이지 UI 구현
class WriteForm(forms.Form):
    '''
        attrs 속성으로 각 폼에 class를 부여한다.
        가로 사이즈 조정을 위해 w100 클래스가 추가되었다.
        첨부파일의 경우 필수사항이 아니므로 required=False 추가한다.
        입력폼의 타이틀 부분을 한글로 처리하기 위해 label을 추가한다.
    '''
    my_name = forms.CharField(
        label = '작성자',
        widget = forms.TextInput(attrs={'class':'form-control w100'})
    )
    my_pass = forms.CharField(
        label = '패스워드',
        widget = forms.TextInput(attrs={'class':'form-control w200'})
    )
    my_title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(attrs={'class':'form-control'})
    )
    my_content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(attrs={'class':'form-control'})
    )
    my_file = forms.FileField(
        label = '첨부파일',
        widget = forms.FileInput(attrs={'class':'form-control'}),
        required=False
    )
    