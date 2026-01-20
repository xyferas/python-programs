

def calculate_points(membershipTier, totalSpent):
    
    if totalSpent < 100:
        return 0
    else:
        tier = membershipTier.lower()
        points = 0
        bonus = 0

        if tier == "gold":
            points = 10
            if totalSpent > 500:
                bonus = 50

        elif tier == "silver":
            points = 5
            if totalSpent > 500:
                bonus = 20

        elif tier == "regular":
            points = 2
        
        return (totalSpent//100) * points + bonus
