"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: 2A202600606
Name: Vu Thanh Danh 

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Returns:
        list: Danh sach cac records (dictionaries)
    """
    print(f"Extracting data from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Extracted {len(data)} records from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac validation:
       - Price phai > 0 (loai bo gia am hoac bang 0)
       - Category khong duoc rong

    Returns:
        list: Danh sach cac records hop le
    """
    valid_records = []
    error_count = 0

    for record in data:
        try:
            price = float(record.get('price', 0))
        except (TypeError, ValueError):
            price = 0

        category = str(record.get('category', '')).strip() if record.get('category') is not None else ''

        if price <= 0 or category == '':
            error_count += 1
            continue

        valid_records.append(record)

    print(f"Validation summary: {len(valid_records)} kept, {error_count} dropped.")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Yeu cau:
       - Tinh discounted_price = price * 0.9 (giam 10%)
       - Chuan hoa category thanh Title Case (vi du: "electronics" -> "Electronics")
       - Them cot processed_at = timestamp hien tai

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    df = pd.DataFrame(data)
    if df.empty:
        return df

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['discounted_price'] = df['price'] * 0.9
    df['category'] = df['category'].astype(str).str.strip().str.title()
    df['processed_at'] = datetime.datetime.now().isoformat()

    print(f"Transformation complete. Added discounted_price and processed_at for {len(df)} records.")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path} with {len(df)} records.")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")
