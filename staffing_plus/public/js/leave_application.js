frappe.ui.form.on("Leave Application", {
    refresh: function(frm) {

        // Only show after document is saved
        if (!frm.is_new()) {

            const timesy = localStorage.getItem("leave_application_return_timesy");

            // if (timesy) {

                frm.add_custom_button(__('Back to Timesy'), function() {

                    localStorage.removeItem("leave_application_return_timesy");

                    frappe.set_route("Form", "Timesy", timesy);

                });
            // }
        }
    },

	on_submit: function (frm) {
    const timesy = localStorage.getItem("leave_application_return_timesy");
    // Always mark absent when leave is submitted and approved
    if (frm.doc.status === 'Approved' && frm.doc.employee) {
        frappe.call({
            method: 'staffing.staffing.doctype.timesy.timesy.mark_leave_as_absent',
            args: {
                employee_code: frm.doc.employee,
                from_date: frm.doc.from_date,
                to_date: frm.doc.to_date
            },
            callback: function(r) {
                if (r.message === 'success') {
                    frappe.show_alert({
                        message: 'Leave dates marked as Absent in Timesy and Attendance',
                        indicator: 'green'
                    })
                }
            }
        })
    }

    if (timesy) {
        setTimeout(function () {
            localStorage.removeItem("leave_application_return_timesy");
            frappe.set_route("Form", "Timesy", timesy);
        }, 1500);
    }
    }
    
})