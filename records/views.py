from django.shortcuts import render, redirect, get_object_or_404
from .models import Record

def record_list(request):
    records = Record.objects.all()
    return render(request, 'records/record_list.html',{'records':records})

def create_record(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        Record.objects.create(
            title = title,
            description = description,
            file = file,
        )
        return redirect('record_list')
    return render(request, 'records/create_record.html')

def update_record(request, pk):
    record = get_object_or_404(Record, pk = pk)

    if request.method == 'POST':
        record.title = request.POST.get('title')
        record.description = request.POST.get('description')

        if request.FILES.get('file'):
            record.file = request.FILES.get('file')

        record.save()
        return redirect('record_list')
    return render(request, 'records/update_record.html', {'record':record})

def delete_record(request, pk):
    record = Record.objects.get(id = pk)
    record.delete()
    return redirect('record_list')

def view_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'records/view_record.html', {'record': record})