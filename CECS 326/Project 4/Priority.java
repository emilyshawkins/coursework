/**
 * Non-preemptive priority scheduling algorithm.
 */
 
import java.util.*;

// Your code here

public class Priority implements Algorithm{

    List<Task> taskQueue; // List of tasks
    boolean[] ran; // Auxillary array to indicate if task is finished

    public Priority(List<Task> queue) {
        taskQueue = queue;
        ran = new boolean[queue.size()]; // Initialze to false
        Arrays.fill(ran, false);
    }

    @Override
    public void schedule() {
        System.out.println("\nPriority Scheduling \n");

        for (int i = 0; i < taskQueue.size(); i++) {
            Task task = pickNextTask(); // Gets task to run

            System.out.println("Will run task:");
            System.out.println(task);
        }
    }

    @Override
    public Task pickNextTask() {

        Task highestPriority = new Task(null, 0, 0); // Placeholder task
        int location = -1; // Placeholder index

        for (int j = 0; j < taskQueue.size(); j++) { // Iterates through array to find highest priority task
            if (location == -1 && ran[j] == false) { // Initialize valid task that has not been executed
                highestPriority = taskQueue.get(j);
                location = j;
            }
            // Compare priorities of task and changes if a higher priority one is found
            else if (taskQueue.get(j).getPriority() < highestPriority.getPriority() && ran[j] == false) {
                highestPriority = taskQueue.get(j);
                location = j;
            }
        }

        ran[location] = true; // Indicates that the task has run
        return highestPriority;
    }

}