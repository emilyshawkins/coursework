/**
 * FCFS scheduling algorithm.
 */
 
import java.util.*;

//Your code here

public class FCFS implements Algorithm {

    List<Task> taskQueue; // List of tasks
    int toSchedule; // Index of task to schedule

    public FCFS(List<Task> queue) {
        taskQueue = queue;
        toSchedule = 0;
    }

    @Override
    public void schedule() {
        System.out.println("\nFCFS Scheduling \n");

        for (int i = 0; i < taskQueue.size(); i++) {
            Task task = pickNextTask(); // Picks task to run

            System.out.println("Will run task:");
            System.out.println(task);
        }
    }

    @Override
    public Task pickNextTask() {

        Task toRun = taskQueue.get(toSchedule); // Gets task at index
        toSchedule++; // Increments index for next task

        return toRun;
    }

}