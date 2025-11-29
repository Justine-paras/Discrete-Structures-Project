import webview
import time
import threading
from backend.navigation import get_shortest_path
from backend.scholarship import ScholarshipAPI
from backend.parking import (get_region_status,
    get_region_totals,
    get_lots,
    park_vehicle,
    leave_vehicle)


class API:
    def __init__(self):
        # instantiate ScholarshipAPI once
        self.scholarship = ScholarshipAPI()

    def open_navigation(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/navigation.html')).start()
        return "navigation loaded"
    
    def get_shortest_path(self, start, end):
        return get_shortest_path(start, end) 
    
    def open_scholarship(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/scholarship.html')).start()
        return "scholarship loaded"

    # Delegate scholarship methods
    def get_requirements(self, scholarship_type):
        return self.scholarship.get_requirements(scholarship_type)

    def check_eligibility(self, scholarship_type, answers):
        return self.scholarship.check_eligibility(scholarship_type, answers)
    
    def open_parking(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/parking.html')).start()
        return "parking loaded"
    
    def get_parking_status(self):
        return get_region_totals()

    def get_parking_availability(self):
        return get_region_status()

    def get_parking_lots(self, region):
        return get_lots(region)

    def park(self, region, lot):
        return park_vehicle(region, lot)

    def leave(self, lot):
        return leave_vehicle(lot)



