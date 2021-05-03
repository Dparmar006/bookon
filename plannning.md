# Service

    - avg_time
    - start_time
    - end_time

# Owner

    - open_time
    - close_time

function (service_tobe_booked) => { - check of avg_time slot is available between open_time & close_time - loop through every service that day

        - if there are no services rn => service_tobe_booked.start_time = owner.open_time,
          service_tobe_booked.end_time = service_tobe_booked.start_time + service.avg_time

        - if there are service        => service_tobe_booked.start_time = last-service.end_time,
          service_tobe_booked.end_time = service_tobe_booked.start_time + service.avg_time

        - if service_tobe_booked.end_time > owner.close_time =>  { don't accept }

}
