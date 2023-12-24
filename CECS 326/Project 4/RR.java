import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class RR implements Algorithm {

    private List<Task> taskList;
    private Queue<Task> taskQueue;

    public RR(List<Task> tasks) {
        taskList = tasks;
        taskQueue = new LinkedList<>(tasks);
    }

    @Override
    public void schedule() {
        System.out.println("\nRound Robin Scheduling\n");

        while (!taskQueue.isEmpty()) {
            Task currentTask = pickNextTask();
            executeTask(currentTask);

            if (currentTask.getBurst() > 0) {
                // add it back to the queue if there are remaining burst time
                taskQueue.add(currentTask);
            }
        }
    }

    @Override
    public Task pickNextTask() {
        // dequeue the next task in the queue
        return taskQueue.poll();
    }

    private void executeTask(Task task) {
        System.out.println("Executing task: " + task.getName());
        int remainingBurst = task.getBurst() - 10; // Deduct time quantum

        // burst time doesn't go below zero
        task.setBurst(Math.max(remainingBurst, 0));
    }
}