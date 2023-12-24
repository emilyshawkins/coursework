/**
 * Philosopher.java
 *
 * This class represents each philosopher thread.
 * Philosophers alternate between eating and thinking.
 *
 */

import java.util.Random;

public class Philosopher implements Runnable
{

    int philosopher_id;
    DiningServer table;

    Philosopher(int philosopher_id, DiningServer table) { // Philosopher has an id and table they eat at
        this.philosopher_id = philosopher_id;
        this.table = table;
    }

    @Override
    public void run() {

        while (true) { // Looping

            //All threads start off thinking
            thinking_eating("thinking"); // Philosopher is currently thinking (thread sleeps)

            this.table.takeForks(philosopher_id); // Philosopher tries to take forks

            thinking_eating("eating"); // Philosopher is currently eating (thread sleeps)

            this.table.returnForks(philosopher_id); // Philosopher puts their forks back

        }

    }

    public void thinking_eating(String action) { // Makes thread sleep from 1 - 3 seconds while they eat or think
        try {
                int rand = 1000 + new Random().nextInt(2001);
                Thread.sleep(rand); // Sleeps for rand amount of time
                System.out.println("Philosopher " + this.philosopher_id + " spent " + rand + " ms " +  action);
            }
            catch (InterruptedException e) {}
    }

}
