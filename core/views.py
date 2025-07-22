from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Client
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")  # ⛔ Login failed
            return redirect('login')  # Or re-render login with context
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Or wherever your login view is


@login_required
def dashboard(request):
    clients = Client.objects.all()
    return render(request, 'dashboard.html', {'clients': clients})

@login_required
def add_client(request):
    if request.method == 'POST':
        Client.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            company=request.POST['company'],
            onboarding_date=request.POST['onboarding_date'],
            status=request.POST['status'],
            services_required=request.POST['services_required'],
            created_by=request.user
        )
        return redirect('dashboard')
    return render(request, 'add_client.html')


def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    status_options = ['Pending', 'In Progress', 'Completed', 'On Hold', 'Cancelled']

    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone = request.POST.get('phone')
        client.company = request.POST.get('company')
        client.onboarding_date = request.POST.get('onboarding_date')
        client.status = request.POST.get('status')
        client.services_required = request.POST.get('services_required')
        client.save()
        return redirect('dashboard')

    return render(request, 'edit_client.html', {
        'client': client,
        'status_options': status_options  # 👈 pass list here
    })

def client_report(request):
    status_filter = request.GET.get('status', '')
    if status_filter:
        clients = Client.objects.filter(status=status_filter)
    else:
        clients = Client.objects.all()

    status_options = ['Pending', 'In Progress', 'Completed', 'On Hold', 'Cancelled']
    return render(request, 'client_report.html', {
        'clients': clients,
        'status_filter': status_filter,
        'status_options': status_options,
    })

def client_report_pdf(request):
    status_filter = request.GET.get('status')
    clients = Client.objects.all()

    if status_filter:
        clients = clients.filter(status=status_filter)

    template_path = 'client_report_pdf.html'
    context = {'clients': clients}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="client_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation failed', status=500)

    return response



