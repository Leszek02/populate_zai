# Populate_zai
A script for generating and populating fossasia open-event's database for testing purposes.

# Prepare for generating
Update variable `API_HOST` in `consts.py` accordingly 

# Generate .csv files

`pip install -r requirements.txt` \
`python generate.py`

# Inject data into the database
(Fossasia's backend infrastructure must be running) \
Windows: `./execute.bat` \
Linux: `./execute.sh`
