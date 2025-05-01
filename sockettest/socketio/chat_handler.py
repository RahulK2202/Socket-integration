import frappe

@frappe.whitelist()
def send_custom_notification(message):
    if frappe.session.user != "Administrator":
        frappe.throw("Only Administrator can send messages.")
    
    # Broadcast message to all connected clients
    frappe.publish_realtime('my_custom_event', message)
    return {"status": "success"}
