from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import my_async_task, scrape_webpage_async
from celery.result import AsyncResult
# Create your views here.


class MyView(APIView):
    def get(self, request):
        number1 = request.GET.get('number1')
        number2 = request.GET.get('number2')
        task = my_async_task.delay(int(number1), int(number2))
        return Response({'task_id': task.id})

class MyViewResult(APIView):
    def get(self, request):
        task_id = request.query_params.get('task_id')
        result = AsyncResult(task_id)
        data = result.get()
        return Response({'result': data})
    

class WebScrap(APIView):

    def get(self, request):
        url = request.query_params.get('url')
        task = scrape_webpage_async.delay(url)
        return Response({'task_id': task.id})

class WebScrapResult(APIView):

    def get(self, request):
        task_id = request.query_params.get('task_id')
        result = AsyncResult(task_id)
        # Return an HTTP response that includes the task result
        if result.successful():
            # Task completed successfully; retrieve result
            data = result.get()
            # Do something with the result
            return Response({'status': 'success', 'data': data})
        elif result.failed():
            # Task failed to complete; retrieve exception
            exception = result.result
            # Do something with the exception
            return Response({'status': 'error', 'message': str(exception)})
        else:
            # Task is still running
            return Response({'status': 'running'})