class CarBase:
    def __init__(self, photo_file_name):
        self.photo_file_name = photo_file_name


class Truck (CarBase):
    def __init__(self, photo_file_name, body_whl):
        super().__init__(photo_file_name)
        self._body_whl = body_whl  
        try:
            self.body_length = float(self._body_whl.split("x", 2)[0])
            self.body_width = float(self._body_whl.split("x", 2)[1])        
            self.body_height = float(self._body_whl.split("x", 2)[2])       
        except ValueError:
            self.body_length, self.body_width, self.body_height = 0, 0, 0
        
    @property
    def body_whl(self):
        if len(self._body_whl) == 0:
            self._body_whl = "0x0x0"
        return self._body_whl    

   
    


truck = Truck("123.jpg", "")
truck.body_width