from django.shortcuts import render,redirect, get_object_or_404
from cal.models import Event
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def read_api(request):
	event = Event.objects.all()
	dict_value = {"event":list(event.values('title', 'description','start_time','end_time'))}
	return JsonResponse(dict_value)

@csrf_exempt
def update_api(request, pk):
	event = Event.objects.get(pk = pk)
	if request.method == "GET":
		return JsonResponse({"title":event.title, "description":event.description, "start_time":event.start_time, "end_time":event.end_time})

	else:
		decoded_data = request.body.decode('utf-8')
		event_data = json.loads(decoded_data)
		event.title = event_data['title']
		event.description = event_data['description']
		event.start_time = event_data['start_time']
		event.end_time = event_data['end_time']
		event.save()
		return JsonResponse({"message": "Successfully updated"})

@csrf_exempt
def delete_data(request, pk):
	if request.method=='DELETE':
		event = Event.objects.get(pk = pk)
		event.delete()
		return JsonResponse({"message":"Successfully Deleted"})
		return redirect('cal:calendar')


def pagination(request, PAGENO, SIZE):
		skip = SIZE* (PAGENO -1)
		events = Event.objects.all() [skip:(PAGENO * SIZE)]
		dict = {
		"events":list(events.values("title", "description","start_time","end_time"))
		}
		return JsonResponse(dict)