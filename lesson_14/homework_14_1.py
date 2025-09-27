import unittest
from homework_14 import TeamLead


class TestTeamLead(unittest.TestCase):
    def test_teamlead_has_manager_and_developer_attributes(self):
        lead = TeamLead("Kate", 100000, "IT", "Python", 7)

        self.assertTrue(hasattr(lead, "name"))
        self.assertTrue(hasattr(lead, "salary"))

        self.assertTrue(hasattr(lead, "department"))

        self.assertTrue(hasattr(lead, "programming_language"))

        self.assertTrue(hasattr(lead, "team_size"))


if __name__ == "__main__":
    unittest.main()
