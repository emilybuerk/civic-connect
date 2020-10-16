from django.test import TestCase

from django.contrib.auth.models import User
from .models import Issue, Resource


class IssueModelTests(TestCase):

    # 1. id_name() tests

    def test_id_name_standard(self):
        """
        id_name() returns a version of the issue name usable
        as an HTML id tag
        """
        # Inputs
        issue_name = 'Civic Connect'

        # Expected Outputs
        id_name = 'civic-connect'

        # Failure Message
        message = "Failed standard id_name() test"

        # Build model
        issue = Issue(name=issue_name)
        issue.save()

        # Assertions
        self.assertEqual(issue.id_name(), id_name, message)

    def test_id_name_no_space(self):
        """
        id_name() returns a version of the issue name usable
        as an HTML id tag
        """
        # Inputs
        issue_name = 'CivicConnect'

        # Expected Outputs
        id_name = 'civicconnect'

        # Failure Message
        message = "Failed id_name() with no spaces"

        # Build model
        issue = Issue(name=issue_name)
        issue.save()

        # Assertions
        self.assertEqual(issue.id_name(), id_name, message)

    def test_id_name_all_upper_case(self):
        """
        id_name() returns a version of the issue name usable
        as an HTML id tag
        """
        # Inputs
        issue_name = 'CIVIC CONNECT'

        # Expected Outputs
        id_name = 'civic-connect'

        # Failure Message
        message = "Failed id_name() all upper case"

        # Build model
        issue = Issue(name=issue_name)
        issue.save()

        # Assertions
        self.assertEqual(issue.id_name(), id_name, message)

    def test_id_name_empty(self):
        """
        id_name() returns a version of the issue name usable
        as an HTML id tag
        """
        # Inputs
        issue_name = ''

        # Expected Outputs
        id_name = ''

        # Failure Message
        message = "Failed id_name() empty name"

        # Build model
        issue = Issue(name=issue_name)
        issue.save()

        # Assertions
        self.assertEqual(issue.id_name(), id_name, message)

    def test_id_name_has_hyphen(self):
        """
        id_name() returns a version of the issue name usable
        as an HTML id tag
        """
        # Inputs
        issue_name = 'Civic-Connect'

        # Expected Outputs
        id_name = 'civic-connect'

        # Failure Message
        message = "Failed id_name() with hyphen"

        # Build model
        issue = Issue(name=issue_name)
        issue.save()

        # Assertions
        self.assertEqual(issue.id_name(), id_name, message)

    # 2. has_resources() tests
    
    def test_has_resources_one_active(self):
        """
        has_resources() checks if there are any active resources
        attached to the issue
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['ResourceOne']
        status = ['A']

        # Expected Outputs
        has_resources = True

        # Failure Message
        message = "Failed has_resources() with one active resource"
        
        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()    # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID, 
                                      anonymous=ANONYMOUS)

        # Assertions
        self.assertIs(issue.has_resources(), has_resources, message)

    def test_has_resources_two_inactive(self):
        """
        has_resources() checks if there are any active resources
        attached to the issue
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['ResourceOne', 'ResourceTwo']
        status = ['R', 'P']

        # Expected Outputs
        has_resources = False

        # Failure Message
        message = "Failed has_resources() with two inactive resources"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        self.assertIs(issue.has_resources(), has_resources, message)

    def test_has_resources_none(self):
        """
        has_resources() checks if there are any active resources
        attached to the issue
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = []
        status = []

        # Expected Outputs
        has_resources = False

        # Failure Message
        message = "Failed has_resources() with no resources"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        self.assertIs(issue.has_resources(), has_resources, message)

    def test_has_resources_active_and_non_active(self):
        """
        has_resources() checks if there are any active resources
        attached to the issue
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['Active', 'Inactive']
        status = ['A', 'P']

        # Expected Outputs
        has_resources = True

        # Failure Message
        message = "Failed has_resources() with active and inactive resource"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        self.assertIs(issue.has_resources(), has_resources, message)
        
    # 3. active_resources() tests

    def test_active_resources_two_out_of_order(self):
        """
        active_resources() returns a list of all active resources in alphabetical order
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['Bananas', 'Apples']
        status = ['A', 'A']

        # Expected Outputs
        expected = ['Apples', 'Bananas']

        # Failure Message
        message = "Failed active_resources() with two active resources in wrong order"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        actual = issue.active_resources()
        for i in range(len(actual)):
            self.assertEqual(actual[i].title, expected[i], message)
            
    def test_active_resources_active_and_inactive(self):
        """
        active_resources() returns a list of all active resources in alphabetical order
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['Apples', 'Chocolate', 'Dates', 'Bananas']
        status = ['A', 'P', 'R', 'A']

        # Expected Outputs
        expected = ['Apples', 'Bananas']

        # Failure Message
        message = "Failed active_resources() with two active and two inactive resources"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        actual = issue.active_resources()
        for i in range(len(actual)):
            self.assertEqual(actual[i].title, expected[i], message)
            
    def test_active_resources_empty(self):
        """
        active_resources() returns a list of all active resources in alphabetical order
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = []
        status = []

        # Expected Outputs
        expected = []

        # Failure Message
        message = "Failed active_resources() with empty resource set"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        actual = issue.active_resources()
        for i in range(len(actual)):
            self.assertEqual(actual[i].title, expected[i], message)
            
    def test_active_resources_inactive_only(self):
        """
        active_resources() returns a list of all active resources in alphabetical order
        """
        # Inputs
        issue_name = 'Civic-Connect'
        resources = ['Bananas', 'Apples']
        status = ['P', 'R']

        # Expected Outputs
        expected = []

        # Failure Message
        message = "Failed active_resources() with two inactive resources"

        # Extra constants
        URL = 'sample/url'
        SUBMITTER_ID = 1
        ANONYMOUS = False

        # Build model
        User(username="TestUser").save()  # create a fake submitter
        issue = Issue(name=issue_name)
        issue.save()
        for i in range(len(resources)):
            issue.resource_set.create(title=resources[i], url=URL, status=status[i], submitter_id=SUBMITTER_ID,
                                      anonymous=ANONYMOUS)

        # Assertions
        actual = issue.active_resources()
        for i in range(len(actual)):
            self.assertEqual(actual[i].title, expected[i], message)
