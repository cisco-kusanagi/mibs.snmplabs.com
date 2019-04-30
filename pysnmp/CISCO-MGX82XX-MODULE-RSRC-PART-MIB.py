#
# PySNMP MIB module CISCO-MGX82XX-MODULE-RSRC-PART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-MODULE-RSRC-PART-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Unsigned32, TimeTicks, Counter64, ModuleIdentity, Gauge32, Integer32, NotificationType, IpAddress, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "Integer32", "NotificationType", "IpAddress", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx82xxModuleRsrcPartMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 73))
ciscoMgx82xxModuleRsrcPartMIB.setRevisions(('2003-04-18 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setLastUpdated('200304180000Z')
if mibBuilder.loadTexts: ciscoMgx82xxModuleRsrcPartMIB.setOrganization('Cisco Systems, Inc.')
cardResourcePartition = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 9))
cardLcnPartitionType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noPartition", 1), ("controllerBased", 2), ("portControllerBased", 3))).clone('noPartition')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardLcnPartitionType.setStatus('current')
cardResPartGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2), )
if mibBuilder.loadTexts: cardResPartGrpTable.setStatus('current')
cardResPartGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1), ).setIndexNames((0, "CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"))
if mibBuilder.loadTexts: cardResPartGrpEntry.setStatus('current')
cardResPartCtrlrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("par", 1), ("pnni", 2), ("tag", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardResPartCtrlrNum.setStatus('current')
cardResPartRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartRowStatus.setStatus('current')
cardResPartNumOfLcnAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardResPartNumOfLcnAvail.setStatus('current')
cmmRsrcPartMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2))
cmmRsrcPartMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1))
cmmRsrcPartMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2))
cmmRsrcPartCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cmmRsrcPartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartCompliance = cmmRsrcPartCompliance.setStatus('current')
cmmRsrcPartGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2, 1)).setObjects(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardLcnPartitionType"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartRowStatus"), ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartNumOfLcnAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmRsrcPartGroup = cmmRsrcPartGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", cardResPartGrpTable=cardResPartGrpTable, ciscoMgx82xxModuleRsrcPartMIB=ciscoMgx82xxModuleRsrcPartMIB, cmmRsrcPartMIBConformance=cmmRsrcPartMIBConformance, cmmRsrcPartMIBCompliances=cmmRsrcPartMIBCompliances, cmmRsrcPartGroup=cmmRsrcPartGroup, cardResPartNumOfLcnAvail=cardResPartNumOfLcnAvail, cardResourcePartition=cardResourcePartition, cmmRsrcPartMIBGroups=cmmRsrcPartMIBGroups, cmmRsrcPartCompliance=cmmRsrcPartCompliance, cardResPartRowStatus=cardResPartRowStatus, cardResPartCtrlrNum=cardResPartCtrlrNum, cardLcnPartitionType=cardLcnPartitionType, PYSNMP_MODULE_ID=ciscoMgx82xxModuleRsrcPartMIB, cardResPartGrpEntry=cardResPartGrpEntry)
