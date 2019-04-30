#
# PySNMP MIB module CISCO-SWITCH-CGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-CGMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, IpAddress, Bits, ObjectIdentity, Gauge32, Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks", "iso")
RowStatus, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention")
ciscoSwitchCgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 101))
ciscoSwitchCgmpMIB.setRevisions(('1998-05-07 00:00',))
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setLastUpdated('9805070000Z')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setOrganization('Cisco Systems, Inc')
ciscoSwitchCgmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1))
sCgmpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1))
class SCgmpVlanIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1023)

sCgmpEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpEnable.setStatus('current')
sCgmpFastLeaveEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setStatus('current')
sCgmpRouterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 6000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setStatus('current')
sCgmpRouterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4), )
if mibBuilder.loadTexts: sCgmpRouterTable.setStatus('current')
sCgmpRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterVlanIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterMacAddress"))
if mibBuilder.loadTexts: sCgmpRouterEntry.setStatus('current')
sCgmpRouterVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 1), SCgmpVlanIndex())
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setStatus('current')
sCgmpRouterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setStatus('current')
sCgmpRouterEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setStatus('current')
ciscoSwitchCgmpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3))
ciscoSwitchCgmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1))
ciscoSwitchCgmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2))
ciscoSwitchCgmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCgmpMIBCompliance = ciscoSwitchCgmpMIBCompliance.setStatus('current')
sCgmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpFastLeaveEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterHoldTime"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sCgmpGroup = sCgmpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-CGMP-MIB", sCgmpRouterEntry=sCgmpRouterEntry, sCgmpEnable=sCgmpEnable, ciscoSwitchCgmpMIBObjects=ciscoSwitchCgmpMIBObjects, sCgmpGroup=sCgmpGroup, sCgmpRouterEntryStatus=sCgmpRouterEntryStatus, sCgmpRouterVlanIndex=sCgmpRouterVlanIndex, ciscoSwitchCgmpMIBGroups=ciscoSwitchCgmpMIBGroups, ciscoSwitchCgmpMIBCompliances=ciscoSwitchCgmpMIBCompliances, PYSNMP_MODULE_ID=ciscoSwitchCgmpMIB, sCgmpInfo=sCgmpInfo, sCgmpFastLeaveEnable=sCgmpFastLeaveEnable, sCgmpRouterHoldTime=sCgmpRouterHoldTime, ciscoSwitchCgmpMIB=ciscoSwitchCgmpMIB, sCgmpRouterMacAddress=sCgmpRouterMacAddress, ciscoSwitchCgmpMIBCompliance=ciscoSwitchCgmpMIBCompliance, sCgmpRouterTable=sCgmpRouterTable, SCgmpVlanIndex=SCgmpVlanIndex, ciscoSwitchCgmpMIBConformance=ciscoSwitchCgmpMIBConformance)
