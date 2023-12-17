class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.cuisine_map = defaultdict(dict)
        
        self.food_map = {foods[i]: [cuisines[i], ratings[i]] for i in range(len(foods))}
        
        for i in range(len(cuisines)):
            
            if ratings[i] not in self.cuisine_map[cuisines[i]]:
                
                self.cuisine_map[cuisines[i]][ratings[i]] = set()
                
            self.cuisine_map[cuisines[i]][ratings[i]].add(foods[i])

    def changeRating(self, food: str, newRating: int) -> None:
        
        current_cuisine, old_rating = self.food_map[food]
        
        self.food_map[food][1] = newRating
        
        # remove food from the old rating system 

        self.cuisine_map[current_cuisine][old_rating].remove(food)
        
        if not self.cuisine_map[current_cuisine][old_rating]:
            
            del self.cuisine_map[current_cuisine][old_rating]

        # add food to the new rating set
        
        if newRating not in self.cuisine_map[current_cuisine]:
            
            self.cuisine_map[current_cuisine][newRating] = set()
            
        self.cuisine_map[current_cuisine][newRating].add(food)

    def highestRated(self, cuisine: str) -> str:
        
        max_rating = max(self.cuisine_map[cuisine].keys())
        
        if max_rating in self.cuisine_map[cuisine]:
            
            return min(self.cuisine_map[cuisine][max_rating]) 
        
        else:
            
            return ""



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)