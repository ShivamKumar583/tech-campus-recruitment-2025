discussion.md
markdown
Copy
Edit
# Discussion

## Solutions Considered

### 1. String Manipulation with `split()`
- **Approach:** We considered using Python's built-in `split()` method to break down each log line into its components (timestamp, log level, and message).
- **Pros:** Simple and easy to implement.
- **Cons:** Doesn't handle variations in log formatting and requires strict input structure.

### 2. Regular Expressions (`re` module)
- **Approach:** Used regex to match the specific log format and extract required fields.
- **Pros:** More flexible and can handle different timestamp formats.
- **Cons:** Requires a well-defined pattern and may fail if logs deviate slightly.

### 3. Using `datetime` for Parsing
- **Approach:** We explored using Python’s `datetime` module to parse timestamps and reformat them correctly.
- **Pros:** Ensures accurate timestamp formatting.
- **Cons:** Extra processing needed for incorrect timestamps.

## Final Solution Summary

We chose **Regular Expressions (`re` module)** because:  
- It allows us to accurately extract log components (timestamp, log level, message).  
- It provides flexibility in handling different formats.  
- It avoids unnecessary overhead from multiple string operations.  

## Steps to Run

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/ShivamKumar583/tech-campus-recruitment-2025.git
   cd tech-campus-recruitment-2025

2. **Navigate to src/ Directory** 
    cd src

3. **Run the Log Extraction Script** 
    python extract_logs.py YYYY-MM-DD
    Replace YYYY-MM-DD with the desired date.

4.  **Check Output**
    Extracted logs will be saved in the output/ folder.
    Example: output/output_2024-12-01.txt
