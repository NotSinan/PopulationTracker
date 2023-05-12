class WorldListProcessor:
    def __init__(self) -> None:
        self.world_populations = {}
    
    def get_population(self, rows):
        for row in rows:
            # extract the columns from the row
            columns = row.find_all('td')
            
            try:
                world_id = int(columns[0].find('a')['id'].split('-')[2])
                population = int(columns[1].text.strip().split()[0])
                member_world = str(columns[3].text)
                if member_world == "Members":
                    if world_id not in self.world_populations:
                        self.world_populations[world_id] = population
                    else:
                        diff = population - self.world_populations[world_id]
                        if diff >= 5:
                            print(f'World {world_id} has increased by {diff} players')
                    self.world_populations[world_id] = population
            except (IndexError, ValueError) as e:
                print(f"Error parsing population data for world {world_id}")




        