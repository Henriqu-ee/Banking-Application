def get_cambio(moeda):
    taxas = {
        'USD': 5.2,
        'EUR': 6.1,
        'JPY': 0.038
    }
    return taxas.get(moeda)