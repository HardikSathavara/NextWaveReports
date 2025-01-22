
def format_field_name(fields):
    
    return [{field:field.replace('_', ' ').title()} for field in fields]