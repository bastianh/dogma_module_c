import random
import unittest
from dogma import Dogma, DOGMA_STATE_Active, DOGMA_STATE_Online
from dogma_types import *

class TestCapacitor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dogma = Dogma()       

    @classmethod
    def tearDownClass(cls):
        cls.dogma = None

    def assert_capacitor_unstable(self, reload, expected_delta, expected_mins, expected_secs, precision_ms):
        global_delta, stable, param = self.dogma.get_capacitor(reload)
        self.assertAlmostEqual(expected_delta,global_delta*1000,delta=0.1)
        self.assertFalse(stable)
        self.assertAlmostEqual((expected_secs + expected_mins * 60) * 1000,param,delta=precision_ms)

    def assert_capacitor_stable(self, reload, expected_delta, expected_percentage):
        global_delta, stable, param = self.dogma.get_capacitor(reload)
        self.assertAlmostEqual(expected_delta,global_delta*1000,delta=0.1)
        self.assertTrue(stable)
        self.assertAlmostEqual(expected_percentage,param,delta=2.5)

    def test_capacitor(self):

        slot1 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_MultifrequencyL)
        self.assert_capacitor_unstable(False, 4.76, 0, 0, 0.000001)
        self.assert_capacitor_unstable(True, 4.76, 0, 0, 0.000001)

        slot2 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_MultifrequencyL)
        self.assert_capacitor_unstable(False, 2*4.76, 0, 0, 0.000001)
        self.assert_capacitor_unstable(True, 2*4.76, 0, 0, 0.000001)

        self.dogma.set_module_state(slot1, DOGMA_STATE_Online)
        self.dogma.set_module_state(slot2, DOGMA_STATE_Online)
        self.assert_capacitor_stable(False, 0, 100)
        self.assert_capacitor_stable(True, 0, 100)

        self.dogma.set_ship(TYPE_Abaddon);
        self.dogma.set_module_state(slot1, DOGMA_STATE_Active);
        self.dogma.set_module_state(slot2, DOGMA_STATE_Active);
        self.dogma.add_charge(slot2, TYPE_MultifrequencyL);
        self.assert_capacitor_stable(False, 4.76 * 2 - 21.3, 76.0);
        self.assert_capacitor_stable(True, 4.76 * 2 - 21.3, 76.0);

        slot3 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_MultifrequencyL)
        slot4 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_MultifrequencyL)
        self.assert_capacitor_stable(False, 4.76 * 4 - 21.3, 43.8);
        self.assert_capacitor_stable(True, 4.76 * 4 - 21.3, 43.8);

        self.dogma.add_charge(slot1, TYPE_StandardL);
        self.dogma.add_charge(slot2, TYPE_StandardL);
        self.dogma.add_charge(slot3, TYPE_StandardL);
        self.dogma.add_charge(slot4, TYPE_StandardL);
        slot5 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_StandardL)
        slot6 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_StandardL)
        slot7 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_StandardL)
        slot8 = self.dogma.add_module_sc(TYPE_MegaPulseLaserII, DOGMA_STATE_Active, TYPE_StandardL)
        self.assert_capacitor_stable(False, 2.62 * 8 - 21.3, 31.7);
        self.assert_capacitor_stable(True, 2.62 * 8 - 21.3, 31.7);

        self.dogma.add_charge(slot1, TYPE_InfraredL);
        self.assert_capacitor_unstable(False, 2.62 * 7 + 3.1 - 21.3, 100, 49, 60000);
        self.assert_capacitor_unstable(True, 2.62 * 7 + 3.1 - 21.3, 100, 49, 60000);

        self.dogma.add_charge(slot1, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot2, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot3, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot4, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot5, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot6, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot7, TYPE_MultifrequencyL);
        self.dogma.add_charge(slot8, TYPE_MultifrequencyL);
        self.assert_capacitor_unstable(False, 4.76 * 8 - 21.3, 5, 53, 5000);
        self.assert_capacitor_unstable(True, 4.76 * 8 - 21.3, 5, 53, 5000);

        slot10 = self.dogma.add_module_sc(TYPE_HeavyCapacitorBoosterII, DOGMA_STATE_Active, TYPE_CapBooster800);
        self.assert_capacitor_stable(True, 4.76 * 8 - 78.4, 89.8);

        # to be continued

