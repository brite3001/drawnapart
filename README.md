# Drawn Apart

Artifacts for "DRAWN APART : A Device Identification Technique based on Remote GPU Fingerprinting", by Tomer Laor, Naif Mehanna, Vitaly Dyadyuk, Antonin Durey, Pierre Laperdrix, Clémentine Maurice, Yossi Oren, Romain Rouvoy, Walter Rudametkin, and Yuval Yarom

# Collecting Data with modified gpu.html and offscreen.html
1. Open gpu or offscreen in a chrome browser window
2. Make sure to set chrome not to prompt for a download location on every new download
3. Use an auto clicker (XClicker) to click the 'this file is trying to download multiple files' prompt that appears regularly
4. Use the timing_data_to_csv.py file to combine all the individual text files into a single CSV, ready to ML
