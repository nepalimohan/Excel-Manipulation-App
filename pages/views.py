import pyexcel
import socket
import secrets

from django.shortcuts import render
from django.views import View
from django.core.files.storage import default_storage
from ip2geotools.databases.noncommercial import DbIpCity

from .models import Files, userInfo
from django.urls import resolve


class ExcelView(View):
    def get(self, request):
        current_url = request.build_absolute_uri()
    
        print('*****',current_url)
        
        try:
            IP = socket.gethostbyname(current_url)
            response = DbIpCity.get(IP, api_key='free')
            
            print("IP:", IP)
            print("City:", response.city)
            print("Region:", response.region) 
            print("Country:", response.country)
            
            info = userInfo.objects.create(ip=IP, city= response.city, 
                                        region=response.region, country= response.country)
            
            data = {
                'info': info,
            }
            return render(request, 'base.html', data)
            
        except:
            data = {
                'error': 'IP not fetched'
            }
        return render(request, 'base.html', data)
    
    def post(self, request):
        #getting primary file from form
        primary_file = request.FILES['primary']
        primary_sheet = pyexcel.iget_records(file_type='xlsx',file_content=primary_file.read(), name_columns_by_row=0)
        
        #getting secondary file from form
        secondary_file = request.FILES['secondary']
        secondary_sheet = pyexcel.iget_records(file_type='xlsx',file_content=secondary_file.read())
        
        primary_dict = {}
        secondary_dict = {}
        
        for primary_data in primary_sheet:
            primary_dict[primary_data['Name']] = primary_data['Age']
        # print(primary_dict)
        
        
        for secondary_data in secondary_sheet:
            secondary_dict[secondary_data['Name']] = secondary_data['Age']
        # print(secondary_dict)
        
        sheet = pyexcel.Sheet()
        sheet.row+= ['Name', 'Age']
        
        sheet1 = pyexcel.Sheet()
        sheet1.row+= ['Name', 'Age']
        
        sheet2 = pyexcel.Sheet()
        sheet2.row+= ['Name', 'Age']
        
        diff = set(secondary_dict.keys()) - set(primary_dict.keys())
        diff_dict = dict.fromkeys(diff)
        diff_dict = {key: secondary_dict[key] for key in diff_dict.keys()}
        for key1, value1 in diff_dict.items():
            # print(key1, value1)
            sheet1.row+= [key1, value1]
            
        #to find and store unique keys present in primary file/1st file data
        diff_in_primary = set(primary_dict.keys()) - set(secondary_dict.keys())
        diff_dict_primary = dict.fromkeys(diff_in_primary)
        diff_dict_primary = {key: primary_dict[key] for key in diff_dict_primary.keys()}
        # print(diff_dict_primary)
        for key1, value1 in diff_dict_primary.items():
            # print(key1, value1)
            sheet2.row+= [key1, value1]
        
        for key, value in primary_dict.items():
            for name, age in secondary_dict.items():
                if key == name:
                    sheet.row+= [name, age]
                    break
                    # print(key ,name)
                else:
                    pass
        
        sheet_file = secrets.token_hex(3)
        sheet_file1 = secrets.token_hex(4)
        sheet_file2 = secrets.token_hex(2)
        
        
        sheet.save_as(f'media/changed_values{sheet_file}.xlsx')
        sheet1.save_as(f'media/unique_values_second_file{sheet_file1}.xlsx')
        sheet2.save_as(f'media/unique_values_first_file{sheet_file2}.xlsx')
        print(sheet_file)
        
        changed_values_path = default_storage.url(f'changed_values{sheet_file}.xlsx')
        print(changed_values_path)
        unique_values_second_path = default_storage.url(f'unique_values_second_file{sheet_file1}.xlsx')
        unique_values_first_path = default_storage.url(f'unique_values_first_file{sheet_file2}.xlsx')
        
        file = Files.objects.create(changed_values=changed_values_path, 
                                    uniquevalues_two=unique_values_second_path,
                                    uniquevalues_one=unique_values_first_path)
        
        data = {
            'file': file,
        }
        
        print(request.path)
        
        return render(request, 'base.html', data)