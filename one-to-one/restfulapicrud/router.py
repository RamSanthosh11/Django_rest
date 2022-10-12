from employeeapi.viewsets import EmployeeViewset,vehicleViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)
router.register('vehicle',vehicleViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive