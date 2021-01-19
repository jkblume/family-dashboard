// Library für WiFi-Verbindung
#include <ESP8266WiFi.h>

// Daten des WiFi-Netzwerks
const char* ssid     = "";
const char* password = "";

// Port des Web Servers auf 80 setzen
WiFiServer server(80);

const int relay = 5;

// Variable für den HTTP Request
String header;

void setup() {
  pinMode(relay, OUTPUT);
  
  Serial.begin(115200);

  // Mit dem WiFi-Netzwerk verbinden
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Lokale IP-Adresse im Seriellen Monitor ausgeben und Server starten
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();   // Auf Clients (Server-Aufrufe) warten

  if (client) {                             // Bei einem Aufruf des Servers
    Serial.println("Client available");
    String currentLine = "";                // String definieren für die Anfrage des Clients

    while (client.connected()) { // Loop, solange Client verbunden ist

      if (client.available()) {
        char c = client.read();             // Ein (1) Zeichen der Anfrage des Clients lesen
        Serial.write(c);                    // und es im Seriellen Monitor ausgeben
        header += c;
        if (c == '\n') {                    // bis eine Neue Zeile ausgegeben wird
          
          // Wenn der Client eine Leerzeile sendet, ist das Ende des HTTP Request erreicht
          if (currentLine.length() == 0) {

            // Der Server sendet nun eine Antwort an den Client
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type: application/json");
            client.println("Access-Control-Allow-Origin: *");
            client.println("Connection: close");
            client.println();

            // Die Webseite anzeigen
            client.println("{}");

            // Die Antwort mit einer Leerzeile beenden
            client.println();
            // Den Loop beenden
            break;
          } else { // Bei einer Neuen Zeile, die Variable leeren
            if (currentLine.indexOf("GET") != -1) {
              String paramterName = "command=";
              int startIndex = currentLine.indexOf(paramterName) + paramterName.length();
              int endIndex = currentLine.lastIndexOf(" ");
              String parameterValue = currentLine.substring(startIndex, endIndex);
              
              int duration = parameterValue.toInt();

              if (duration > 0) {
                relayControl(duration);
              }
            }

            currentLine = "";
          }
        } else if (c != '\r') {  // alles andere als eine Leerzeile wird
          currentLine += c;      // der Variable hinzugefüht
        }
      }
    }
    // Variable für den Header leeren
    header = "";
    // Die Verbindung beenden
    client.stop();
    Serial.println("Client disconnected");
    Serial.println("");
  }
}

// Custom function accessible by the API
int relayControl(int duration) {
  Serial.println("Function called: ");
  Serial.println(duration);
  
  digitalWrite(relay, HIGH);
  Serial.println("Flowing now...");
  delay(duration); 
  digitalWrite(relay, LOW);
  Serial.println("Stopped flowing.");
  
  return 1;
}
