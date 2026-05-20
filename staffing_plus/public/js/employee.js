
frappe.ui.form.on("Employee", {
    refresh: function (frm) {
        if (!frm.is_new()) {
			setTimeout(function () {
				frm.page.add_inner_button(__("Holiday List Assignment"), function () {
		
					frappe.db.get_value(
						'Holiday List Assignment',
						{
							assigned_to: frm.doc.name,
							applicable_for: 'Employee'
						},
						'name'
					).then(r => {
		
						if (r.message && r.message.name) {
		
							frappe.set_route(
								'Form',
								'Holiday List Assignment',
								r.message.name
							);
		
						} else {
		
							frappe.new_doc('Holiday List Assignment', {
								applicable_for: 'Employee',
								assigned_to: frm.doc.name,
								employee_name: frm.doc.employee_name,
								employee_company: frm.doc.company,
							});
		
						}
					});
				}).css({
					'background-color': '#000000',
					'color': '#ffffff',
					'border-color': '#000000'
				});
		
			}, 500);
		}

    }
})