from django.shortcuts import render

# Create your views here.
# converter/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFUploadForm
from pdf2docx import Converter
import os

def convert_pdf_to_word(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            pdf_path = os.path.join('uploads', pdf_file.name)
            with open(pdf_path, 'wb') as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)

            docx_path = pdf_path.replace('.pdf', '.docx')
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            response = HttpResponse(open(docx_path, 'rb').read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(docx_path)}'
            return response

    else:
        form = PDFUploadForm()
    return render(request, 'converter/upload.html', {'form': form})
