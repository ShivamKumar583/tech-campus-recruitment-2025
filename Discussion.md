# **Log Extraction Script**

## **Overview**
This script extracts and processes log entries based on a given date. It efficiently filters logs using **Regular Expressions (`re` module)** to ensure accuracy and flexibility.

---

## **Solutions Considered**

### **1️⃣ String Manipulation with `split()`**
- **Approach:** Used Python’s built-in `split()` method to divide log entries into timestamp, log level, and message.
- **✅ Pros:**
  - Simple and easy to implement.
- **❌ Cons:**
  - Requires a strict input structure.
  - Struggles with variations in log formatting.

### **2️⃣ Regular Expressions (`re` module)**
- **Approach:** Used regex to match the log format and extract key fields dynamically.
- **✅ Pros:**
  - More flexible, handles multiple timestamp formats.
  - Extracts data accurately without relying on fixed positions.
- **❌ Cons:**
  - Requires a well-defined pattern.
  - May break if log formats vary significantly.

### **3️⃣ Using `datetime` for Parsing**
- **Approach:** Utilized Python’s `datetime` module to parse and validate timestamps before further processing.
- **✅ Pros:**
  - Ensures correct timestamp handling.
  - Reduces errors due to incorrect formats.
- **❌ Cons:**
  - Extra processing overhead for incorrect timestamps.

---

## **Final Solution: Regular Expressions (`re` module)**
We chose **regex-based extraction** because:
✅ It provides flexibility in handling different log formats.  
✅ It accurately extracts the timestamp, log level, and message.  
✅ It avoids unnecessary overhead from multiple string operations.  

---

## **How to Run the Log Extraction Script**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ShivamKumar583/tech-campus-recruitment-2025.git
cd tech-campus-recruitment-2025
```

### **2️⃣ Navigate to the `src/` Directory**
```bash
cd src
```

### **3️⃣ Run the Script**
```bash
python extract_logs.py YYYY-MM-DD
```
📌 Replace `YYYY-MM-DD` with the target date.

### **4️⃣ View Extracted Logs**
📂 Extracted logs will be saved in the `output/` folder.  
📜 Example output file:  
✅ `output/logs_2024-12-01.txt`

✨ **Now, your logs are clean, structured, and ready for analysis!** 🚀
