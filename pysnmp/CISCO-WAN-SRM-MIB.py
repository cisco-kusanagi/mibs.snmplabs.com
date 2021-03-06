#
# PySNMP MIB module CISCO-WAN-SRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-SRM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, Integer32, Counter32, Unsigned32, TimeTicks, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Integer32", "Counter32", "Unsigned32", "TimeTicks", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanSrmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 30))
ciscoWanSrmMIB.setRevisions(('2002-08-26 00:00',))
if mibBuilder.loadTexts: ciscoWanSrmMIB.setLastUpdated('200208260000Z')
if mibBuilder.loadTexts: ciscoWanSrmMIB.setOrganization('Cisco Systems, Inc.')
srm3T3CnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 10))
srmeCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 22))
srm3T3CnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1), )
if mibBuilder.loadTexts: srm3T3CnfGrpTable.setStatus('current')
srm3T3CnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1), ).setIndexNames((0, "CISCO-WAN-SRM-MIB", "srmT3LineNum"), (0, "CISCO-WAN-SRM-MIB", "srmStartT1LineNum"))
if mibBuilder.loadTexts: srm3T3CnfGrpEntry.setStatus('current')
srmT3LineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmT3LineNum.setStatus('current')
srmStartT1LineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmStartT1LineNum.setStatus('current')
srmT1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmT1RowStatus.setStatus('current')
srmTargetSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmTargetSlotNum.setStatus('current')
srmTargetSlotLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmTargetSlotLineNum.setStatus('current')
srmeCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1), )
if mibBuilder.loadTexts: srmeCnfGrpTable.setStatus('current')
srmeCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1), ).setIndexNames((0, "CISCO-WAN-SRM-MIB", "srmeLineNum"), (0, "CISCO-WAN-SRM-MIB", "srmeStartVtNum"))
if mibBuilder.loadTexts: srmeCnfGrpEntry.setStatus('current')
srmeLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmeLineNum.setStatus('current')
srmeStartVtNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srmeStartVtNum.setStatus('current')
srmeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeRowStatus.setStatus('current')
srmeTargetSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeTargetSlotNum.setStatus('current')
srmeTargetSlotLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeTargetSlotLineNum.setStatus('current')
srmeVtFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 3, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("sf", 2), ("esf", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srmeVtFramingType.setStatus('current')
ciscoWanSrmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 30, 2))
ciscoWanSrmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 30, 2, 1))
ciscoWanSrmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 30, 2, 2))
ciscoWanSrmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 30, 2, 2, 1)).setObjects(("CISCO-WAN-SRM-MIB", "ciscoWanSrmConfGroup"), ("CISCO-WAN-SRM-MIB", "ciscoWanSrmeConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmCompliance = ciscoWanSrmCompliance.setStatus('current')
ciscoWanSrmConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 30, 2, 1, 1)).setObjects(("CISCO-WAN-SRM-MIB", "srmT3LineNum"), ("CISCO-WAN-SRM-MIB", "srmStartT1LineNum"), ("CISCO-WAN-SRM-MIB", "srmT1RowStatus"), ("CISCO-WAN-SRM-MIB", "srmTargetSlotNum"), ("CISCO-WAN-SRM-MIB", "srmTargetSlotLineNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmConfGroup = ciscoWanSrmConfGroup.setStatus('current')
ciscoWanSrmeConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 30, 2, 1, 2)).setObjects(("CISCO-WAN-SRM-MIB", "srmeLineNum"), ("CISCO-WAN-SRM-MIB", "srmeStartVtNum"), ("CISCO-WAN-SRM-MIB", "srmeRowStatus"), ("CISCO-WAN-SRM-MIB", "srmeTargetSlotNum"), ("CISCO-WAN-SRM-MIB", "srmeTargetSlotLineNum"), ("CISCO-WAN-SRM-MIB", "srmeVtFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmeConfGroup = ciscoWanSrmeConfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-SRM-MIB", srmT3LineNum=srmT3LineNum, ciscoWanSrmCompliance=ciscoWanSrmCompliance, srmeCnfGrp=srmeCnfGrp, ciscoWanSrmMIBConformance=ciscoWanSrmMIBConformance, ciscoWanSrmMIBCompliances=ciscoWanSrmMIBCompliances, ciscoWanSrmConfGroup=ciscoWanSrmConfGroup, srmT1RowStatus=srmT1RowStatus, srmeTargetSlotNum=srmeTargetSlotNum, srmeCnfGrpTable=srmeCnfGrpTable, srm3T3CnfGrpTable=srm3T3CnfGrpTable, ciscoWanSrmMIBGroups=ciscoWanSrmMIBGroups, PYSNMP_MODULE_ID=ciscoWanSrmMIB, srmeVtFramingType=srmeVtFramingType, srmTargetSlotLineNum=srmTargetSlotLineNum, srmTargetSlotNum=srmTargetSlotNum, srmeCnfGrpEntry=srmeCnfGrpEntry, srmeTargetSlotLineNum=srmeTargetSlotLineNum, srmeStartVtNum=srmeStartVtNum, ciscoWanSrmeConfGroup=ciscoWanSrmeConfGroup, srmeLineNum=srmeLineNum, ciscoWanSrmMIB=ciscoWanSrmMIB, srmeRowStatus=srmeRowStatus, srm3T3CnfGrpEntry=srm3T3CnfGrpEntry, srmStartT1LineNum=srmStartT1LineNum, srm3T3CnfGrp=srm3T3CnfGrp)
