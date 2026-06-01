from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from django.db.models import Count, Q


class CustomAdminSite(AdminSite):
    site_header = "Smart Hospital Management"
    site_title = "Hospital Admin"
    index_title = "Dashboard"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
            path('api/search/', self.admin_view(self.api_search), name='api_search'),
            path('api/stats/', self.admin_view(self.api_stats), name='api_stats'),
        ]
        return custom_urls + urls
    
    def dashboard_view(self, request):
        """Render interactive dashboard with statistics"""
        from django.http import JsonResponse
        from accounts.models import User
        from patients.models import Patient
        from doctors.models import Doctor
        from appointment.models import Appointment
        from bedmanagement.models import Bed
        from billing.models import Bill
        
        stats = {
            'total_users': User.objects.count(),
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'active_appointments': Appointment.objects.filter(status='PENDING').count(),
            'occupied_beds': Bed.objects.filter(status='OCCUPIED').count(),
            'total_beds': Bed.objects.count(),
            'pending_bills': Bill.objects.filter(status='UNPAID').count(),
            'total_revenue': sum(bill.total_amount for bill in Bill.objects.all()),
        }
        
        recent_appointments = Appointment.objects.all().order_by('-created_at')[:5]
        recent_patients = Patient.objects.all().order_by('-registered_at')[:5]
        
        context = {
            **self.each_context(request),
            'stats': stats,
            'recent_appointments': recent_appointments,
            'recent_patients': recent_patients,
            'title': 'Hospital Dashboard',
        }
        
        return render(request, 'admin/dashboard.html', context)
    
    def api_search(self, request):
        """API endpoint for live search"""
        from django.http import JsonResponse
        from patients.models import Patient
        from doctors.models import Doctor
        from accounts.models import User
        
        query = request.GET.get('q', '')
        
        if len(query) < 2:
            return JsonResponse({'results': []})
        
        results = {
            'patients': list(Patient.objects.filter(
                Q(full_name__icontains=query) | Q(patient_id__icontains=query)
            ).values('id', 'patient_id', 'full_name')[:5]),
            'doctors': list(Doctor.objects.filter(
                Q(user__first_name__icontains=query) | Q(specialization__icontains=query)
            ).values('id', 'specialization')[:5]),
            'users': list(User.objects.filter(
                Q(username__icontains=query) | Q(email__icontains=query)
            ).values('id', 'username', 'email')[:5]),
        }
        
        return JsonResponse({'results': results})
    
    def api_stats(self, request):
        """API endpoint for live statistics"""
        from django.http import JsonResponse
        from patients.models import Patient
        from doctors.models import Doctor
        from appointment.models import Appointment
        from bedmanagement.models import Bed
        from billing.models import Bill
        
        stats = {
            'patients': Patient.objects.count(),
            'doctors': Doctor.objects.count(),
            'appointments': {
                'pending': Appointment.objects.filter(status='PENDING').count(),
                'confirmed': Appointment.objects.filter(status='CONFIRMED').count(),
                'completed': Appointment.objects.filter(status='COMPLETED').count(),
            },
            'beds': {
                'available': Bed.objects.filter(status='AVAILABLE').count(),
                'occupied': Bed.objects.filter(status='OCCUPIED').count(),
            },
            'bills': {
                'unpaid': Bill.objects.filter(status='UNPAID').count(),
                'paid': Bill.objects.filter(status='PAID').count(),
            }
        }
        
        return JsonResponse({'stats': stats})
    
    def index(self, request, extra_context=None):
        """Override index to show dashboard"""
        from patients.models import Patient
        from doctors.models import Doctor
        from accounts.models import User
        from appointment.models import Appointment
        
        if extra_context is None:
            extra_context = {}
        
        # Add dashboard stats to context
        extra_context.update({
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_users': User.objects.count(),
            'pending_appointments': Appointment.objects.filter(status='PENDING').count(),
        })
        
        return super().index(request, extra_context)


custom_admin_site = CustomAdminSite(name='custom_admin')
