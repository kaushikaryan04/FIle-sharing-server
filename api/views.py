from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from .serializers import FileUploadSerializer , UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from core.settings import BASE_DIR
import os

class UploadFileView(APIView) :
    permission_classes = (IsSuperUser, )
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self , request , *args , **kwargs) : 
        file = request.FILES.get("file")
        if file :
            file_type = file.name.split(".")[-1]
            print(request.user.id)
            serializer =  self.serializer_class(data = {'file' : file , 'file_type' : file_type , "user" : request.user.id})
            if serializer.is_valid() :
                serializer.save()
                return Response({"Success" :  "File save successfull"})
            else :
                return Response({"error": "unable to save the file"})
        else :
            return Response({"error" : "No file Provided or wrong file type"})
            

    
class SignUpView(CreateAPIView):
    serializer_class = UserSerializer

class DownloadFileView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self , request , *args , **kwargs) :
        file_name = request.GET.get("file_name")
        file_path = os.path.join(BASE_DIR , "FileUploads" , file_name)
        if os.path.exists(file_path) :
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
        else :
            print(file_path)
            return Response({
                "error" : "file not found with this name and extension"
            })
