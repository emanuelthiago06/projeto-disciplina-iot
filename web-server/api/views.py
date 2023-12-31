from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from api.models import Sensor
from django.utils import timezone
from .forms import YourForm
import pandas as pd
from tensorflow import keras


def create_csv_from_data(lista):
    columns = ["x"+str(i) for i in range(len(lista))]
    db = pd.DataFrame(columns=columns)
    for i in range(8):
        db.loc[i] = lista
    return db

def determine_infart(predict_list):
    for i in predict_list:
        if i >0.2:
            return "Paciente com Infarto" 
    return "normal"

def initial_page(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Redirect to the other page with form data
            return HttpResponseRedirect('/iot/graph/?field=' + form.cleaned_data['id_do_sensor'])
    else:
        form = YourForm()

    return render(request, 'initial_page.html', {'form': form})

def test_model(db):
    loaded_model = keras.models.load_model("detection_model.h5")
    predictions = loaded_model.predict(db)
    predit = determine_infart(predictions)
    return predit

def view_graph(request):
    if request.method == "POST" and "clean_database" in request.POST:
        Sensor.objects.all().delete()
        form = YourForm(request.POST)
        return render(request, 'initial_page.html', {'form': form})
    predit = "normal"
    id = request.GET.get('field', '')
    data = []
    dates =[]
    bellow_1_count = []
    sensores = Sensor.objects.all()
    count = 0
    for i in sensores:
        if i.id_personal != int(id):
            continue
        date = i.created_at
        if not date:
            continue
        data.append(i.value)
        if len(data)%18==0:
            db = create_csv_from_data(data[count-17:count+1])
            predit = test_model(db)
        if i.value < 1:
            bellow_1_count.append(i.value)
        dates.append(date.strftime("%Y-%m-%d %H:%M"))
        count+=1
    print(bellow_1_count)

    context = {
        'data': data,
        'labels': dates,
        'below_1_count': len(bellow_1_count),
        'average_value': 0 if not data else sum(data)/len(data),
        'status': predit
    }
    return render(request, 'plot.html', context)


@csrf_exempt
def add_point(request):
    try:
        if request.method == "POST":
            value = float(request.POST.get('value', "id"))
            id = int(request.POST.get("id"))
            print(value)
            new_entry = Sensor(id_personal=id,value=value, created_at= timezone.now())
            new_entry.save()
            return JsonResponse({
                "mensagem": "Dado armazenado com sucesso",
                "status" : 200
            })
    except:
        return JsonResponse({
                "mensagem": "Erro no request",
                "status" : 400
            })
