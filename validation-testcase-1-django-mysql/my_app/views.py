from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from my_app.models import InfoModel
from .forms import InfoForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            salary = form.cleaned_data['salary']
            print(fname)
            print(salary)

            if fname and salary:
                db_fn_isqual_to_post_fn = InfoModel.objects.filter(f_name=fname)
                if db_fn_isqual_to_post_fn:
                    messages.error(request, f'{fname} is already exist')
                    # form = InfoForm(request.POST)
                # ----------------------#
                else:
                    addinfo = InfoModel(f_name=fname, salary=salary)
                    addinfo.save()
                    messages.success(request, f'Data has been Added!')
    else:
        form = InfoForm()

    context = {
        'info': InfoModel.objects.all(),
        'form': form
    }
    return render(request, 'index.html', context)


def delete(request, pk):
    delete_item = InfoModel.objects.filter(pk=pk)
    delete_item.delete()
    return redirect('home')
