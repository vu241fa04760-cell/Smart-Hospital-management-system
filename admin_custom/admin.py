from .admin_site import custom_admin_site

# Register all models with custom admin site
from accounts.models import User, PatientProfile
from patients.models import Patient
from ambulance.models import Ambulance
from appointment.models import Appointment
from bedmanagement.models import Bed
from billing.models import Bill
from departments.models import Department
from doctors.models import Doctor
from hospitaltiming.models import HospitalTiming
from lab_reports.models import LabReport
from notifications.models import Notification
from nurse.models import Nurse
from pharmacy.models import Medicine
from prescriptions.models import Prescription
from staff.models import Staff

from accounts.admin import UserAdmin, PatientProfileAdmin
from patients.admin import PatientAdmin
from ambulance.admin import AmbulanceAdmin
from appointment.admin import AppointmentAdmin
from bedmanagement.admin import BedAdmin
from billing.admin import BillAdmin
from departments.admin import DepartmentAdmin
from doctors.admin import DoctorAdmin
from hospitaltiming.admin import HospitalTimingAdmin
from lab_reports.admin import LabReportAdmin
from notifications.admin import NotificationAdmin
from nurse.admin import NurseAdmin
from pharmacy.admin import MedicineAdmin
from prescriptions.admin import PrescriptionAdmin
from staff.admin import StaffAdmin

# Register all models
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(PatientProfile, PatientProfileAdmin)
custom_admin_site.register(Patient, PatientAdmin)
custom_admin_site.register(Ambulance, AmbulanceAdmin)
custom_admin_site.register(Appointment, AppointmentAdmin)
custom_admin_site.register(Bed, BedAdmin)
custom_admin_site.register(Bill, BillAdmin)
custom_admin_site.register(Department, DepartmentAdmin)
custom_admin_site.register(Doctor, DoctorAdmin)
custom_admin_site.register(HospitalTiming, HospitalTimingAdmin)
custom_admin_site.register(LabReport, LabReportAdmin)
custom_admin_site.register(Notification, NotificationAdmin)
custom_admin_site.register(Nurse, NurseAdmin)
custom_admin_site.register(Medicine, MedicineAdmin)
custom_admin_site.register(Prescription, PrescriptionAdmin)
custom_admin_site.register(Staff, StaffAdmin)
