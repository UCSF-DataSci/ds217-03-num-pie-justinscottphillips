#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # Calculate average heart rate using data['heart_rate'].mean()
    # Calculate average systolic BP using data['blood_pressure_systolic'].mean()
    # Calculate average glucose level using data['glucose_level'].mean()
    average_heart_rate = data['heart_rate'].mean()
    average_systolic_bp = data['blood_pressure_systolic'].mean()
    average_glucose = data['glucose_level'].mean()

    print("Average Heart Rate:", average_heart_rate)
    print("Average Systolic BP:", average_systolic_bp)
    print("Average Glucose Level:", average_glucose)

    # Return as dictionary with keys: 'avg_heart_rate', 'avg_systolic_bp', 'avg_glucose'
    return {
        'avg_heart_rate': average_heart_rate,
        'avg_systolic_bp': average_systolic_bp,
        'avg_glucose': average_glucose
    }
    pass


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # Count readings where heart rate > 90 using boolean indexing
    # Example: high_hr_count = len(data[data['heart_rate'] > 90])
    # Or: high_hr_count = (data['heart_rate'] > 90).sum()
   
    # Count readings where systolic BP > 130 using boolean indexing
    # Example: high_bp_count = len(data[data['blood_pressure_systolic'] > 130])

    # Count readings where glucose > 110 using boolean indexing
    # Example: high_glucose_count = len(data[data['glucose_level'] > 110])

    high_hr_count = (data['heart_rate'] > 90).sum()
    high_bp_count = (data['blood_pressure_systolic'] > 130).sum()
    high_glucose_count = (data['glucose_level'] > 110).sum()

    print("High HR count:", high_hr_count)
    print("High BP count:", high_bp_count)
    print("High Glucose count:", high_glucose_count)
    
    # Return dictionary with keys: 'high_heart_rate', 'high_blood_pressure', 'high_glucose'
    return {
        'high_heart_rate': high_hr_count,
        'high_blood_pressure': high_bp_count,
        'high_glucose': high_glucose_count
    }
    pass


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    # Create a formatted report string using f-strings
    # Include all statistics with proper formatting using .1f for decimals
    # Example: f"Heart Rate: {stats['avg_heart_rate']:.1f} bpm"        
    # Include section headers and labels for readability
    # Include total_readings, all averages, and all abnormal counts

    message = f"===========================\n"
    message += f"Health Data Analysis Report\n"
    message += f"===========================\n"

    message += f"\nDataset Statistics\n"
    message += f"   Total Readings: {total_readings}\n"

    message += f"\nAverage Values\n"
    message += f"   Average Heart Rate: {stats['avg_heart_rate']:.1f} bpm\n"
    message += f"   Average Systolic BP: {stats['avg_systolic_bp']:.1f} mmHg\n"
    message += f"   Average Glucose Level: {stats['avg_glucose']:.1f} mg/dL\n"
    
    message += f"\nAbnormal Readings\n"
    message += f"   High Heart Rate (>90 bpm): {abnormal['high_heart_rate']}\n"
    message += f"   High Systolic BP (>130 mmHg): {abnormal['high_blood_pressure']}\n"
    message += f"   High Glucose Level (>110 mg/dL): {abnormal['high_glucose']}\n"
    return message
    pass


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # Write the report to a file using open() with 'w' mode
    # Example: with open(filename, 'w') as f:
    #              f.write(report)

    with open("output/analysis_report.txt", "w") as f:  
        f.write(report)
    pass


def main():
    """Main execution function."""
    # Load the data from 'health_data.csv' using load_data()
    data = load_data('health_data.csv')

    # Calculate statistics using calculate_statistics()
    stats = calculate_statistics(data)

    # Find abnormal readings using find_abnormal_readings()
    abnormal = find_abnormal_readings(data)

    # Calculate total readings using len(data)
    total_readings = len(data)

    # Generate report using generate_report()
    report = generate_report(stats, abnormal, total_readings)
    print(report)
    
    # Save to 'output/analysis_report.txt' using save_report()
    save_report(report, 'output/analysis_report.txt')
    
    # Print success message
    print("Report saved to output/analysis_report.txt")
    pass


if __name__ == "__main__":
    main()

    # Test code to verify functionality
    data = load_data('health_data.csv')
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)

