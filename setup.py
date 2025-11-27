#!/usr/bin/env python
"""
Setup script for the Django TODO application.
This script helps with initial project setup.
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and print status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(e.stderr)
        return False

def main():
    print("🚀 Setting up Django TODO Application")
    print("=" * 50)

    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)

    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)

    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        sys.exit(1)

    # Run tests
    run_tests = input("\n🤔 Do you want to run the test suite? (y/n): ").lower().strip()
    if run_tests == 'y':
        if not run_command("python manage.py test", "Running test suite"):
            print("⚠️  Some tests failed. Please check the output above.")
        else:
            print("✅ All tests passed!")

    # Create superuser (optional)
    create_superuser = input("\n🤔 Do you want to create a Django superuser for admin access? (y/n): ").lower().strip()
    if create_superuser == 'y':
        print("🔄 Creating superuser...")
        try:
            subprocess.run([sys.executable, 'manage.py', 'createsuperuser'], check=True)
            print("✅ Superuser created successfully!")
        except subprocess.CalledProcessError:
            print("⚠️  Superuser creation skipped or failed.")

    print("\n🎉 Setup completed successfully!")
    print("\nTo run the application:")
    print("  python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000/")
    if create_superuser == 'y':
        print("Admin panel: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    main()
