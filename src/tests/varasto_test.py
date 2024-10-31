import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_negatiivinen_tilavuus(self):
    	neg_tilavuus = Varasto(-1)
    	self.assertAlmostEqual(neg_tilavuus.tilavuus,0)
    	
    def test_negatiivinen_alku_saldo(self):
    	neg_saldo = Varasto(10, -1)
    	self.assertAlmostEqual(neg_saldo.saldo, 0)
    	
    def test_lisays_lisaa_saldoa_neg(self):
    	self.varasto.lisaa_varastoon(-1)
    	return
    	
    def test_lisays_lisaa_saldoa_yli_tilavuuden(self):
    	self.varasto.lisaa_varastoon(11)
    	self.assertAlmostEqual(self.varasto.saldo, 10)
    	
    def test_lisays_lisaa_pienentaa_vapaata_tilaa_yli_tilavuuden(self):
    	self.varasto.lisaa_varastoon(11)
    	self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    	
    def test_ottaminen_neg(self):
    	self.varasto.ota_varastosta(-1)
    	return 0.0
    	
    def test_ottaminen_yli_saldon(self):
    	self.varasto.ota_varastosta(11)
    	return 10
    	
    def test_tulostaminen(self):
    	tulostus = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
    	self.assertEqual(str(self.varasto), tulostus)
