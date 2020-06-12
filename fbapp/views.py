from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import a,PhotoPost,Comment
from .forms import UserUpdate,ProfileUpdate,PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.http import HttpResponse



class PostDetail(DetailView):
    template_name = "PostDetail.html"
    model = PhotoPost
    context_object_name = "photopost"



def CreateComment(request,**kwargs):
    com=request.POST["comment"]


    FORM = Comment(comment=com,user=request.user,post_connected=request.self.get_object_or_404())
    if FORM.is_valid():
        FORM.save()
        return redirect("home")

    #return HttpResponse("Hi")




class CreatePost(LoginRequiredMixin, CreateView):


    model = PhotoPost
    fields = ["caption","photo"]
    success_url = "home"



    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)










def Login(request):
    if request.method=="POST":
        uname=request.POST["username"]
        passw=request.POST["password"]
        user=authenticate(username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect("home")

        else:
            messages.warning(request,"username or Password incorrect!")







def index(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        ph = request.POST['ph']
        password = request.POST['pass']
        birth=request.POST['b']
        g=request.POST['g']
        username=ph.split('@')[0]

        if User.objects.filter(email=ph).exists():
            messages.info(request, "email or ph no already exists!")
            return redirect("/home/")
        else:
            k = a.objects.create_user(password=password, username=username, first_name=fname, last_name=lname, email=ph,gender=g,
                                         birth=birth,)
            k.save()
            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect("profile")



    else:

        return render(request, "facebook.html")
@login_required
def home(request):
    photopost=PhotoPost.objects.all()


    return render(request,"fbhome.html",{"photopost":photopost,"cform":PostComment})

@login_required
def Profile(request):
    if request.method=="POST":

        uform=UserUpdate(request.POST,instance=request.user)
        pform=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.info(request,"updated successfully!")

            return redirect("profile")

    else:
        uform=UserUpdate(instance=request.user)
        pform=ProfileUpdate(instance=request.user.profile)

        context={
            "uform":uform,
            "pform":pform,
        }
    return render(request,"profile.html",context)
