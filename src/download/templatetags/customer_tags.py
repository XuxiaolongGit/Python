from django import template
register = template.Library()
import math
@register.inclusion_tag('download/pagination.html',takes_context=True)
def pagination_html(context):
    num = 3  #总共显示多少个页码,一定是奇数
    page_num = context['page']
    per_page = context['per_page']
    books = context['books']
    #总学生数
    total_num = context['total_num']
    #总页数
    total_page = math.ceil(total_num/per_page)
    #页码列表
    page_list = []
    if page_num - (num-1)//2 <=0:
        for i in range(page_num):
            page_list.append(i+1)
    else: #左边的页数 应该从page_num - (num-1)//2开始
        for i in range(page_num-(num-1)//2,page_num+1):
            page_list.append(i)
    #生成当前页，右边的页数
    if page_num+(num-1)//2 >=total_page:
        for i in range(page_num+1,total_page+1):
            page_list.append(i)
    else:
        for i in range(page_num+1,page_num+(num-1)//2+1):
            page_list.append(i)

    return {
        'page_num_list':page_list,
        'page_num':page_num,
        'context':context,
        'total_page':total_page
    }

@register.simple_tag
def add_class(field,class_str):
    return field.as_widget(attrs={'class':class_str})