# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()


    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)

        valido = Socio(dni=12345679, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        invalido = Socio(dni=12345678, nombre='Jose', apellido='Garcia')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)


    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        valido = Socio(dni=12345678, nombre='J23', apellido='P23')
        self.assertTrue(self.ns.regla_2(valido))
        valido = Socio(dni=12345678, nombre='Juan56789012345', apellido='Perez6789012345')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan567890123456', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez67890123456')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        for x in range(self.ns.MAX_SOCIOS):
            socio = Socio(dni=x, nombre='Juan', apellido='Perez')
            exito = self.ns.alta(socio)
            self.assertTrue(exito)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)



    def test_baja(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        socio_recuperado = self.ns.buscar_dni(socio.dni)
        self.assertTrue(self.ns.baja(socio_recuperado.id_socio))

    def test_buscar(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertTrue(self.ns.buscar(socio.id_socio) == socio)

    def test_buscar_dni(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertTrue(self.ns.buscar_dni(socio.dni) == socio)

    def test_todos(self):
        for x in range(1,self.ns.MAX_SOCIOS+1):
            socio = Socio(dni=x, nombre='Juan', apellido='Perez')
            exito = self.ns.alta(socio)
            self.assertTrue(len(self.ns.todos()) == x)

    def test_modificacion(self):
        socio_original = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio_original)
        socio_modificar = self.ns.buscar_dni(socio_original.dni)
        socio_modificar.dni = 87654321
        socio_modificar.nombre = 'Nauj'
        socio_modificar.apellido = 'Zerep'
        self.ns.modificacion(socio_modificar)
        socio_recuperado = self.ns.buscar(socio_modificar.id_socio)
        self.assertTrue(socio_recuperado == socio_modificar)
