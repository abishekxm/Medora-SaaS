def cancel_appointment(appointment):
    appointment.status = "cancelled"
    appointment.save()


def reschedule_appointment(appointment, start_time, end_time):
    appointment.start_time = start_time
    appointment.end_time = end_time
    appointment.status = "scheduled"
    appointment.save()