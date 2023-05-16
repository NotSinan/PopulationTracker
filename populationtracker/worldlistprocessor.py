class WorldListProcessor:
    def __init__(self, threshold):
        self.world_populations = {}
        self.threshold = threshold

    def get_population(self, rows):
        world_population = []
        for row in rows:
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
                        if diff >= self.threshold:
                            world_population.append((world_id, diff))
                    self.world_populations[world_id] = population

            except (IndexError, ValueError):
                pass
        
        return world_population
