import groupdocs_conversion_cloud
from flask import send_from_directory, render_template
from shutil import copyfile
import os
from PyPDF2 import PdfFileReader
from app import DOWNLOAD_FOLDER, app
# add 'uploads' folder to the project's root directory where uploaded files could be saved


# groupdocx API settings
api_sid = os.environ.get('APP_SID')
api_key = os.environ.get('APP_KEY')

def pdfToDocx(filename, remote_name, output_name):
        app_sid = api_sid
        app_key = api_key
        print("KEYS accepted")
        # no. of pages in pdf file
        print(app.config['UPLOAD_FOLDER']+remote_name)
        file  = PdfFileReader(open(app.config['UPLOAD_FOLDER']+remote_name,'rb'))
        page_counts = file.getNumPages()
        print("Number of pages: ", page_counts)
        print("Download path: ", app.config['DOWNLOAD_FOLDER']+output_name)
        # Create instance of the API
        convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
        file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

        try:

                #upload soruce file to storage
                filename = filename
                remote_name = remote_name
                output_name= remote_name.rsplit('.')[0]+'.docx'
                strformat='docx'
                print(filename, remote_name, output_name)

                request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name,filename)
                print("upload request")
                response_upload = file_api.upload_file(request_upload)
                print("uploaded to the cloud")
                        #Convert PDF to Word document
                settings = groupdocs_conversion_cloud.ConvertSettings()
                settings.file_path =remote_name
                settings.format = strformat
                settings.output_path = output_name
                print("converted to docx")

                loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
                loadOptions.hide_pdf_annotations = True
                loadOptions.remove_embedded_files = False
                loadOptions.flatten_all_fields = True

                settings.load_options = loadOptions

                convertOptions = groupdocs_conversion_cloud.DocxConvertOptions()
                convertOptions.from_page = 1
                convertOptions.pages_count = int(page_counts)

                settings.convert_options = convertOptions

                request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
                response = convert_api.convert_document(request)
                
                print("Document converted successfully: " + str(response))
                # Download request
                request_download = groupdocs_conversion_cloud.DownloadFileRequest(output_name)
                response_download = file_api.download_file(request_download)
                print("Response Download ", response_download)
                copyfile(response_download,
                        app.config['DOWNLOAD_FOLDER']+output_name)
                
                print("Successful")
        except groupdocs_conversion_cloud.ApiException as e:
                print("Exception when calling get_supported_conversion_types: {0}".format(e.message))
                return render_template("api_exception.html")
        

