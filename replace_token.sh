#!/bin/bash

path="/etc/xiaoya"  # 修改为实际的文件路径
files=("$path/mytoken.txt" "$path/myopentoken.txt" "$path/temp_transfer_folder_id.txt")

for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Creating empty file: $file"
        touch "$file"
    fi

    echo "Enter replacement for $file (press Enter to skip):"
    read replacement

    if [ -n "$replacement" ]; then
        # Save the replacement content to the file
        echo "$replacement" > "$file"
    fi

    # Display the result
    echo -e "\n$file:"
    cat "$file"
    echo "--------------------------"
done

echo -e "\nFinal Contents:"
for file in "${files[@]}"; do
    echo "$file: $(cat $file)"
done

echo "Replacement completed."

