import unittest
from statement_intake.core import inspect_file


class FormatTests(unittest.TestCase):
    def test_legacy_is_distinct(self):
        self.assertEqual(inspect_file('fixtures/legacy.ofx')['format'],'sgml-1')
        self.assertEqual(inspect_file('fixtures/legacy.ofx')['account_tags'],1)

    def test_correction_is_readable_as_source(self):
        self.assertEqual(inspect_file('fixtures/correction.ofx')['transaction_tags'],1)
