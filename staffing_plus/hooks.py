app_name = "staffing_plus"
app_title = "Staffing Plus"
app_publisher = "thinkNxg"
app_description = "Staffing Plus"
app_email = "thinkNxg@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "staffing_plus",
# 		"logo": "/assets/staffing_plus/logo.png",
# 		"title": "Staffing Plus",
# 		"route": "/staffing_plus",
# 		"has_permission": "staffing_plus.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/staffing_plus/css/staffing_plus.css"
# app_include_js = "/assets/staffing_plus/js/staffing_plus.js"

# include js, css files in header of web template
# web_include_css = "/assets/staffing_plus/css/staffing_plus.css"
# web_include_js = "/assets/staffing_plus/js/staffing_plus.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "staffing_plus/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Employee" : "public/js/employee.js",
    "Holiday List Assignment" : "public/js/holiday_list_assignment.js",
    "Leave Application" : "public/js/leave_application.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "staffing_plus/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "staffing_plus.utils.jinja_methods",
# 	"filters": "staffing_plus.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "staffing_plus.install.before_install"
# after_install = "staffing_plus.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "staffing_plus.uninstall.before_uninstall"
# after_uninstall = "staffing_plus.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "staffing_plus.utils.before_app_install"
# after_app_install = "staffing_plus.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "staffing_plus.utils.before_app_uninstall"
# after_app_uninstall = "staffing_plus.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "staffing_plus.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "staffing_plus.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"staffing_plus.tasks.all"
# 	],
# 	"daily": [
# 		"staffing_plus.tasks.daily"
# 	],
# 	"hourly": [
# 		"staffing_plus.tasks.hourly"
# 	],
# 	"weekly": [
# 		"staffing_plus.tasks.weekly"
# 	],
# 	"monthly": [
# 		"staffing_plus.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "staffing_plus.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "staffing_plus.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "staffing_plus.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "staffing_plus.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["staffing_plus.utils.before_request"]
# after_request = ["staffing_plus.utils.after_request"]

# Job Events
# ----------
# before_job = ["staffing_plus.utils.before_job"]
# after_job = ["staffing_plus.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"staffing_plus.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

doc_events = {
    "Project": {
        "autoname": "staffing_plus.staffing_plus.custom_script.project.set_project_name_from_lead"
    }
}

fixtures = [
    {
    	"doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [ 
                    "Project-custom_lead",                  
                 ]
            ]
        ]
    }
]