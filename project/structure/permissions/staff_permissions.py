def staff_required(user):
    return user.is_authenticated and user.is_staff
