from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import LoginForm, SignUpForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def login(request):
  form = LoginForm(request.POST or None)
  msg = None
  if request.method == "POST":
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_aktif == 'T':
          auth_login(request, user)
          return redirect("/")
        else:
          msg = 'User sedang tidak aktif, silahkan hubungi Administrator'
      else:
        msg = 'Username / Password yang anda masukkan tidak sesuai, silahkan ulangi kembali'
    else:
      msg = 'Error validating the form'

  return render(request, "authentication/login.html", {"form": form, "msg": msg})

@login_required
def user_logout(request):
  logout(request)
  return redirect("/auth/login")

def register(request):
  context = {'segment': 'register'}
  form = SignUpForm(request.POST or None)
  msg = None

  return render(request, "authentication/register.html", {"form": form, "msg": msg})

# api data user
@require_http_methods(["POST"])
def registerDataUser(request):
  p_nama = request.POST.get('nama')
  p_username = request.POST.get('username')
  p_email = request.POST.get('email')
  p_password = request.POST.get('password')
  p_repassword = request.POST.get('repassword')
  p_notelp = request.POST.get('notelp')
  p_role = 2
  p_status = "P"

  data = {}
  status = 400

  if p_password != p_repassword : 
    data = {
      "status": "failed",
      "message": "Password dan Ulangi Password yang anda masukkan tidak sama"
    }
  else:
    try:
      user = get_user_model().objects.create(
        role_id=p_role,
        nama=p_nama,
        username=p_username,
        email=p_email,
        notelp=p_notelp,
        is_aktif=p_status,
      )
      user.set_password(p_password)
      user.save()
      data = {
        "status": "success",
        "message": "New user added to database"
      }
      status = 201 
    except Exception as e:
      data = {
        "status": "failed",
        "message": f"failed to save data to database {e}"
      }
      status = 400
  return JsonResponse(data, status=status)