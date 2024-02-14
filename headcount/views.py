from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime
from .models import Headcount
from ipdb import set_trace

class HeadcountTotalview(APIView):
    def get(self, request):
        # http://127.0.0.1:8001/headcount/line_chart/?init_date=2022-01-01&end_date=2022-02-01
        init_date_str = request.query_params.get('init_date')
        end_date_str = request.query_params.get('end_date')

        if not init_date_str or not end_date_str:
            return JsonResponse({"error": "init_date e end_date são parâmetros necessários"}, status=400)

        try:
            init_date = datetime.strptime(init_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({"error": "Formato de data inválido. A data deve estar no formato 'aaaa-mm-dd'"}, status=400)

        
        queryset = Headcount.objects.filter(dt_reference_month__gte=init_date, dt_reference_month__lte=end_date, 
                                    fg_status=1).values('id_employee').count()

        return JsonResponse({'headcount_total_ativos': queryset,}, status=200)

# class HeadcountTotalCategoryView(APIView):
#     def get(self, request):
#         set_trace()
#         # http://127.0.0.1:8001/headcount/line_chart/?init_date=2022-01-01&end_date=2022-02-01&category=
#         init_date_str = request.query_params.get('init_date')
#         end_date_str = request.query_params.get('end_date')
#         category = request.query_params.get('category')
        
#         if not end_date_str or not category:
#             return JsonResponse({"error": "end_date e category são parâmetros necessários"}, status=400)

#         try:
#             init_date = datetime.strptime(init_date_str, '%Y-%m-%d')
#             end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
#         except ValueError:
#             return JsonResponse({"error": "Formato de data inválido. A data deve estar no formato 'aaaa-mm-dd'"}, status=400)
        
#         filter = {}
#         if category == 'ds_category_1':
#             filter['ds_category_1'] = category
#         elif category == 'ds_category_2':
#             filter['ds_category_2'] = category
#         elif category == 'ds_category_3':
#             filter['ds_category_3'] = category
#         elif category == 'ds_category_4':
#             filter['ds_category_4'] = category
#         elif category == 'ds_category_5':
#             filter['ds_category_5'] = category
        
#         queryset = Headcount.objects.filter(dt_reference_month__gte=init_date, dt_reference_month__lte=end_date,
#                                              fg_status=1, **filter).values('id_employee').count()

#         return JsonResponse({'headcount_total_ativos_category': queryset}, status=200)
class HeadcountTotalCategoryView(APIView):
    def get(self, request):
        set_trace()
        init_date_str = request.query_params.get('init_date')
        end_date_str = request.query_params.get('end_date')
        category = request.query_params.get('category')
        
        if not end_date_str or not category:
            return JsonResponse({"error": "end_date e category são parâmetros necessários"}, status=400)

        try:
            init_date = datetime.strptime(init_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({"error": "Formato de data inválido. A data deve estar no formato 'aaaa-mm-dd'"}, status=400)
        
        filter = {}
        if category in ['ds_category_1', 'ds_category_2', 'ds_category_3', 'ds_category_4', 'ds_category_5']:
            filter[category] = category
        
        queryset = Headcount.objects.filter(dt_reference_month__gte=init_date, dt_reference_month__lte=end_date,
                                             fg_status=1, **filter).values('id_employee').count()

        return JsonResponse({'headcount_total_ativos_category': queryset}, status=200)


    

