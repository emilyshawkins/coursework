/**
 * An echo server listening on port 6007. This server reads from the client
 * and echoes back the result. 
 */

import java.net.*;
import java.io.*;

public class EchoServer {
    public static void main(String[] args) { // Main
        try {
            ServerSocket sock = new ServerSocket(6007); // Creates ServerSocket

            while (true) {
                Socket client = sock.accept(); // Waits for connection from client
                // Gets output stream to write to it
                PrintWriter pout = new PrintWriter(client.getOutputStream(), true);

                InputStream input = client.getInputStream(); // Gets input stream
                // Reads from input stream
                BufferedReader buff_read = new BufferedReader(new InputStreamReader(input));

                String text; // Initializes string for text from socket
                // Keeps looping and sending text to socket when the client is still connected
                while(input.read() != -1 && (text = buff_read.readLine()) != null)
                    pout.println(text);

                client.close(); //When client disconnects, socket closes and it waits for new connect
            }
        }
        
        catch (IOException error) {
            System.err.println((error));
        }
    }


}
