from relationmtom.viewsets import personViewset,phoneViewset,aadarViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('phone',phoneViewset)
router.register('person',personViewset)
router.register('aadar',aadarViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive