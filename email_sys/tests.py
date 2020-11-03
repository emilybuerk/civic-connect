from django.test import TestCase
from .models import Template

# Create your tests here.

class TemplateModelTests(TestCase):

    def test_template_title_standard(self):
        """
        template_title() returns the template title
        """
        # Inputs
        template_title = 'Civic Connect'

        # Expected Outputs
        template_title_expected = 'Civic Connect'

        # Failure Message
        message = "Failed standard template_title test"

        # Build model
        template = Template(title=template_title)
        template.save()

        # Assertions
        self.assertEqual(template.template_title(), template_title_expected, message)

    def test_template_title_empty(self):
        """
        template_title() returns an empty title
        """
        # Inputs
        template_title = ' '

        # Expected Outputs
        template_title_expected = ' '

        # Failure Message
        message = "Failed empty template_title test"

        # Build model
        template = Template(title=template_title)
        template.save()

        # Assertions
        self.assertEqual(template.template_title(), template_title_expected, message)

    def test_template_title_complex(self):
        """
        template_title() returns the template title
        """
        # Inputs
        template_title = '547365%%$$$))((@%#'

        # Expected Outputs
        template_title_expected = '547365%%$$$))((@%#'

        # Failure Message
        message = "Failed complex template_title test"

        # Build model
        template = Template(title=template_title)
        template.save()

        # Assertions
        self.assertEqual(template.template_title(), template_title_expected, message)

    def test_template_body_standard(self):
        """
        template_body() returns the template title
        """
        # Inputs
        template_body = 'Civic Connect:' \
                        'This is an example body for the template test.'

        # Expected Outputs
        template_body_expected = 'Civic Connect:' \
                                 'This is an example body for the template test.'

        # Failure Message
        message = "Failed standard template_body test"

        # Build model
        template = Template(body=template_body)
        template.save()

        # Assertions
        self.assertEqual(template.template_body(), template_body_expected, message)

    def test_template_body_empty(self):
        """template_body() returns an empty title
        """
        # Inputs
        template_body = ' '

        # Expected Outputs
        template_body_expected = ' '

        # Failure Message
        message = "Failed empty template_body test"

        # Build model
        template = Template(body=template_body)
        template.save()

        # Assertions
        self.assertEqual(template.template_body(), template_body_expected, message)

    def test_template_body_complex(self):
        """
        template_body() returns a template title
        """
        # Inputs
        template_body = 'Civic Connect:' \
                        'This is an example body for the template test.' \
                        '85747 %%%%% ******* ()()()##@@@@@@!!!!^^^^^^^~~~~~~~'

        # Expected Outputs
        template_body_expected = 'Civic Connect:' \
                        'This is an example body for the template test.' \
                        '85747 %%%%% ******* ()()()##@@@@@@!!!!^^^^^^^~~~~~~~'

        # Failure Message
        message = "Failed complex template_body test"

        # Build model
        template = Template(body=template_body)
        template.save()

        # Assertions
        self.assertEqual(template.template_body(), template_body_expected, message)