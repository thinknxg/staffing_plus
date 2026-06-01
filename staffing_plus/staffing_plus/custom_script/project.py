import frappe


def set_project_name_from_lead(doc, method):
    # Run only for new projects
    if not doc.is_new():
        return

    if not doc.custom_lead:
        return

    # Convert L10001 -> P10001
    project_name = doc.custom_lead.replace("E", "P", 1)

    # Check if already exists
    if frappe.db.exists("Project", project_name):
        frappe.throw(f"Project {project_name} already exists")

    doc.name = project_name
    # doc.project_name = project_name