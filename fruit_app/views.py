from testdaten.base import fruits #ich habe die Liste in eine globale Datei ausgelagert, damit die view übersichtlicher bleibt.
from django.http import HttpResponse #, JsonResponse
#import json

# Create your views here.
def send_fruit_list(request):
                    
    return HttpResponse(f"<!DOCTYPE html> {fruits}")
    