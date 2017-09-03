from django.shortcuts import render
from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from errorlog.models.models import errorLog
from django.views.generic import FormView
from django.http import HttpResponse
from time import time
import csv
# Create your views here.
template_path = "templates/"

class SearchForm(forms.Form):
    group = forms.CharField(required=False)

    required_css_class = 'bootstrap3-req'

    # Set this to allow tests to work properly in Django 1.10+
    # More information, see issue #337
    use_required_attribute = False

class IndexView(FormView):
    template_name = 'index.html'
    form_class = SearchForm

    def get_data(self, group, page):
        if group == None or group.strip() == "" :
            data = errorLog.objects.order_by("-createTime");
        else:
            data = errorLog.objects.filter(group__icontains=group).order_by("-createTime");
        paginator = Paginator(data, 10)
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        return show_lines

    def get(self, request):
        group = request.GET.get("group")
        page = request.GET.get('page')
        count = errorLog.objects.count()
        if count < 10:
            for i in range(50):
                istr = str(i)
                log = errorLog.objects.create()
                log.name = "name" + istr
                log.group = "group" + istr
                log.path = "/app/applogs/aa" + istr
                log.save()
        show_lines = self.get_data(group, page)
        return render(request,  'index.html', {'lines': show_lines, 'group': group, 'form': SearchForm})

    def post(self, request):

        group = request.POST.get('group')
        show_lines = self.get_data(group, 1)
        return render(request, 'index.html', {'lines': show_lines, 'group': group, 'form': SearchForm})

def export(request):
    group = request.GET.get("group")
    if group == None or group.strip() == "" :
        data = errorLog.objects.order_by("-createTime");
    else:
        data = errorLog.objects.filter(group__icontains=group).order_by("-createTime");
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    now = int(time())
    response['Content-Disposition'] = 'attachment; filename="export' + str(now) + '.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'group', 'path', 'create time'])
    for log in data:
        writer.writerow([log.name, log.group, log.path, log.createTime])

    return response