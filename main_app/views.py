from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Issue
from .forms import IssueReportingForm, CategoryForm, IssueUpdateForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'main_app/dashboard.html')

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

