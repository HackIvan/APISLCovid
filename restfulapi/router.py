from covidslapi.viewsets import latestUpdateSLViewset
from covidslapi.viewsets import districtCasesViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('latest',latestUpdateSLViewset,)
router.register('district',districtCasesViewset,)