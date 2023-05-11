from django.shortcuts import render, redirect

# added below
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import models as md
# from django.urls import reverse
from .forms import InkhawmInchhiarnaBlogNewForm
from django.contrib import messages
import requests
import json


# Create your views here.


def inkhawmHome(request):
    if request.method == "POST":
        form = InkhawmInchhiarnaBlogNewForm(request.POST or None)
        if form.is_valid():
            print('Form is valid')
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            form.save()
            messages.success(
                request, ('Form submitted successfully'))
            return redirect('inkhawm:inkhawmHome')
            # return render(request, 'fillform.html', {'title': 'Fill the form'})
        else:
            print('invalid form')
            # a hming hi html a name kha a nia, a apge a mi kha name hamngin kan la a
            # we pass it again to html to the same name
            inkhawm_ni = request.POST['inkhawm_ni']
            mat_grp_cmt = request.POST['mat_grp_cmt']
            mat_members = request.POST['mat_members']
            mt_nme_total = request.POST['mt_nme_total']
            marka_grp_cmt = request.POST['marka_grp_cmt']
            marka_members = request.POST['marka_members']
            mk_nme_total = request.POST['mk_nme_total']
            luka_grp_cmt = request.POST['luka_grp_cmt']
            luka_members = request.POST['luka_members']
            lk_nme_total = request.POST['lk_nme_total']
            johan_grp_cmt = request.POST['johan_grp_cmt']
            johan_members = request.POST['johan_members']
            jh_nme_total = request.POST['jh_nme_total']
            leader_secy = request.POST['leader_secy']
            chhimtu1 = request.POST['chhimtu1']
            print(chhimtu1)
            chhimtu1_no = request.POST['chhimtu1_no']
            total = request.POST['total']
            messages.success(
                request, ('There was an error in your input data. Please Fill again!'))
            print(form.errors.as_data())
        return render(request, 'inkhawmHome.html',
                      {'page_title': 'Inkhawm app home page|Fill the form', 'ip_date_entered': inkhawm_ni,
                       'ip_matGrpcmt': mat_grp_cmt, 'ip_matMem': mat_members, 'ip_mat_total': mt_nme_total,
                       'ip_marGrpcmt': marka_grp_cmt, 'ip_marMem': marka_members, 'ip_mk_total': mk_nme_total,
                       'ip_lukaGrpcmt': luka_grp_cmt, 'ip_lukaMem': luka_members, 'ip_lk_total': lk_nme_total,
                       'ip_johanaGrpcmt': johan_grp_cmt, 'ip_johanaMem': johan_members, 'ip_jh_total': jh_nme_total,
                       'ip_leader_secy': leader_secy,
                       'ip_chhimtu1': chhimtu1, 'ip_chhimtu1_no': chhimtu1_no,
                       'ip_g_total': total,
                       'error': form.errors})
    else:
        print('get method')
        # messages = []
        print(messages)
        return render(request, 'inkhawmHome.html', {'page_title': 'Inkhawm app home page|Fill teh form'})


# class HomeView(ListView):
#     model = md.Post
#     template_name = 'home.html'

#     # this makes var my_variable accessible on html page
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Home of Blog Section'
#         # context['my_vars'] = 'nunpuia dinfela'
#         return context


def inkhawm_data(request):
    # fn based views
    # list
    endpoint = "http://127.0.0.1:8060/api/list/"

    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    # data = {"title": "create Prod.", "price": 56.5}
    get_response = requests.get(endpoint, headers)
    # print("response in text is : ", get_response.text)
    data = json.loads(get_response.text)
    # print('keys are', data[1].keys())
    # print('first element in the list is without loads', get_response.json()[1])
    # context = {'json_data': get_response.text}
    context = {'endpoint': endpoint, 'json_data': data,
               'json_js': get_response.text, "page_title": "Inkhawm Data Visualise (via API)"}
    # print("variable passed to html is", context)
    # return render(request, 'inkhawm_data.html', {'endpoint': endpoint, 'json_data': data, 'json_js': get_response.text, "funny": "ehehehhe__"})
    # return render(request, 'inkhawm_data.html', {'json_data': data, "funny": "ehehehhe__"})
    return render(request, 'inkhawm_data.html', context)
