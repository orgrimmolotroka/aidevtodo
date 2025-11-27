#!/usr/bin/env python
"""
Test runner for Django TODO application.
"""

import os
import sys
import subprocess

def main():
    """Run the Django test suite."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.test_settings')

    # Import Django and run tests
    import django
    from django.conf import settings
    from django.test.utils import get_runner

    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["todos"])

    if failures:
        sys.exit(1)
    else:
        print("\n🎉 All tests passed!")
        sys.exit(0)

if __name__ == '__main__':
    main()
