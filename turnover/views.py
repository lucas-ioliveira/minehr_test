from rest_framework.views import APIView
from django.http import JsonResponse
from datetime import datetime
from turnover.models import Turnover


class TurnoverTotalView(APIView):
    def get(self, request):
        #http://127.0.0.1:8001/turnover/line_chart/?init_date=2022-01-01&end_date=2022-02-01
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
        
        ativos_periodo = Turnover.objects.filter(**filter, fg_dismissal_on_month=0).values('fg_status').count() 
        media_ativos = ativos_periodo / 12
        media_ativos_formatada = "{:.2f}".format(media_ativos)
        media_ativos_formatada = float(media_ativos_formatada)

        soma_demitidos = Turnover.objects.filter(**filter, fg_dismissal_on_month=1).values('fg_dismissal_on_month').count()
        soma_demitidos = "{:.2f}".format(soma_demitidos)
        soma_demitidos = float(soma_demitidos)

        id_matricula = Turnover.objects.filter(**filter).values('id_employee').count()
        id_matricula = "{:.2f}".format(id_matricula)
        id_matricula = float(id_matricula)

        calc = (soma_demitidos / media_ativos_formatada) * 100
        calc = "{:.2f}".format(calc)
        calc = float(calc)

        return JsonResponse({
                               "xAxis": {
                                    "type": "category",
                                    "data": [
                                        calc
                                    ]
                                },
                                "yAxis": {
                                    "type": "value"
                                },
                                "series": {
                                    "type": "stacked_line",
                                    "series": [
                                        {
                                            'init_date': init_date_str,
                                            'end_date': end_date_str,
                                            "type": "line",
                                            "data": [
                                                
                                            ]
                                        },
                                    ]
                                },
                                "title": "Taxa de Turnover por Ano (%)",
                                "grid": 6,
                                "color": [
                                    "#D4DDE2",
                                    "#A3B6C2"
                                ]
                            }, status=200)

class TurnoverTotalCategoryView(APIView):
    def get(self, request):
        #http://localhost:8001/turnover/category_charts/?init_date=2022-01-01&end_date=2022-03-01&category=Cookfurt
        init_date_str = request.query_params.get('init_date')
        end_date_str = request.query_params.get('end_date')
        category = request.query_params.get('category')
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
        
        ativos_periodo = Turnover.objects.filter(**filter, fg_dismissal_on_month=0).values('fg_status').count() 
        media_ativos = ativos_periodo / 12
        media_ativos_formatada = "{:.2f}".format(media_ativos)
        media_ativos_formatada = float(media_ativos_formatada)

        soma_demitidos = Turnover.objects.filter(**filter, fg_dismissal_on_month=1).values('fg_dismissal_on_month').count()
        soma_demitidos = "{:.2f}".format(soma_demitidos)
        soma_demitidos = float(soma_demitidos)

        if Turnover.objects.filter(**filter, ds_category_1=category).values('id_employee').exists():
            id_matricula = Turnover.objects.filter(**filter, ds_category_1=category).values('id_employee').count()
        elif Turnover.objects.filter(**filter, ds_category_2=category).values('id_employee').exists():
            id_matricula = Turnover.objects.filter(**filter, ds_category_2=category).values('id_employee').count()
        elif Turnover.objects.filter(**filter, ds_category_3=category).values('id_employee').exists():
            id_matricula = Turnover.objects.filter(**filter, ds_category_3=category).values('id_employee').count()
        elif Turnover.objects.filter(**filter, ds_category_4=category).values('id_employee').exists():
            id_matricula = Turnover.objects.filter(**filter, ds_category_4=category).values('id_employee').count()
        elif Turnover.objects.filter(**filter, ds_category_5=category).values('id_employee').exists():
            id_matricula = Turnover.objects.filter(**filter, ds_category_5=category).values('id_employee').count()
        else:
            id_matricula = 0

        id_matricula = "{:.2f}".format(id_matricula)
        id_matricula = float(id_matricula)

        calc = (soma_demitidos / media_ativos_formatada) * 100
        calc = "{:.2f}".format(calc)
        calc = float(calc)

        return JsonResponse({
                               "xAxis": {
                                    "type": category,
                                    "data": [
                                        calc
                                    ]
                                },
                                "yAxis": {
                                    "type": "value"
                                },
                                "series": {
                                    "type": "stacked_line",
                                    "series": [
                                        {
                                            'init_date': init_date_str,
                                            'end_date': end_date_str,
                                            "type": "line",
                                            "data": [
                                                
                                            ]
                                        },
                                    ]
                                },
                                "title": "Taxa de Turnover por Ano (%)",
                                "grid": 6,
                                "color": [
                                    "#D4DDE2",
                                    "#A3B6C2"
                                ]
                            }, status=200)