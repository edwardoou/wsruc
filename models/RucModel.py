class Ruc():

    def __init__(self) -> None:
        self.ruc = ''
        self.razon_social = ''
        self.tipo_contribuyente = ''
        self.nombre_comercial = ''
        self.fecha_inscripcion = ''
        self.fecha_inicio = ''
        self.estado_contibuyente = ''
        self.condicion_contribuyente = ''
        self.domicilio_fiscal = ''
        self.sistema_emision_comprobante = ''
        self.actividad_comercio_exterior = ''
        self.sistema_contabilidad = ''
        self.actividades_economicas = ''
        self.comprobantes_pago = ''
        self.sistema_emision_electronica = ''
        self.fecha_emisor_electronico = ''
        self.comprobante_electronico = ''
        self.afiliado_ple = ''
        self.padrones = ''

    def to_json(self):
        return {
            'ruc': self.ruc,
            'razon_social': self.razon_social,
            'tipo_contribuyente': self.tipo_contribuyente,
            'nombre_comercial': self.nombre_comercial,
            'fecha_inscripcion': self.fecha_inscripcion,
            'fecha_inicio' : self.fecha_inicio,
            'estado_contibuyente': self.estado_contibuyente,
            'condicion_contribuyente': self.condicion_contribuyente,
            'domicilio_fiscal': self.domicilio_fiscal,
            'sistema_emision_comprobante' : self.sistema_emision_comprobante,
            'actividad_comercio_exterior' : self.actividad_comercio_exterior,
            'sistema_contabilidad' : self.sistema_contabilidad,
            'actividades_economicas' : self.actividades_economicas,
            'comprobantes_pago' : self.comprobantes_pago,
            'sistema_emision_electronica' : self.sistema_emision_electronica,
            'fecha_emisor_electronico' : self.fecha_emisor_electronico,
            'comprobante_electronico' : self.comprobante_electronico,
            'afiliado_ple' : self.afiliado_ple,
            'padrones' : self.padrones
        }