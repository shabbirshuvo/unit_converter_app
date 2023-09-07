unit_dict = {
    'Length': {
        'units': ['meters', 'kilometers', 'miles', 'feet', 'inches'],
        'conversion_factors': {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084,
            'inches': 39.3701
        }
    },
    'Area': {
        'units': ['square meters', 'square kilometers', 'acres', 'square feet', 'square inches'],
        'conversion_factors': {
            'square meters': 1,
            'square kilometers': 0.000001,
            'acres': 0.000247105,
            'square feet': 10.7639,
            'square inches': 1550.0031
        }
    },
    'Volume': {
        'units': ['cubic meters', 'liters', 'gallons', 'cubic feet', 'cubic inches'],
        'conversion_factors': {
            'cubic meters': 1,
            'liters': 1000,
            'gallons': 264.172,
            'cubic feet': 35.3147,
            'cubic inches': 61023.7
        }
    },
    'Speed': {
        'units': ['m/s', 'km/h', 'mph', 'ft/s'],
        'conversion_factors': {
            'm/s': 1,
            'km/h': 3.6,
            'mph': 2.23694,
            'ft/s': 3.28084
        }
    },
    'Mass': {
        'units': ['kg', 'g', 'lb', 'oz'],
        'conversion_factors': {
            'kg': 1,
            'g': 1000,
            'lb': 2.20462,
            'oz': 35.274
        }
    },
    'BMI': {
        # Assuming BMI is calculated using kg/m^2
        'units': ['kg/m^2'],
        'conversion_factors': {
            'kg/m^2': 1  # Since it's a single unit, you might handle it differently in your app.
        }
    }
}
