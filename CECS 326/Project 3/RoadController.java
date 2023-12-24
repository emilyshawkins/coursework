/**
 * RoadController.java
 *
 *
 */

import java.util.concurrent.Semaphore;

class Road {
    private Semaphore semaphore = new Semaphore(1);

    public void enterRoad(String direction, int villager) {
        try {
            semaphore.acquire();
            System.out.println("");
            System.out.println(direction + " villager " + villager + " is entering the road.");
        } catch (InterruptedException e) {}
    }

    public void leaveRoad(String direction, int villager) {
        System.out.println(direction + " villager " + villager + " villager has left the road.");
        System.out.println("");
        semaphore.release();
    }
}

public class RoadController
{  
   public static void main(String[] args) {
      Road road = new Road();

        // Create multiple Eastvillagers and Westvillagers
        Thread[] eastThreads = new Thread[3];
        Thread[] westThreads = new Thread[3];

        for (int i = 0; i < 3; i++) {
            eastThreads[i] = new Thread(new East_village("East", i, road));
            westThreads[i] = new Thread(new West_village("West", i, road));
            eastThreads[i].start();
            westThreads[i].start();
        }
   }

}
