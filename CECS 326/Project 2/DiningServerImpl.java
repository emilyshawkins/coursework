/**
 * DiningServer.java
 *
 * This class contains the methods called by the  philosophers.
 *
 */

import java.util.concurrent.locks.Lock;
import java.util.Vector;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class DiningServerImpl  implements DiningServer
{
	Lock lock = new ReentrantLock(); // Lock for critical section
	Condition[] philosophers_forks = new Condition[5]; // Waiting and Signaling Philosopher threads
	int[] forks = {1, 1, 1, 1, 1}; // Fork availibility: 0 = taken, 1 = available
	Vector<Integer> waiting = new Vector<Integer>(); // Stores philosopher ids that are waiting

	DiningServerImpl() {
		for (int i = 0; i < 5; i++) {
			philosophers_forks[i] = lock.newCondition(); // Fill can_take, size 5
		}
	}
	
	@Override
	public void takeForks(int philNumber) { // Allows philosopher to take forks if they are both available and wait if they aren't

		lock.lock();
		// Critical section
		try {
			while(canTake(philNumber) == false) { // When forks can't be taken

				waiting.add(philNumber); // Add to waiting queue

				philosophers_forks[philNumber].await(); // Waits
			}

			forks[philNumber] = forks[(philNumber + 1) % 5] = 0; // Forks set to 0: taken
			System.out.println("Philosopher " + philNumber + " took forks " + philNumber + " and " + (philNumber + 1) % 5);
		}
		catch (InterruptedException err) {}
		finally {
			lock.unlock();
		}
		
	}

	@Override
	public void returnForks(int philNumber) { // Returns the forks after philosopher finishes eating

		lock.lock();
		// Critical section
		try {
			forks[philNumber] = forks[(philNumber + 1) % 5] = 1; // Forks set to 1: available
			System.out.println("Philosopher " + philNumber + " returned forks " + philNumber + " and " + (philNumber + 1) % 5);
			
			if (waiting.size() != 0) { // If theres a philosopher waiting in queue, signal them
				philosophers_forks[waiting.remove(0)].signal();
			}
		}
		finally {
			lock.unlock();
		}
		
	}  

	public boolean canTake(int philNumber) { // Checks if both forks can be taken
		if (forks[philNumber] == 1 && forks[(philNumber + 1) % 5] == 1) {
			return true;
		}
		else {
			return false;
		}
	}

	public void forksAvailable() {
		for (int i = 0; i < 5; i++) {
			if (forks[i] == 0) {
				System.out.println("Fork " + i + " is taken");
			}
			else {
				System.out.println("Fork " + i + " is available");
			}
		}
	}

}
