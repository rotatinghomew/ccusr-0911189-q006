import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from storylines.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'storylines', 'edition', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_suggested_link_cannot_change_series(self):
        current = report(self.data)
        self.assertIn({'topic':'museum','week':1,'reads':2},current['series'])
        self.assertIn({'topic':'square','week':1,'reads':1},current['series'])
        self.assertEqual(current['audience']['square'],['R3'])

    def test_duplicate_read_conflict(self):
        self.data['reads'][1]['article'] = 'a2'
        with self.assertRaises(ValueError):
            report(self.data)
