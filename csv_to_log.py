import pandas as pd

# Load the CSV file
df = pd.read_csv('CANdata (1).csv')

# Open a new log file to write the output
with open('converted_log.log', 'w') as log_file:
    # Write the header
    log_file.write("***BUSMASTER Ver 1.9.0 Beta 1***\n")
    log_file.write("***PROTOCOL CAN***\n")
    log_file.write("***NOTE: PLEASE DO NOT EDIT THIS DOCUMENT***\n")
    log_file.write("***[START LOGGING SESSION]***\n")
    log_file.write(f"***START DATE AND TIME {pd.to_datetime('now').strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}***\n")
    log_file.write("***HEX***\n")
    log_file.write("***SYSTEM MODE***\n")
    log_file.write("***START CHANNEL BAUD RATE***\n")
    log_file.write("***END CHANNEL BAUD RATE***\n")
    log_file.write("***START DATABASE FILES (DBF/DBC)***\n")
    log_file.write("***END DATABASE FILES (DBF/DBC)***\n")
    log_file.write("***<Time><Tx/Rx><Channel><CAN ID><Type><DLC><DataBytes>***\n")

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # Format the log entry
        time = row['System Time']  # Adjust based on your CSV
        time_cleaned = time.strip(('"= '))  # Remove double quotes and spaces
        # replacing '.' with ':'
        if '.' in time_cleaned:
            # Split the string into the part before and after the last '.'
            time_parts = time_cleaned.rsplit('.', 1)  # Split on the last occurrence of '.'
            # Combine the parts, replacing '.' with ':'
            time_cleaned = time_parts[0] + ':' + time_parts[1]  # Rejoin with ':'
            time_cleaned += '0'

        #direction = row['Direction']  # Tx or Rx
        direction = 'Rx'
        channel = row['Channel']  # Channel number
        can_id = row['Frame ID']  # Directly using the CAN ID from the CSV
        type_ = row['Type']  # e.g., 's' for standard
        dlc = row['DLC']  # Data Length Code
        data = row['Data']  # Directly using the Data from the CSV
        data_clean = data.strip(' x|')

        # Write the formatted log entry
        log_file.write(f"{time_cleaned} {direction} {channel} {can_id} {type_} {dlc} {data_clean}\n")

    log_file.write(f"***END DATE AND TIME {pd.to_datetime('now').strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}***\n")
    log_file.write("***[STOP LOGGING SESSION]***\n")
