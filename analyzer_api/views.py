from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from setfit import SetFitModel
from .serializers import SentimentSerializer
from .models import Sentiment

#Shows an overview of the API
def index(request):
    return render(request, 'index.html')

#Analyzes the text using the pretrained model
@api_view(['POST'])
def analyze(request):
    
    text = request.data.get('text')

    try:
        existing_data = Sentiment.objects.get(text=text) # Checking if the text already exists in the database 
        serializer = SentimentSerializer(existing_data)
        return Response(serializer.data, status=200)

    except Sentiment.DoesNotExist:
    
        model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
        prediction = model([text])
        sentiemnt_data = prediction.tolist()
        sentiment = ''
        
        if sentiemnt_data[0] == 1:
            sentiment = 'positive'

        elif sentiemnt_data[0] == 0:
            sentiment = 'negative'
        
        else:
            sentiment = 'neutral'
        
    #Saving the data into the database
    data = {'text': text, 'sentiment' : sentiment}
    serializer = SentimentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)

    response_data = {"sentiment": sentiment}
    return Response(response_data, status=200)

    
#Displays all the data that has analyzed
@api_view(['GET'])
def all_analyzed(request):
    
    sentiments = Sentiment.objects.all()
    serializer = SentimentSerializer(sentiments, many=True)
    return Response(serializer.data, status=200)


#Error Handlers
def invalid_request(request, exception):
    return render(request, 'invalid_request.html', status=400)

def page_not_found(request, exception):
    return render(request, 'not_found.html', status=404)

def server_error(request):
    return render(request, 'server_error.html', status=500)