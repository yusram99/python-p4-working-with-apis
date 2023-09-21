import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
        programs_list.append(program["agency"])

    return programs_list

# Create an instance of GetPrograms
programs = GetPrograms()
# Call the program_school method to get the list of schools
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
