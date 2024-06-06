from models.button import button

class GetDashboardButtons:
    
    def __init__(self):
        pass
    
    def execute(self):
        
        buttons = [
            button(label='Dashboard', url='/dashboard/'),
            button(label='Tablas', url='tables'),
            button(label='Paginas', url='pages'),
            button(label='Graficas', url='charts'),
            button(label='Configuracion', url='configweb'),
            button(label='Cerrar Sesión', url='logout')
        ]
        
        return buttons