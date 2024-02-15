from rest_framework.views import APIView
from django.http import JsonResponse
from datetime import datetime
from headcount.models import Headcount

class HeadcountTotalview(APIView):
    def get(self, request):
        # http://127.0.0.1:8000/headcount/line_chart/?init_date=2022-01-01&end_date=2022-02-01
        init_date_str = request.query_params.get('init_date')
        end_date_str = request.query_params.get('end_date')
        filter = {}

        if not init_date_str or not end_date_str:
            return JsonResponse({"error": "init_date e end_date são parâmetros necessários"}, status=400)

        try:
            init_date = datetime.strptime(init_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({"error": "Formato de data inválido. A data deve estar no formato 'aaaa-mm-dd'"}, status=400)
        
        filter['dt_reference_month__gte'] = init_date
        filter['dt_reference_month__lte'] = end_date
        filter['fg_status'] = 1

        
        if Headcount.objects.filter(**filter).values('id_employee').exists():

            queryset = Headcount.objects.filter(**filter).values('id_employee').count()
        else:
            queryset = 0
            return JsonResponse({"error": "Nenhum dado encontrado"}, status=200)

        return JsonResponse({
                            'xAxis': {
                                'type':'category',
                                'data':[
                                    queryset
                                ]
                            },
                            'yAxis': {
                                'type':'value'
                            },
                            'series': {
                                'type': 'stacked_line',
                                'series': [
                                    {
                                        'init_date': init_date_str,
                                        'end_date': end_date_str,
                                    }
                                ]
                            },
                            'Title': 'Headcount Total Ativos',
                             }, status=200)

class HeadcountTotalCategoryView(APIView):
    def get(self, request):
        #http://localhost:8000/headcount/category_charts/?init_date=2022-01-01&end_date=2022-02-01&category=2
        init_date_str = request.query_params.get('init_date')
        end_date_str = request.query_params.get('end_date')
        category = request.query_params.get('category')
        filter = {}
        
        if not end_date_str or not category:
            return JsonResponse({"error": "end_date e category são parâmetros necessários"}, status=400)

        try:
            init_date = datetime.strptime(init_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({"error": "Formato de data inválido. A data deve estar no formato 'aaaa-mm-dd'"}, status=400)
        
        filter['dt_reference_month__gte'] = end_date
        filter['dt_reference_month__lte'] = end_date
        filter['fg_status'] = 1

        
        if Headcount.objects.filter(**filter, ds_category_1=category).values('id_employee').exists():
            
            queryset = Headcount.objects.filter(**filter, ds_category_1=category).values('id_employee').count()
        
        elif Headcount.objects.filter(**filter, ds_category_2=category).values('id_employee').exists():
            
            queryset = Headcount.objects.filter(**filter, ds_category_2=category).values('id_employee').count()
        
        elif Headcount.objects.filter(**filter, ds_category_3=category).values('id_employee').exists():
            
            queryset = Headcount.objects.filter(**filter, ds_category_3=category).values('id_employee').count()
        
        elif Headcount.objects.filter(**filter, ds_category_4=category).values('id_employee').exists():
            
            queryset = Headcount.objects.filter(**filter, ds_category_4=category).values('id_employee').count()
        else:
            queryset = 0
            return JsonResponse({"error": "Nenhum dado encontrado"}, status=200)
        

        return JsonResponse({
                            "xAxis": {
                                "type": "value",
                                "show": "true",
                                "max": {}
                            },
                            "yAxis": {
                                "type": category,
                                "data": [
                                    queryset
                                ]
                            },
                            "series": {
                                "type": "horizontal_stacked",
                                "series": [
                                    {   
                                        "init_date": init_date_str,
                                        "end_date": end_date_str,
                                        "name": "Colaboradores",
                                        "data": [
                                            
                                        ],
                                        "type": ""
                                    }
                                ]
                            },
                            "title": "Empresa",
                            "grid": 6,
                            "color": [
                                "#2896DC"
                            ],
                            "is%": "False"
                        }, status=200)





    

