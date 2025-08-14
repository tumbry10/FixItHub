from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Issue
from .forms import IssueReportingForm, CategoryForm, IssueUpdateForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def dashboard(request):
    profile = request.user.userprofile
    context = {
        'profile': profile,
    }
    return render(request, 'main_app/dashboard.html', context)

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, 'Category created successfully')
            return redirect('dashboard')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'main_app/create_category.html', context)

@login_required
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('dashboard')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form
    }
    return render(request, 'main_app/create_category.html', context)

@login_required
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully')
        return redirect('dashboard')
    context = {
        'category': category
    }
    return render(request, 'main_app/delete_category.html')
@login_required
def list_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main_app/list_category.html', context)

@login_required
def list_issue(request):
    user = request.user
    if user.user_type == 1:
        issues = Issue.objects.all()
    else:
        issues = Issue.objects.filter(reported_by = request.user)
    context = {
        'issues': issues
    }
    return render(request, 'main_app/list_issue.html', context)

@login_required
def create_issue(request):
    if request.method == 'POST':
        form = IssueReportingForm(request.POST)
        if form.is_valid():
            issue = form.save(commit = False)
            issue.reported_by = request.user
            issue.save()
            messages.success(request, 'Issue created successfully')
            return redirect('dashboard')
    else:
        form = IssueReportingForm()
    context = {
        'form': form
    }
    return render(request, 'main_app/create_issue.html', context)

@login_required
def update_issue(request, pk):
    issue = Issue.objects.get(id=pk)
    if request.method == 'POST':
        form = IssueUpdateForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Issue updated successfully')
            return redirect('dashboard')
    else:
        form = IssueUpdateForm(instance=issue)
    context = {
        'form': form
    }
    return render(request, 'main_app/create_issue.html', context)

@login_required
def delete_issue(request, pk):
    issue = Issue.objects.get(id=pk)
    if request.method == 'POST':
        issue.delete()
        messages.success(request, 'Issue deleted successfully')
        return redirect('dashboard')
    context = {
        'issue': issue
    }
    return render(request, 'main_app/delete_issue.html', context)

@login_required
def edit_my_issue(request, pk):
    issue = get_object_or_404(Issue, id=pk)

    #check user user_type
    if request.user.user_type != 2:
        messages.error(request, 'You are not authorized to edit this issue')
        return redirect('list_issue')
    
    #Allow only the user who created the issue
    if issue.reported_by != request.user:
        messages.error(request, 'You are not authorized to edit this issue')
        return redirect('list_issue')
    
    #Only allow editing if the status is 'Pending'
    if issue.status != 'pending':
        messages.error(request, 'You are not authorized to edit this issue, its already being actioned')
        return redirect('list_issue')
    
    if request.method == 'POST':
        form = IssueReportingForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Issue updated successfully')
            return redirect('list_issue')
        else:
            messages.error(request, 'Error updating issue')
            return redirect('edit_issue', pk=pk)
    else:
        form = IssueReportingForm(instance=issue)
    context = {
        'form': form
    }
    return render(request, 'main_app/create_issue.html', context)

def delete_my_issue(request, pk):
    issue = get_object_or_404(Issue, id=pk)
    if request.user.user_type != 2:
        messages.error(request, 'You are not authorized to delete this issue')
        return redirect('list_issue')
    if issue.reported_by != request.user:
        messages.error(request, 'You are not authorized to delete this issue')
        return redirect('list_issue')
    if issue.status != 'pending':
        messages.error(request, 'You are not authorized to delete this issue, its already being actioned')
        return redirect('list_issue')
    if request.method == 'POST':
        issue.delete()
        messages.success(request, 'Issue deleted successfully')
        return redirect('list_issue')
    context = {
        'issue': issue
    }
    return render(request, 'main_app/delete_issue.html', context)