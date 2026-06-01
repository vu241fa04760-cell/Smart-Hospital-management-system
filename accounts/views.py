from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.db.models import Q

from .forms import AppointmentRequestForm, LoginForm, SignupForm, UserForm, PatientProfileForm
from .models import PatientProfile


User = get_user_model()


DEPARTMENTS = [
    {
        "name": "Cardiology",
        "icon": "heart-pulse",
        "summary": "Heart screening, ECG review, and ongoing cardiac care.",
    },
    {
        "name": "Neurology",
        "icon": "brain",
        "summary": "Specialist care for stroke, seizures, headache, and nerve health.",
    },
    {
        "name": "Orthopedics",
        "icon": "bone",
        "summary": "Fracture care, joint pain treatment, sports injury support.",
    },
    {
        "name": "Pediatrics",
        "icon": "baby",
        "summary": "Child wellness, vaccination, nutrition, and acute care.",
    },
]

DOCTORS = [
    {"name": "Dr. Ananya Rao", "role": "Cardiologist", "shift": "09:00 AM - 02:00 PM"},
    {"name": "Dr. Vikram Singh", "role": "Neurologist", "shift": "11:00 AM - 05:00 PM"},
    {"name": "Dr. Meera Nair", "role": "Pediatrician", "shift": "10:00 AM - 04:00 PM"},
]

STATS = [
    {"value": "24/7", "label": "Emergency care"},
    {"value": "80+", "label": "Clinical staff"},
    {"value": "14", "label": "Special departments"},
    {"value": "98%", "label": "Patient satisfaction"},
]


