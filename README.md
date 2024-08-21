# Drawn Apart

Artifacts for "DRAWN APART : A Device Identification Technique based on Remote GPU Fingerprinting", by Tomer Laor, Naif Mehanna, Vitaly Dyadyuk, Antonin Durey, Pierre Laperdrix, Clémentine Maurice, Yossi Oren, Romain Rouvoy, Walter Rudametkin, and Yuval Yarom

# Collecting Data with modified gpu.html and offscreen.html
1. Install fastapi: https://fastapi.tiangolo.com/#installation
2. set the `test_num` and `save_path` in `trace_upload_server.py`
3. Start the trace collection server `fastapi dev trace_upload_server.py`
4. Start either `offscreen.html` or `gpu.html` and check that traces are being saved correctly 
5. Use the `timing_data_to_csv.py` file to combine all the individual text files into a single CSV, ready to ML
