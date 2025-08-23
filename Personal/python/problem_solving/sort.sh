for file in *.py; do
	# Get the last character before .py (problem letter)
	problem_letter=$(echo "$file" | sed -E 's/.*([A-Z])\.py/\1/')
	# Make the folder if it doesn't exist
	mkdir -p "$problem_letter"
	# Move the file
	mv "$file" "$problem_letter/"
done
