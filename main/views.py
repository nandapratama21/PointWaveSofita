from django.shortcuts import render
import os
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import random
import sys
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

# Create your views here.

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)


@csrf_exempt
def compile_code(request):
    if request.method == 'POST':
        language = request.POST.get('language', '').lower()
        code = request.POST.get('code', '')

        # random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
        # file_path = f"temp/{random_name}.{language}"

        # with open(file_path, 'w') as program_file:
        #     program_file.write(code)

        original = sys.stdout

        try:
            result = 0
            start_time = time.time()
            if language == "php":
                output = os.popen(f"C:/wamp64/bin/php/php5.6.40/php.exe {file_path} 2>&1").read()
            elif language == "python":
                #output = os.popen(f"C:/Users/KOUSIK/AppData/Local/Programs/Python/Python39/python.exe {file_path} 2>&1").read()
                
                sys.stdout = open('file.txt','w')
                start_time = time.time()
                exec(code)
                end_time = time.time()
                sys.stdout.close()

                sys.stdout = original

                result = round(end_time - start_time, 3)
                output = open('file.txt','r').read()

            elif language == "node":
                os.rename(file_path, f"{file_path}.js")
                output = os.popen(f"node {file_path}.js 2>&1").read()
            elif language in ["c", "cpp"]:
                output_exe = f"{random_name}.exe"
                os.system(f"gcc {file_path} -o {output_exe}")
                output = os.popen(os.path.join(os.path.dirname(__file__), output_exe)).read()
            else:
                output = "Unsupported language"
            response_data = {
                'success': True,
                'output': output,
                'result': str(result) + " seconds" if language == "python" else None,
            }
        except Exception as e:
            end_time = time.time()
            result = round(end_time - start_time, 3)
            sys.stdout = original
            output = e
            response_data = {
                'success': False,
                'output': str(e),
                'result': str(result) + " seconds" if language == "python" else None,
                'status': "Runtime Error"
            
                
            }

        return JsonResponse(response_data)

    return HttpResponse("Invalid request method")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def upload_file(request):
    global file_content
    if request.method == 'POST':
        # Mendapatkan file dari request.FILES
        try:
            uploaded_file = request.FILES['testcase_file']
            file_content = uploaded_file.read()
            # Mengonversi byte menjadi string
            file_content_str = file_content.decode('utf-8', 'ignore')

            # Lakukan sesuatu dengan file, misalnya, simpan ke sistem file atau lakukan pemrosesan lainnya
            # ...

            # Kirim respons JSON sebagai konfirmasi
            return JsonResponse({'message': 'File berhasil diunggah.'})
        except:
            return JsonResponse({'message': 'File tidak diupload.'})


    return JsonResponse({'message': 'Metode HTTP tidak valid.'}, status=400)