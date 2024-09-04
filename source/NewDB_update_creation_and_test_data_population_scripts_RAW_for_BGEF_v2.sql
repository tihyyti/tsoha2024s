Here are the scripts for creating and populating the improved database.

Database Creation Script
SQL

-- Create GearBundle Table
CREATE TABLE GearBundle (
    id SERIAL PRIMARY KEY,
    bundleName VARCHAR(80) NOT NULL,
    price FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create GearRow Table
CREATE TABLE GearRow (
    id SERIAL PRIMARY KEY,
    bundleID INTEGER NOT NULL,
    FOREIGN KEY (bundleID) REFERENCES GearBundle(id)
    -- Add other fields as necessary
);
AI-generated code. Review and use carefully. More info on FAQ.
Database Population Script
SQL

-- Insert test data into GearBundle Table
INSERT INTO GearBundle (bundleName, price, created_at, updated_at) VALUES
('Starter Bundle', 99.99, '2024-07-25 00:00:00', '2024-07-25 00:00:00'),
('Pro Bundle', 199.99, '2024-07-25 00:00:00', '2024-07-25 00:00:00'),
('Ultimate Bundle', 299.99, '2024-07-25 00:00:00', '2024-07-25 00:00:00');

-- Insert test data into GearRow Table
INSERT INTO GearRow (bundleID) VALUES
(1),
(1),
(2),
(2),
(2),
(3),
(3),
(3),
(3);
AI-generated code. Review and use carefully. More info on FAQ.
Python Script for Database Population
If you prefer to use a Python script to populate the database, here is an example:

Python

from datetime import datetime
from your_app import db
from your_app.models import GearBundle, GearRow

# Create test data for GearBundle
bundles = [
    GearBundle(bundleName='Starter Bundle', price=99.99, created_at=datetime(2024, 7, 25), updated_at=datetime(2024, 7, 25)),
    GearBundle(bundleName='Pro Bundle', price=199.99, created_at=datetime(2024, 7, 25), updated_at=datetime(2024, 7, 25)),
    GearBundle(bundleName='Ultimate Bundle', price=299.99, created_at=datetime(2024, 7, 25), updated_at=datetime(2024, 7, 25))
]

# Add bundles to the session
for bundle in bundles:
    db.session.add(bundle)

# Commit the session to save bundles
db.session.commit()

# Create test data for GearRow
rows = [
    GearRow(bundleID=1),
    GearRow(bundleID=1),
    GearRow(bundleID=2),
    GearRow(bundleID=2),
    GearRow(bundleID=2),
    GearRow(bundleID=3),
    GearRow(bundleID=3),
    GearRow(bundleID=3),
    GearRow(bundleID=3)
]

# Add rows to the session
for row in rows:
    db.session.add(row)

# Commit the session to save rows
db.session.commit()
AI-generated code. Review and use carefully. More info on FAQ.
These scripts should help you set up and populate the improved database with test data.