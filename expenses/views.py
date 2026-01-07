from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Expense
from datetime import date,datetime
from django.db.models import Sum
from django.views.decorators.cache import never_cache

# Create your views here.
@login_required(login_url='login')
@never_cache
def home(request):
    selected_category = request.GET.get('category', '')

    if selected_category:
        expenses = Expense.objects.filter(user=request.user, category=selected_category).order_by('-date')
    else:
        expenses = Expense.objects.filter(user=request.user).order_by('-date')

    today = date.today()
    month = today.month

    today_total = Expense.objects.filter(user=request.user, date=today).aggregate(Sum('amount'))['amount__sum'] or 0
    month_total = Expense.objects.filter(user=request.user, date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
    all_total = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'expenses': expenses,
        'today_total': today_total,
        'month_total': month_total,
        'all_total': all_total,
        'selected_category': selected_category,
    }

    return render(request, 'home.html', context)
@login_required(login_url='login')
@never_cache
def add_expenses(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date_str = request.POST['date']  
        expense_date = datetime.strptime(date_str, '%Y-%m-%d').date()  

        Expense.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            category=category,
            date=expense_date
        )
        messages.success(request, 'Expense added successfully!')
        return redirect('home')

    return render(request, 'add_expenses.html')
@login_required(login_url='login')
@never_cache
def delete_expenses(request, expense_id):  
    try:
        expense = Expense.objects.get(id=expense_id, user=request.user)
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    except Expense.DoesNotExist:
        messages.error(request, 'Expense not found or unauthorized.')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')  

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('home')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def profile_view(request):
    return render(request, 'profile.html')

@login_required
def settings_view(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        #  Update email if changed
        if email and email != user.email:
            user.email = email
            user.save()
            messages.success(request, "Email updated successfully!")

        #  Handle password change
        if old_password or new_password or confirm_password:
            if not old_password:
                messages.error(request, "Please enter your old password.")
            elif not user.check_password(old_password):
                messages.error(request, "Old password is incorrect.")
            elif new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in after password change
                messages.success(request, "Password changed successfully!")

    return render(request, 'settings.html')

@login_required
def update_expenses(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        messages.success(request, 'Expense updated successfully!')
        return redirect('home')

    return render(request, 'update_expenses.html', {'expense': expense})
