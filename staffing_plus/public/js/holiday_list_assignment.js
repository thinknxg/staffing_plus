frappe.ui.form.on("Holiday List Assignment", {
    after_save: function (frm) {
		const employee = localStorage.getItem("holiday_list_assignment_return_employee");
		if (employee) {
			setTimeout(function() {
				localStorage.removeItem("holiday_list_assignment_return_employee");
				frappe.set_route("Form", "Employee", employee);
			}, 1000);
		}
	},

	on_submit: function (frm) {
		const employee = localStorage.getItem("holiday_list_assignment_return_employee");
		if (employee) {
			setTimeout(function() {
				localStorage.removeItem("holiday_list_assignment_return_employee");
				frappe.set_route("Form", "Employee", employee);
			}, 1000);
		}
	},
})