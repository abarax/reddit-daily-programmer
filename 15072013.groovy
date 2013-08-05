class RoomLog {
    def time
    def personCount
   
    RoomLog(newTime, newPersonCount) {
        time = newTime
        personCount = newPersonCount
    }
   
    def String toString() {
       time + " " + personCount
    }
   
    def RoomLog plus(other) {       
        return new RoomLog(time + other.time, personCount + other.personCount)
    }
}

Map<Integer, RoomLog> log = new TreeMap<Integer, RoomLog>()

new File("C://input.txt").eachLine { line ->
   line = line.split()
   if (line.length > 1) {
       lineNo = line[0]
       room = Integer.parseInt(line[1])
       type = line[2]
       time = Integer.parseInt(line[3])
       count = 0
      
       if(type == 'I') {          
           time = 0 - time
           count = 1
       }
      
       RoomLog e = log.get(room)
      
       if (e == null)
           log.put(room, new RoomLog(time, count))
       else
           log.put(room, e + new RoomLog(time, count))
    }

}

log.each { entry ->
    println "Room ${entry.key}, ${entry.value.time/entry.value.personCount} minute average visit, ${entry.value.personCount} visitors total"

}