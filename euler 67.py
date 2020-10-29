def FindingNemo(B, A, agraph, distance = 1):
    queue = [A,0]
    aset= {A}
    for node in queue:       
        if node == 0:
            distance +=1
        else:
            for neighbor in node.neighbors:
                if neighbor == B:
                    return distance+1
                elif neighbor not in aset:
                        queue.append(neighbor)
                        aset.add(neighbor)
            if queue[queue.index(node)+1] == 0: 
                queue.append(0)                    
    return None
    
            
                
    