class TestBasicAttributes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dogma = Dogma()
        cls.dogma.set_ship(TYPE_Rifter)

    @classmethod
    def tearDownClass(cls):
        cls.dogma = None

    def test_get_attribute_hiSlots(self):
        hislots = self.dogma.get_ship_attribute(ATT_HiSlots)
        self.assertEqual(hislots, 4)

    def test_get_attribute_medSlots(self):
        medslots = self.dogma.get_ship_attribute(ATT_MedSlots)
        self.assertEqual(medslots, 3)

    def test_get_attribute_lowSlots(self):
        lowslots = self.dogma.get_ship_attribute(ATT_LowSlots)
        self.assertEqual(lowslots, 3)

    def test_get_attribute_UpgradeSlotLeft(self):
        slots = self.dogma.get_ship_attribute(ATT_UpgradeSlotsLeft)
        self.assertEqual(slots,3)

    def test_get_attribute_MaxSubSystem(self):
        slots = self.dogma.get_ship_attribute(ATT_MaxSubSystems)
        self.assertEqual(slots,0)

class TestBasicCharges(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dogma = Dogma()
        cls.slot = None
        cls.dogma.set_ship(TYPE_Rifter)

    @classmethod
    def tearDownClass(cls):
        cls.dogma = None


    def expect_optimal_falloff_tracking(self, optimal:float, falloff:float, tracking:float):
        value = self.dogma.get_module_attribute(self.slot, ATT_MaxRange)
        self.assertAlmostEqual(optimal,value,delta=0.5)

        value = self.dogma.get_module_attribute(self.slot, ATT_Falloff)
        self.assertAlmostEqual(falloff,value,delta=0.5)

        value = self.dogma.get_module_attribute(self.slot, ATT_TrackingSpeed)
        self.assertAlmostEqual(tracking,value,delta=0.000000005)

    def test_autocannon(self):
        self.slot = self.dogma.add_module_s(TYPE_125mmGatlingAutoCannonII, DOGMA_STATE_Active)
        self.expect_optimal_falloff_tracking(1200.0, 7500.0, 0.52125)

        self.dogma.add_charge(self.slot, TYPE_EMPS)
        self.expect_optimal_falloff_tracking(600.0, 7500.0, 0.52125)

        self.dogma.add_charge(self.slot, TYPE_NuclearS)
        self.expect_optimal_falloff_tracking(1920.0, 7500.0, 0.5473125)

        self.dogma.add_charge(self.slot, TYPE_BarrageS)
        self.expect_optimal_falloff_tracking(1200.0, 11250.0, 0.3909375)


class TestBasicSkillLevel(unittest.TestCase):

    HARB_BaseCPU = 375.00
    HARB_BasePG = 1425.00


    def test_skills(self):
        dogma = Dogma()
        dogma.set_ship(TYPE_Harbinger)

        self.assertAlmostEqual(self.HARB_BasePG * 1.25, dogma.get_ship_attribute(ATT_PowerOutput))
        self.assertAlmostEqual(self.HARB_BaseCPU * 1.25, dogma.get_ship_attribute(ATT_CpuOutput))

        dogma.set_default_skill_level(1)

        self.assertAlmostEqual(self.HARB_BasePG * 1.05, dogma.get_ship_attribute(ATT_PowerOutput))
        self.assertAlmostEqual(self.HARB_BaseCPU * 1.05, dogma.get_ship_attribute(ATT_CpuOutput))

        dogma.set_skill_level(TYPE_CPUManagement, 4)
        dogma.set_skill_level(TYPE_PowerGridManagement, 0)

        self.assertAlmostEqual(self.HARB_BasePG , dogma.get_ship_attribute(ATT_PowerOutput))
        self.assertAlmostEqual(self.HARB_BaseCPU * 1.20, dogma.get_ship_attribute(ATT_CpuOutput))

        dogma.set_default_skill_level(5)
        dogma.reset_skill_levels()

        self.assertAlmostEqual(self.HARB_BasePG * 1.25, dogma.get_ship_attribute(ATT_PowerOutput))
        self.assertAlmostEqual(self.HARB_BaseCPU * 1.25, dogma.get_ship_attribute(ATT_CpuOutput))

if __name__ == '__main__':
    unittest.main()
