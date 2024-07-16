def remove_duplicates(input_file, output_file):
    records = {"|0200|": set(), "|0190|": set(), "|0150|": set(), "|0500|": set()}
    duplicates = {"|0200|": set(), "|0190|": set(), "|0150|": set(), "|0500|": set()}
    output_lines = []

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            record_type = line[:6]
            if record_type in records:
                if line in records[record_type]:
                    duplicates[record_type].add(line)
                else:
                    records[record_type].add(line)
                    output_lines.append(line)
            else:
                output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in output_lines:
            file.write(line)

    # Print duplicates
    for record_type, lines in duplicates.items():
        if lines:
            print(f"Duplicated lines for {record_type}:")
            for line in lines:
                print(line)

    print(f"Process completed. Cleaned file saved as {output_file}")


# Usage example:
input_file = "C:\\Users\\Axxen\\Desktop\\LONDRECI LEO\\2021_09_.txt"
output_file = "C:\\Users\\Axxen\\Desktop\\LONDRECI LEO\\2021_09_cleaned3.txt"
remove_duplicates(input_file, output_file)
