class WorldListProcessor:
    def __init__(self) -> None:
        self.world_populations = {}
    
    def get_population(self, rows):
        for row in rows:
            # extract the columns from the row
            columns = row.find_all('td')

            # extract the data from the columns
            world_id = int(columns[0].find('a')['id'].split('-')[2])
            population = int(columns[1].text.strip().split()[0])
            if world_id not in self.world_populations:
                self.world_populations[world_id] = population
            

            # calculate the difference in population
            diff = population - self.world_populations[world_id]

            # check if the difference is greater than or equal to 10
            if diff >= 1:
                print(f'World {world_id} has increased by {diff} players')
            self.world_populations[world_id] = population


        