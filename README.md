# YouTubeAppTesting

#Appium install

1. python (我用3.6)
2. appium-python-client (cmd打 ==pip install Appium-Python-Client==)
3. 安裝python unittest (cmd打 ==pip install pytest==)
4. node.js
5. appium (cmd打 ==npm install appium==)
6. appium-doctor (cmd打 ==npm install appium-doctor==)
7. 安裝java sdk (有裝過就跳過)
8. Android Studio (裝Android SDK和AVD Manager，android studio的比較好用)

- 在cmd打==appium-doctor==後，這裡會提醒那些東西有缺，改掉打x的地方就好了，上面東西都裝完的話就只需要修改環境變數

- IDE我用visual studio，在Python Environment新增一個，然後把Prefix path、Interpreter path、Windows interpreter和Library path填上，預設有提示

- 都裝好以後，cmd打==appium==就可以啟動appium伺服器，從android studio打開模擬器後，appium會抓到adb上的devices，就可以直接寫腳本做測試了