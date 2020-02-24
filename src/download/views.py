from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,FileResponse
from download.models import Book
import os
from download.forms import BookForm
from django.db.models import Q
from src.settings import UPLOAD_ROOT
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'download/index.html')
def books(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin@admin.com' and password == '123456':
            request.session['name'] = username
            request.session.set_expiry(10)
            return redirect(reverse('download:books_admin'))
        return redirect(reverse('download:books'))
    section = 'PDF列表'
    # 获取查询参数
    search = request.GET.get('search', '').strip()
    if search:
        bks = Book.objects.filter(name__contains=search)
    else:
        bks = Book.objects.all().order_by('-c_time')
    # 当前页码
    page = request.GET.get('page', 1)
    # 每页显示多少数据
    per_page = request.GET.get('per_page', 10)
    page = int(page)
    per_page = int(per_page)
    total_num = bks.count()
    bks = bks[(page - 1) * per_page:page * per_page]
    return render(request, "download/books_user.html",
                  context={'books': bks, 'section': section,
                           'search': search,
                           'per_page': per_page,
                           'page': page,
                           'total_num': total_num
                           })




def edit(request,pk):
    section = 'PDF信息修改'
    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return render(reverse('download:books'))
    return render(request, 'download/student_edit_form.html',
                  context={
                      'section': section,
                      'book': book,
                      'form': form,
                  })


# def add(request):
#     section = '添加PDF'
#     if request.method == 'GET':
#         form = BookForm()
#         return render(request, 'download/student_edit_form.html', context={
#             'section': section,
#             'form':form,
#         })
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect(reverse('download:books'))

def delete(request):
    pk = request.GET.get('pk')
    book = Book.objects.get(pk=pk)
    book.delete()
    day_dir = book.c_time.strftime('%Y%m%d')
    pre_dir = os.path.join(UPLOAD_ROOT,day_dir)
    filepath = os.path.join(pre_dir,book.name)
    os.remove(filepath)
    if not os.listdir(pre_dir):
        os.rmdir(pre_dir)
    return redirect(reverse('download:books_admin'))

def upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file', None)
        for file in files:
            day_dir = datetime.now().strftime('%Y%m%d')
            pre_dir = os.path.join(UPLOAD_ROOT, day_dir)
            if not os.path.exists(pre_dir):
                os.mkdir(pre_dir)
            filename = os.path.join(pre_dir,file.name)
            with open(filename, 'wb') as f:
                for line in file.chunks():
                    f.write(line)
            filesize = os.path.getsize(filename)
            filesize = str(round((filesize/1024/1024),2))+"MB"
            book = Book(name=file.name,size=filesize)
            book.save()
        return HttpResponse('<h1>上传成功</h1>')

    return render(request, "download/upload_form.html")

def download(request,pk):
    book = Book.objects.get(pk=pk)
    day_dir = book.c_time.strftime('%Y%m%d')
    pre_dir=os.path.join(UPLOAD_ROOT,day_dir)
    filepath = os.path.join(pre_dir,book.name)
    file = open(filepath, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"'%(book.name)
    return response

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin@admin.com' and password == '123456':
            request.session['name'] = username
            request.session.set_expiry(10)
            return redirect(reverse('download:books_admin'))

    return render(request, "download/login.html")
def books_admin(request):
    section = 'PDF列表'
    # 获取查询参数
    search = request.GET.get('search', '').strip()
    if search:
        bks = Book.objects.filter(name__contains=search)
    else:
        bks = Book.objects.all().order_by('-c_time')
    # 当前页码
    page = request.GET.get('page', 1)
    # 每页显示多少数据
    per_page = request.GET.get('per_page', 10)
    page = int(page)
    per_page = int(per_page)
    total_num = bks.count()
    bks = bks[(page - 1) * per_page:page * per_page]
    return render(request, "download/books.html",
                  context={'books': bks, 'section': section,
                           'search': search,
                           'per_page': per_page,
                           'page': page,
                           'total_num': total_num
                           })
