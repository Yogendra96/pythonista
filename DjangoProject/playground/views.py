from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import UploadFileForm
import pandas as pd
# Create your views here.
@api_view()
def hello(request):
    return render(request, 'hello.html', {'name':'yogi'})

@api_view(['POST', 'GET'])
def upload_file(request):
    context = {'a':'b'}
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES['uploadedFile']
        print(request.FILES)
        csv = pd.read_csv(uploadedFile)
        print(csv['Sales'], csv['Sales'])
        context = get_vis(csv)
    return render(request, "upload.html", context = context)


def get_vis(csv):
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(days, counts, '--bo')

    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.set_title('sales Data')
    ax.set_ylabel("Count")
    ax.set_xlabel("item")
    ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
    ax.yaxis.set_minor_locator(LinearLocator(25))

    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    context['chart'] = b64
    return context