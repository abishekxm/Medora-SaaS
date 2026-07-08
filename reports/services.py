from .models import Report

def generate_report(author, title, report_type, data):
    return Report.objects.create(author=author, title=title, report_type=report_type, data=data)

def get_reports_by_type(report_type):
    return Report.objects.filter(report_type=report_type)
