from db import get_lenses_collection

# Lenses Collection
lenses_collection = get_lenses_collection()

# Lenses object
class ContactLens:
    def __init__(self, manufacturer, name, frequency):
        self.manufacturer = manufacturer
        self.name = name
        self.frequency = frequency


# Add new lenses entry to database
def insert_lens(data):
    try:
        result = lenses_collection.insert_one(data)
        if result.inserted_id:
            response = {"message": "Lens added."}
            status_code = 200
        else:
            response = {"message": "Error adding lens"}
            status_code = 500
    except Exception as err:
        response = {"message": str(err)}
        status_code = 500
    return response, status_code


# Delete lenses entry to database
def delete_lens(data):
    try:
        result = lenses_collection.delete_one(data)
        if result.inserted_id:
            response = {"message": "Lens deleted."}
            status_code = 200
        else: 
            response = {"message": "Error deleting lens."}
            status_code = 500
    except Exception as err:
        response = {"message": str(err)}
        status_code = 500
    return response, status_code

# Display prices available on multiple websites using buildmypc format

