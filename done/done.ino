#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Viet";
const char* password = "";

const char* serverAddress = "http://172.20.10.3:5000"; 

const int LED_PIN = 22; 

bool isLightOn = false;
unsigned long lastUpdateTime = 0;
const unsigned long updateInterval = 3000; 
unsigned long lastWifiCheckTime = 0;
const unsigned long wifiCheckInterval = 60000; 

void setupWiFi() {
  Serial.print("Đang kết nối WiFi...");
  
  WiFi.mode(WIFI_STA);  
  delay(1000); 
  WiFi.begin(ssid, password);
  
  int attempts = 0;
  int maxAttempts = 20;
  
  while (WiFi.status() != WL_CONNECTED && attempts < maxAttempts) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  if(WiFi.status() == WL_CONNECTED) {
    Serial.println("\n✅ Kết nối WiFi thành công!");
    Serial.print("📡 Địa chỉ IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\n❌ Không thể kết nối WiFi sau nhiều lần thử!");
  }
}


void setupGPIO() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);  
  Serial.println("✅ Cấu hình GPIO xong! LED nối với GPIO: " + String(LED_PIN));
}

bool checkWiFiConnection() {
  if(WiFi.status() != WL_CONNECTED) {
    Serial.println("⚠️ Mất kết nối WiFi. Đang kết nối lại...");
    setupWiFi();
    return WiFi.status() == WL_CONNECTED;
  }
  return true;
}

void checkLightStatus() {
  if(!checkWiFiConnection()) {
    Serial.println("⚠️ Không thể kiểm tra trạng thái đèn: WiFi chưa kết nối");
    return;
  }
  
  HTTPClient http;
  
  String url = String(serverAddress) + "/light/status";
  http.begin(url);
  
  int httpResponseCode = http.GET();
  Serial.print("📡 Light status response code: ");
  Serial.println(httpResponseCode);
  
  if(httpResponseCode == 200) {
    String response = http.getString();
    Serial.println("🔹 Phản hồi từ server: " + response);
    
    // Parse JSON response
    StaticJsonDocument<200> doc;
    DeserializationError error = deserializeJson(doc, response);
    
    if(!error) {
      bool serverLightState = doc["light"];
      
      // Đồng bộ trạng thái đèn với server
      if(serverLightState != isLightOn) {
        isLightOn = serverLightState;
        digitalWrite(LED_PIN, isLightOn ? HIGH : LOW);
        Serial.println(isLightOn ? "💡 Đèn đã BẬT theo server" : "💡 Đèn đã TẮT theo server");
      } else {
        Serial.println("✅ Trạng thái đèn đã đồng bộ với server");
      }
    } else {
      Serial.print("❌ Lỗi khi parse JSON: ");
      Serial.println(error.c_str());
    }
  } else {
    Serial.print("❌ Lỗi khi lấy trạng thái đèn: ");
    Serial.println(httpResponseCode);
  }
  
  http.end();
}

void pingServer() {
  if(!checkWiFiConnection()) {
    Serial.println("⚠️ Không thể ping server: WiFi chưa kết nối");
    return;
  }
  
  HTTPClient http;
  
  String url = String(serverAddress) + "/";
  http.begin(url);
  
  int httpResponseCode = http.GET();
  Serial.print("📡 Server ping response code: ");
  Serial.println(httpResponseCode);
  
  if(httpResponseCode > 0) {
    Serial.println("✅ Server đang hoạt động");
  } else {
    Serial.println("❌ Không thể kết nối đến server");
  }
  
  http.end();
}

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n--- 🚀 Khởi động hệ thống ---");
  
  setupGPIO();
  
  setupWiFi();
  
  pingServer();
  
  Serial.println("✅ ESP32 đã sẵn sàng kết nối với server Flask");
}

void loop() {
  unsigned long currentTime = millis();
  
  if(currentTime - lastWifiCheckTime > wifiCheckInterval) {
    lastWifiCheckTime = currentTime;
    checkWiFiConnection();
  }
  
  if(currentTime - lastUpdateTime > updateInterval && WiFi.status() == WL_CONNECTED) {
    lastUpdateTime = currentTime;
    
    Serial.println("\n--- 🔄 Đang cập nhật trạng thái ---");
    
    pingServer();
    
    checkLightStatus();
  }
  
  delay(100);
}
