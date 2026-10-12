import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App {
    static final BlockingQueue<String> priceQueue = new LinkedBlockingQueue<>();
    static final Pattern PRICE_PATTERN =
        Pattern.compile("\"price\"\\s*:\\s*\"?([^\",}]+)");

    public static void main(String[] args) throws InterruptedException {
        String apiKey = System.getenv("TWELVE_DATA_API_KEY");

        if (apiKey == null || apiKey.isBlank()) {
            System.out.println("API key not found.");
            return;
        }

        HttpClient client = HttpClient.newHttpClient();

        while (true) {
            String timestamp = Instant.now().toString();

            try {
                String url = "https://api.twelvedata.com/price?symbol=DIA&apikey="
                    + URLEncoder.encode(apiKey, StandardCharsets.UTF_8);

                HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

                HttpResponse<String> response =
                    client.send(request, HttpResponse.BodyHandlers.ofString());

                Matcher matcher = PRICE_PATTERN.matcher(response.body());

                if (matcher.find()) {
                    String result = timestamp + " | DIA price: " + matcher.group(1);
                    priceQueue.offer(result);
                    System.out.println(result);
                    System.out.println("Queue size: " + priceQueue.size());
                } else {
                    System.out.println(timestamp + " | Could not get a price: " + response.body());
                }

            } catch (IOException e) {
                System.out.println(timestamp + " | Network error: " + e.getMessage());
            }

            Thread.sleep(15000);
        }
    }
}
