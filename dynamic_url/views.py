from django.shortcuts import render


def show_data(request, myid):

    template = 'dynamic_url.html'

    if myid == 1:
      context = {'myid': myid, 'name': 'Nayem Nehal', 'dept': 'Department of PLL'}
    if myid == 2:
      context = {'myid': myid, 'name': 'Maysha Mahmud', 'dept': 'Department of Math'}
    if myid == 3:
      context = {'myid': myid, 'name': 'Jakir Hossain', 'dept': 'Department of Bangla'}
    if myid == 4:
      context = {'myid': myid, 'name': 'Emran Shakil', 'dept': 'Department of English'}

    return render(request, template_name=template, context=context)
