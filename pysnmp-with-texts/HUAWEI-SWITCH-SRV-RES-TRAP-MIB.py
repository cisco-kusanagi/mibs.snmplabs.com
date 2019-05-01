#
# PySNMP MIB module HUAWEI-SWITCH-SRV-RES-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SWITCH-SRV-RES-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, TimeTicks, Counter64, IpAddress, Bits, iso, ModuleIdentity, Integer32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "TimeTicks", "Counter64", "IpAddress", "Bits", "iso", "ModuleIdentity", "Integer32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwSwitchSrvResTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334))
hwSwitchSrvResTrapMIB.setRevisions(('2014-08-06 08:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setRevisionsDescriptions((' Version 1.00.',))
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setLastUpdated('201408060858Z')
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwSwitchSrvResTrapMIB.setDescription('The private mib file includes the alarm information of fowarding engine resouce overload.')
hwSrvResTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1))
hwSrvServiceId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("gvrpInterface", 1), ("dldpInterface", 2), ("igmpSnoopingQuerier", 3), ("multicastUserVlan", 4), ("portSecMac", 5), ("stormControlInterface", 6), ("sflowInterface", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvServiceId.setStatus('current')
if mibBuilder.loadTexts: hwSrvServiceId.setDescription('The ID of service.')
hwSrvServiceDescr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvServiceDescr.setStatus('current')
if mibBuilder.loadTexts: hwSrvServiceDescr.setDescription('The description of service.')
hwSrvRecommendThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSrvRecommendThreshold.setStatus('current')
if mibBuilder.loadTexts: hwSrvRecommendThreshold.setDescription('The recommended threshold.')
hwSrvResTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2))
hwSrvSeviceResTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1))
hwSrvServiceExceedThreshould = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if mibBuilder.loadTexts: hwSrvServiceExceedThreshould.setStatus('current')
if mibBuilder.loadTexts: hwSrvServiceExceedThreshould.setDescription('The service exceed the recommended threshold.')
hwSrvServiceExceedThreshouldResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 2)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if mibBuilder.loadTexts: hwSrvServiceExceedThreshouldResume.setStatus('current')
if mibBuilder.loadTexts: hwSrvServiceExceedThreshouldResume.setDescription('The service fall below the recommended threshold.')
hwSrvResTrapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100))
hwSrvResTrapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1))
hwSrvResTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvResObjectGroup"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvResTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResTrapCompliance = hwSrvResTrapCompliance.setStatus('current')
if mibBuilder.loadTexts: hwSrvResTrapCompliance.setDescription('Compliance statement for agents that provide full support for hwSrvResTrapMIB.')
hwSrvResTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2))
hwSrvResObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 1)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResObjectGroup = hwSrvResObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwSrvResObjectGroup.setDescription('Group for base trap objects.')
hwSrvResTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 2)).setObjects(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshould"), ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshouldResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSrvResTrapGroup = hwSrvResTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwSrvResTrapGroup.setDescription('Group for all traps.')
mibBuilder.exportSymbols("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", hwSwitchSrvResTrapMIB=hwSwitchSrvResTrapMIB, hwSrvResTrapCompliances=hwSrvResTrapCompliances, hwSrvResObjectGroup=hwSrvResObjectGroup, hwSrvServiceId=hwSrvServiceId, hwSrvSeviceResTrap=hwSrvSeviceResTrap, hwSrvServiceDescr=hwSrvServiceDescr, PYSNMP_MODULE_ID=hwSwitchSrvResTrapMIB, hwSrvServiceExceedThreshould=hwSrvServiceExceedThreshould, hwSrvServiceExceedThreshouldResume=hwSrvServiceExceedThreshouldResume, hwSrvResTrapObject=hwSrvResTrapObject, hwSrvResTrapConformance=hwSrvResTrapConformance, hwSrvResTrapGroup=hwSrvResTrapGroup, hwSrvResTrapGroups=hwSrvResTrapGroups, hwSrvResTraps=hwSrvResTraps, hwSrvRecommendThreshold=hwSrvRecommendThreshold, hwSrvResTrapCompliance=hwSrvResTrapCompliance)
