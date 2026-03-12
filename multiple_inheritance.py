class camera_phone:
    def picture(self):
        print("best pictures quality")
class smart_phone:
    def all_purpose(self):
        print("all purpose in one device")
class mobile(camera_phone,smart_phone):
    def use(self):
        print("using purposes")
c=mobile()
c.use()
c.picture()
c.all_purpose()
