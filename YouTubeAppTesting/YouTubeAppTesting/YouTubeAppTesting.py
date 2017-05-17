import unittest

from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from time import sleep


class TestClass(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = R'C:\Users\Mystia\documents\visual studio 2015\Projects\test\test\YouTube_12.17.apk'
        desired_caps['appPackage'] =  'com.google.android.youtube'
        desired_caps['appActivity'] = 'com.google.android.youtube.HomeActivity'
        #desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'

        print('opening youtube ...')
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test1(self):
        print("wait for opening")
        sleep(2)

        print('click menu button ...')
        self.dr.find_element_by_accessibility_id("更多選項").click()
        sleep(1)

        print('click login button ...')
        try :
            t = self.dr.find_element_by_android_uiautomator('new UiSelector().text("登入")').click()
            sleep(1)
            self.dr.find_element_by_android_uiautomator('new UiSelector().text("軟測")').click()
        except:
            print("already login")
            self.dr.tap([(555,1629)] ,100)
        sleep(0.5)
        
        self.dr.tap([(555,1629)] ,100)
        sleep(2)

        print('click subscribe ...')
        self.dr.find_element_by_accessibility_id("訂閱這個頻道").click()
        sleep(1)    

        print('click add button ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("新增至")').click()
        sleep(1)      

        print('click watch later button ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("稍後觀看")').click()
        sleep(1)      

        print('back ...')
        self.dr.press_keycode(4)
        sleep(2)

        print('slide left ...')
        self.dr.swipe(930, 1500, 100, 150, 300)
        sleep(0.5)

        print('click account ...')
        self.dr.find_element_by_accessibility_id("帳戶").click()
        sleep(1)   

        print('click watch later button ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("稍後觀看")').click()
        sleep(1)    

        print('click menu ...')
        self.dr.find_element_by_accessibility_id("選單").click()
        sleep(1)   

        print('remove from watch late ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("從稍後觀看中移除")').click()
        sleep(1)          

        print('back ...')
        self.dr.press_keycode(4)
        sleep(2)

        print('click subscribe ...')
        try :
            self.dr.find_element_by_accessibility_id("訂閱內容").click()
        except :
            print('oh ... it\'s look like it have news')
            try :
                self.dr.find_element_by_accessibility_id("訂閱內容：有新內容").click()
            except :
                print('okay, there\'s nothing news, it\'s will fail a moment later')
        sleep(1)   

        print('menu ...')
        self.dr.find_element_by_accessibility_id("選單").click()
        sleep(1)   

        print('canel subscribe ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("取消訂閱")').click()
        sleep(1)   

        print('click menu button ...')
        self.dr.find_element_by_accessibility_id("更多選項").click()
        sleep(1)

        print('click logout button ...')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("登出")').click()
        sleep(1)

    def test0(self):
        print("wait for opening")
        sleep(2)

        print('click account ...')
        self.dr.find_element_by_accessibility_id("帳戶").click()
        sleep(2)   

        print('click recommend video ...')
        self.dr.find_element_by_accessibility_id("發燒影片").click()
        sleep(2)   

        print('click a random video ...')
        self.dr.tap([(530,1000)] ,100)
        sleep(8)   

        #print('click video')
        #self.dr.tap([(500,350)] ,100)
        #sleep(0.5)    

        #t = self.dr.find_element_by_android_uiautomator('new UiSelector().resourceId("com.google.android.youtube:id/app_promotion_card")')
        #if not t.isEmpty():
        try :
            self.dr.find_element_by_android_uiautomator('new UiSelector().text("略過廣告")').click()
            print('skip the ad !!')
            sleep(5)
        except :
            pass

        print('click video')
        self.dr.tap([(500,350)] ,100)
        sleep(0.5) 

        print('click option')
        self.dr.find_element_by_accessibility_id("更多選項").click()
        sleep(1)                 

        print('click quality')
        self.dr.find_element_by_android_uiautomator('new UiSelector().text("畫質")').click()
        sleep(1)          

        try :
            t = self.dr.find_element_by_android_uiautomator('new UiSelector().text("360p")').click()
            sleep(1)
        except:
            print('doesn\'t support 360p video')

        print('click video')
        self.dr.tap([(500,350)] ,100)
        sleep(0.5)

        print('pause video')
        self.dr.find_element_by_accessibility_id("暫停影片").click()
        sleep(5)


    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()