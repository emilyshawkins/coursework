/**
 * An echo client. The client enters data to the server, and the
 * server echoes the data back to the client.
 */
import java.net.*;
import java.io.*;

public class EchoClient
{
    public static void main(String[] args) {
        try {
            Socket sock = new Socket("127.0.0.1", 6007); // Connects to server socket
            // Get output stream to write to socket
            PrintWriter pout = new PrintWriter(sock.getOutputStream(), true); 

            // Gets the input stream to read from socket
            InputStreamReader socket_input = new InputStreamReader(sock.getInputStream());
            BufferedReader socket_in = new BufferedReader(socket_input);

            // Read user/client input from std in
            InputStreamReader input = new InputStreamReader(System.in);
            BufferedReader user_in = new BufferedReader(input);

            String text; // Initialize string to store user input from std in
            // It the user types in "Close Socket" the loop will break
            while((text = user_in.readLine()) != null && !text.equals("Close Socket")) {
                pout.println(" " + text); // User input to Socket
                System.out.println(socket_in.readLine()); // Prints what has been return by the socket
            }

            sock.close(); // Closes socket after the user inputs "Close Socket"
        }
        catch (IOException error) {
            System.err.println(error);
        }
    }

}
