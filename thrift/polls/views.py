from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from django.db.models import Max

from .models import *




def login_home(request):
    return render(request,"./polls/login.html")

def product_update_admin(request):
   return render(request, "./polls/product_update.html")

def delete_num(request):
  id = request.GET.get('id')
  res = product_add.objects.get(id=int(id))
  res.delete()

  t = product_add.objects.all()
  d = {'details': t}
  return render(request, './polls/admin_view_product.html',d)



def index(request):
    return render(request,"./polls/index.html")


def adminhome(request):
    return render(request,"./polls/adminhome.html")

def user_home(request):
    return render(request,"./polls/user_home.html")

def add_product(request):
    return render(request,"./polls/add_product.html")


def admin_view_pro(request):
    return render(request,"./polls/admin_view_product.html")



def admin_login(request):

    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')

        ul = login.objects.filter(uname=un, passwd=pwd, User_type='admin')
        ud = login.objects.filter(uname=un, passwd=pwd, User_type='user')

        #user_type = userlogin.objects.filter(user_type = 'user')
        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request, './polls/adminhome.html')

        elif len(ud) == 1:
            request.session['user_name'] = ud[0].uname
            request.session['user_id'] = ud[0].id
            context1 = {'uname': request.session['user_name']}
            return render(request, './polls/user_home.html', context1)

        else:

            context ={ 'msg1':'Invalid username and password'}
            return render(request, './polls/login.html',context)

    else:
        return render(request, './polls/login.html')




def user_register(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        p = request.POST.get('passwd')
        housename=request.POST.get('housename')
        phoneno=request.POST.get('phoneno')
        pin=request.POST.get('pin')
        city=request.POST.get('city')
        street=request.POST.get('street')


        #status = "new"

        if login.objects.filter(uname=email):  #orange color uname from models
            msg = {'msg1' : 'already username exits'}
            return render(request, './polls/registration.html', msg)
        else:

            l = login(uname=email, passwd=p,  User_type='user' )
            l.save()

            user_id = login.objects.all().aggregate(Max('id'))['id__max']



            ud = user(user_id=user_id, fname=fname, lname=lname,housename=housename,phoneno=phoneno,pin=pin,city=city,street=street,email=email)
            ud.save()

            context = {'msg': 'User Registered'}
            return render(request, './polls/login.html',context)

    else:
        return render(request, './polls/registration.html')



def logout(request):

    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
        return index(request)
    else:
        return index(request)

def user_details_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = user.objects.get(user_id= int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        #variablename=request.POST.get('modelsnte akathe name')

        housename = request.POST.get('housename')
        city = request.POST.get('city')
        street = request.POST.get('street')

        phoneno = request.POST.get('phoneno')
        pin = request.POST.get('pin')


        up.fname = fname
        up.lname = lname
        up.city = city
        up.pin = pin
        up.street = street

        up.housename = housename
        up.phoneno = phoneno
        up.save()


        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'polls/user_details_update.html',context)

    else:
        user_id = request.session['user_id']
        up = user.objects.get(user_id=int(user_id))
        context={'up':up}
        return render(request, 'polls/user_details_update.html',context)

def add_product(request):
    if request.method == 'POST':
        u_file = request.FILES['image']
        fs = FileSystemStorage()
        path = fs.save(u_file.name, u_file)



        prdt = request.POST.get('product')
        qty = request.POST.get('quantity')
        sz = request.POST.get('size')
        price = request.POST.get('price')
        desc = request.POST.get('description')



        pdt = product_add(product_name=prdt, quantity=qty, size=sz, price=price, product_desc=desc,image=path)
        pdt.save()
        return render(request,'polls/add_product.html')
    else:
        return render(request, 'polls/add_product.html')


def admin_view_pro(request):
    pr = product_add.objects.all()
    p = {'details': pr} #details= chumma ishtamullathu kodukkkunne
    return render(request, "./polls/admin_view_product.html", p)


def product_update(request):
    if request.method == 'POST':
        id = request.POST.get('pid')
        up = product_add.objects.get(id=int(id))


        p = request.POST.get('product')
        q = request.POST.get('quantity')
        s = request.POST.get('size')
        z = request.POST.get('price')
        d = request.POST.get('description')

        up.product_name = p
        up.quantity = q
        up.size = s
        up.price = z
        up.product_desc = d
        up.save()
        upl=product_add.objects.all()
        context={'details':upl}
        return render(request, './polls/admin_view_product.html', context)
    else:
        id = request.GET.get('id')
        pr = product_add.objects.get(id=int(id))
        p = {'up': pr}
        return render(request, './polls/product_update.html',p)

def user_product_view(request):
        upr = product_add.objects.all()
        q = {'details': upr}
        return render(request, "./polls/user_product_view.html", q)







