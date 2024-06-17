import csv
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import CSVUploadForm
from .models import Company, CSVUpload
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def UploadData(request):
    return render(request, 'data.html')

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, 'csvs', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def csv_upload_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            request.session['file_path'] = file_path  # Store file path in session
            return JsonResponse({'file_path': file_path})  # Respond with file path for progress
    else:
        form = CSVUploadForm()
    return render(request, 'data.html', {'form': form})

def import_csv_to_db(file_path):
    batch_size = 1000
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        batch = []
        total_records = sum(1 for row in csvfile)  # Count total records
        csvfile.seek(0)  # Reset reader after counting
        current_record = 0
        for row in reader:
            batch.append(Company(
                cid=row['cid'],
                name=row['name'],
                domain=row['domain'],
                year_founded=row['year_founded'] or None,
                industry=row['industry'],
                size_range=row['size_range'],
                locality=row['locality'],
                country=row['country'],
                linkedin_url=row['linkedin_url'],
                current_employee_estimate=row['current_employee_estimate'],
                total_employee_estimate=row['total_employee_estimate'],
            ))
            current_record += 1
            if len(batch) >= batch_size:
                Company.objects.bulk_create(batch)
                batch = []
                yield current_record, total_records  # Yield progress
        if batch:
            Company.objects.bulk_create(batch)
            yield current_record, total_records  # Final yield to indicate completion

@csrf_exempt
def progress_import_view(request):
    file_path = request.session.get('file_path')
    if file_path:
        progress_data = import_csv_to_db(file_path)
        progress = next(progress_data, None)
        while progress:
            current, total = progress
            yield JsonResponse({'current': current, 'total': total})
            progress = next(progress_data, None)
    return JsonResponse({'current': 0, 'total': 0})