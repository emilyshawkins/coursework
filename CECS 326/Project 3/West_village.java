import java.util.Random;

public class West_village implements Runnable
{

   String direction;
   int villager;
   Road road;

   West_village(String east_west, int villager_num, Road road_ctrl) { // Villager: direction, number, and road
      this.direction = east_west; // East or West
      this.villager = villager_num; // Number/ID
      this.road = road_ctrl; // Road
   }

   @Override
   public void run() {

      while (true) {

         sleep();

         this.road.enterRoad(this.direction, this.villager); // Tries to enter road, acquire semaphore

         traveling(); // Makes thread sleep and produces an action string

         this.road.leaveRoad(this.direction, this.villager); // Leaves road, releases semaphore

      }

   }

   public void traveling() { // Produces a random action string and makes thread sleep
      String[] action = {" is playing cards", " is eating fruit", " is selling candy", 
                         " is jogging", " is reading", " is petting a cat",
                         " is visiting a friend", " is commuting", " is stargazing"};

      int rand_action = new Random().nextInt(9);
      System.out.println(this.direction + " Villager " + this.villager + action[rand_action]);

      sleep();

   }

   public void sleep() {
      try {
         int time = 1000 + new Random().nextInt(1000);
         Thread.sleep(time); // Sleeps 
      }
      catch (InterruptedException err) {}
   }
   
}
