from django.test import TestCase

# Create your tests here.

education_levels = ['下忍', '中忍', '上忍', '影', '小学', '初中', '高中', '专', '本', '研', '博']

want_edu = '火影'


w = [i for i in range(len(education_levels)) if education_levels[i] in want_edu][0]

print(w)