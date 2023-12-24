/**
 * Modified DateClient so that it requests a quote
 * from the quote server.
 */
 
import java.net.*;
import java.io.*;

public class QuoteClient {
    public static void main(String[] args) throws IOException {
        Socket sock = new Socket("localhost", 6017);

        BufferedReader bf = new BufferedReader(new InputStreamReader(sock.getInputStream()));

        // Read and print the quote from the server
        String quote;
        while ((quote = bf.readLine()) != null) {
            System.out.println(quote);
        }

        sock.close();
    }
}