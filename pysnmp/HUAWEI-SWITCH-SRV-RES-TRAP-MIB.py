#
# PySNMP MIB module HUAWEI-SWITCH-SRV-RES-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SWITCH-SRV-RES-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Bits, Unsigned32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Counter64, ModuleIdentity, Gauge32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Unsigned32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwSwitchSrvResTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334))
hwSwitchSrvResTrapMIB.setRevisions(('2014-08-06 08:58',))
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setLastUpdated('201408060858Z')
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwSrvResTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1))
hwSrvServiceId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("gvrpInterface", 1), ("dldpInterface", 2), ("igmpSnoopingQuerier", 3), ("multicastUserVlan", 4), ("portSecMac", 5), ("stormControlInterface", 6), ("sflowInterface", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvServiceId.setStatus('current')
hwSrvServiceDescr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvServiceDescr.setStatus('current')
hwSrvRecommendThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvRecommendThreshold.setStatus('current')
hwSrvResTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2))
hwSrvSeviceResTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1))
hwSrvServiceExceedThreshould = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if mibBuilder.loadTexts: hwSrvServiceExceedThreshould.setStatus('current')
hwSrvServiceExceedThreshouldResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 2)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if mibBuilder.loadTexts: hwSrvServiceExceedThreshouldResume.setStatus('current')
hwSrvResTrapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100))
hwSrvResTrapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1))
hwSrvResTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvResObjectGroup"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvResTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResTrapCompliance = hwSrvResTrapCompliance.setStatus('current')
hwSrvResTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2))
hwSrvResObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResObjectGroup = hwSrvResObjectGroup.setStatus('current')
hwSrvResTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 2)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshould"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshouldResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResTrapGroup = hwSrvResTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", hwSrvResTraps=hwSrvResTraps, hwSrvServiceDescr=hwSrvServiceDescr, hwSrvResTrapCompliance=hwSrvResTrapCompliance, hwSwitchSrvResTrapMIB=hwSwitchSrvResTrapMIB, hwSrvRecommendThreshold=hwSrvRecommendThreshold, hwSrvServiceExceedThreshouldResume=hwSrvServiceExceedThreshouldResume, PYSNMP_MODULE_ID=hwSwitchSrvResTrapMIB, hwSrvResTrapGroup=hwSrvResTrapGroup, hwSrvResTrapConformance=hwSrvResTrapConformance, hwSrvServiceId=hwSrvServiceId, hwSrvServiceExceedThreshould=hwSrvServiceExceedThreshould, hwSrvResObjectGroup=hwSrvResObjectGroup, hwSrvSeviceResTrap=hwSrvSeviceResTrap, hwSrvResTrapCompliances=hwSrvResTrapCompliances, hwSrvResTrapObject=hwSrvResTrapObject, hwSrvResTrapGroups=hwSrvResTrapGroups)
