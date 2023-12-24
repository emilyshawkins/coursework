/**
 * DiningPhilosophers.java
 *
 * This program starts the dining philosophers problem.
 *
 */


public class DiningPhilosophers
{  
  public static void main(String[] args) 
  {
    int numPhilosophers = 5;
    DiningServer diningServer = new DiningServerImpl();

    Thread[] philosophers = new Thread[numPhilosophers];

    for (int i = 0; i < numPhilosophers; i++) {
      philosophers[i] = new Thread(new Philosopher(i, diningServer));
    }

    for (int i = 0; i < numPhilosophers; i++) {
      philosophers[i].start();
    }
  }
}