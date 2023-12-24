/**
 * Quote server listening to port 6017.
 *
 */
 
import java.net.*;
import java.io.*;
import java.util.Random; 

public class QuoteServer
{
    public static void main(String[] args) {
        try {
            ServerSocket sock = new ServerSocket(6017);

            /* now listen for connections */
            while (true) {

                // make some random quotes
                String[] quotes = {
                "Speak softly and carry a big stick",
                "That's one small step for a man, a giant leap for mankind.",
                "The only thing we have to fear is fear itself.",
                "Opportunities don't happen, you create them.",
                "Love your family, work super hard, live your passion"
                };

                Socket client = sock.accept();
                
                // to check if client is connected successfully
                System.out.println("Client connected");

                PrintWriter pout = new PrintWriter(client.getOutputStream(), true);
                
                /* write the quote to the socket */ 
                pout.println("Quote of the day");

                // get a random quote from the quotes array
                Random rand = new Random();
                int index = rand.nextInt(quotes.length);
                pout.println(quotes[index]);

                /* close the socket and resume */
                /* listening for connections */
                client.close();
            }
        }
        catch (IOException ioe) {
            System.err.println(ioe);
        }
    }
}