def home(request):
    form = AppointmentRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        messages.success(request, "Appointment request received. Our team will contact you shortly.")
        return redirect("home")

    return render(
        request,
        "home.html",
        {
            "form": form,
            "departments": DEPARTMENTS,
            "doctors": DOCTORS,
            "stats": STATS,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "Welcome back.")
        return redirect("accounts:dashboard")

    return render(request, "accounts/login.html", {"form": form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        # Create patient profile for new patient users
        if user.role == User.Roles.PATIENT:
            PatientProfile.objects.create(user=user, patient_id=f"PAT-{user.id:05d}")
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("accounts:dashboard")

    return render(request, "accounts/signup.html", {"form": form})


def accounts_home(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    return redirect("accounts:login")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


@login_required
def profile_view(request):
    patient_profile = getattr(request.user, "patient_profile", None)
    return render(
        request,
        "accounts/profile.html",
        {"user_obj": request.user, "patient_profile": patient_profile},
    )


@login_required
def dashboard_redirect(request):
    if request.user.is_staff or request.user.is_superuser or request.user.is_admin_role():
        return redirect("accounts:admin_dashboard")
    return redirect("accounts:patient_dashboard")


@login_required
def admin_dashboard(request):
    """Admin dashboard with real statistics from database"""
    # Check if user is admin
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    # Get statistics from database
    total_users = User.objects.count()
    total_patients = PatientProfile.objects.count()
    total_staff = User.objects.filter(
        Q(role=User.Roles.DOCTOR) | Q(role=User.Roles.NURSE) | Q(role=User.Roles.ADMIN)
    ).count()
    verified_users = User.objects.filter(is_verified=True).count()
    
    # Get recent users
    recent_users = User.objects.order_by("-created_at")[:5]
    
    # Get staff list
    staff_list = User.objects.filter(
        Q(role=User.Roles.DOCTOR) | Q(role=User.Roles.NURSE)
    ).values("username", "first_name", "last_name", "role", "email")[:10]
    
    return render(
        request,
        "accounts/admin_dashboard.html",
        {
            "stats": [
                {"value": total_users, "label": "Total Users"},
                {"value": total_patients, "label": "Total Patients"},
                {"value": total_staff, "label": "Clinical Staff"},
                {"value": verified_users, "label": "Verified Users"},
            ],
            "recent_users": recent_users,
            "staff_list": staff_list,
            "queue": [
                "Review new user registrations",
                "Verify pending patient profiles",
                "Update staff roster",
                "Check system reports",
            ],
        },
    )


@login_required
def patient_dashboard(request):
    """Patient dashboard showing user's own data from database"""
    user = request.user
    
    # Get patient profile if exists
    patient_profile = None
    try:
        patient_profile = PatientProfile.objects.get(user=user)
    except PatientProfile.DoesNotExist:
        pass
    
    context = {
        "user": user,
        "patient_profile": patient_profile,
        "appointments": [],  # Will be populated when appointment model is used
        "prescriptions": [],  # Will be populated when prescription model is used
    }
    
    return render(request, "accounts/patient_dashboard.html", context)


@login_required
def user_list(request):
    """Display all users from database"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    users = User.objects.all().order_by("-created_at")
    return render(request, "accounts/user_list.html", {"users": users})


@login_required
def user_create(request):
    """Create a new user"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    form = UserForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        # Create patient profile if role is patient
        if user.role == User.Roles.PATIENT and not hasattr(user, 'patient_profile'):
            PatientProfile.objects.create(user=user, patient_id=f"PAT-{user.id:05d}")
        messages.success(request, f"User {user.username} created successfully.")
        return redirect("accounts:user_list")
    
    return render(request, "accounts/user_form.html", {"form": form, "title": "Create User"})


@login_required
def user_update(request, pk):
    """Update an existing user"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    user_obj = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user_obj)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"User {user_obj.username} updated successfully.")
        return redirect("accounts:user_list")
    
    return render(
        request,
        "accounts/user_form.html",
        {"form": form, "title": f"Edit User: {user_obj.username}"},
    )


@login_required
def user_delete(request, pk):
    """Delete a user"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    user_obj = get_object_or_404(User, pk=pk)
    
    if request.method == "POST":
        username = user_obj.username
        user_obj.delete()
        messages.success(request, f"User {username} deleted successfully.")
        return redirect("accounts:user_list")
    
    return render(request, "accounts/user_confirm_delete.html", {"user": user_obj})


@login_required
def patient_list(request):
    """Display all patient profiles from database"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    patients = PatientProfile.objects.select_related("user").all().order_by("-user__created_at")
    return render(request, "accounts/patient_list.html", {"patients": patients})


@login_required
def patient_create(request):
    """Create a new patient profile"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    if request.method == "POST":
        user_form = UserForm(request.POST, prefix="user")
        patient_form = PatientProfileForm(request.POST, prefix="patient")
        
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            messages.success(request, f"Patient {patient.patient_id} created successfully.")
            return redirect("accounts:patient_list")
    else:
        user_form = UserForm(prefix="user")
        patient_form = PatientProfileForm(prefix="patient")
    
    return render(
        request,
        "accounts/patient_form.html",
        {
            "user_form": user_form,
            "patient_form": patient_form,
            "title": "Create Patient",
        },
    )


@login_required
def patient_update(request, pk):
    """Update an existing patient profile"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    patient = get_object_or_404(PatientProfile, pk=pk)
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=patient.user, prefix="user")
        patient_form = PatientProfileForm(request.POST, instance=patient, prefix="patient")
        
        if user_form.is_valid() and patient_form.is_valid():
            user_form.save()
            patient_form.save()
            messages.success(request, f"Patient {patient.patient_id} updated successfully.")
            return redirect("accounts:patient_list")
    else:
        user_form = UserForm(instance=patient.user, prefix="user")
        patient_form = PatientProfileForm(instance=patient, prefix="patient")
    
    return render(
        request,
        "accounts/patient_form.html",
        {
            "user_form": user_form,
            "patient_form": patient_form,
            "title": f"Edit Patient: {patient.patient_id}",
        },
    )


@login_required
def patient_delete(request, pk):
    """Delete a patient profile"""
    if not (request.user.is_staff or request.user.is_superuser or request.user.is_admin_role()):
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    patient = get_object_or_404(PatientProfile, pk=pk)
    
    if request.method == "POST":
        patient_id = patient.patient_id
        user = patient.user
        patient.delete()
        messages.success(request, f"Patient {patient_id} deleted successfully.")
        return redirect("accounts:patient_list")
    
    return render(request, "accounts/patient_confirm_delete.html", {"patient": patient})
