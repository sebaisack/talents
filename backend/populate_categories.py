#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import TalentCategory, Talent

# Map of category values to display names
category_map = {
    'music': 'Music',
    'sports': 'Sports',
    'technology': 'Technology',
    'arts': 'Arts',
    'academics': 'Academics',
    'other': 'Other',
}

print("=== Creating TalentCategory records ===\n")

# Create TalentCategory records
categories = {}
for category_value, display_name in category_map.items():
    category_obj, created = TalentCategory.objects.get_or_create(
        name=display_name,
        defaults={'description': f'Category for {display_name}'}
    )
    categories[category_value] = category_obj
    print(f"✓ {'Created' if created else 'Found'}: {display_name} (id={category_obj.id})")

print("\nTalent category foreign keys are populated by Django migration 0013.\n")
print(f"✓ Total categories created: {len(categories)}")
