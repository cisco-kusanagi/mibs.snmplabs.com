#
# PySNMP MIB module WWP-EGRESS-PORT-RESTRICTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-EGRESS-PORT-RESTRICTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, Integer32, Gauge32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, iso, Counter32, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "iso", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpEgressPortRestrictionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 34))
wwpEgressPortRestrictionMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpEgressPortRestrictionMIB.setOrganization('World Wide Packets, Inc')
class PortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpEgressPortRestrictionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1))
wwpEgressPortRestriction = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1))
wwpEgressPortRestrictionNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2))
wwpEgressPortRestrictionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 2, 0))
wwpEgressPortRestrictionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3))
wwpEgressPortRestrictionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 1))
wwpEgressPortRestrictionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 34, 3, 2))
wwpEgressPortRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: wwpEgressPortRestrictionTable.setStatus('current')
wwpEgressPortRestrictionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestVlanId"), (0, "WWP-EGRESS-PORT-RESTRICTION-MIB", "wwpERestPortId"))
if mibBuilder.loadTexts: wwpEgressPortRestrictionEntry.setStatus('current')
wwpERestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestVlanId.setStatus('current')
wwpERestPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpERestPortId.setStatus('current')
wwpERestEgreesPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 3), PortList().clone(hexValue="0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpERestEgreesPorts.setStatus('current')
wwpERestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 34, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpERestStatus.setStatus('current')
mibBuilder.exportSymbols("WWP-EGRESS-PORT-RESTRICTION-MIB", wwpEgressPortRestrictionMIBGroups=wwpEgressPortRestrictionMIBGroups, wwpEgressPortRestriction=wwpEgressPortRestriction, wwpEgressPortRestrictionTable=wwpEgressPortRestrictionTable, PYSNMP_MODULE_ID=wwpEgressPortRestrictionMIB, wwpERestVlanId=wwpERestVlanId, wwpERestPortId=wwpERestPortId, wwpERestStatus=wwpERestStatus, wwpEgressPortRestrictionMIBObjects=wwpEgressPortRestrictionMIBObjects, wwpEgressPortRestrictionMIBConformance=wwpEgressPortRestrictionMIBConformance, wwpERestEgreesPorts=wwpERestEgreesPorts, wwpEgressPortRestrictionNotificationPrefix=wwpEgressPortRestrictionNotificationPrefix, VlanId=VlanId, wwpEgressPortRestrictionNotifications=wwpEgressPortRestrictionNotifications, wwpEgressPortRestrictionMIBCompliances=wwpEgressPortRestrictionMIBCompliances, wwpEgressPortRestrictionEntry=wwpEgressPortRestrictionEntry, wwpEgressPortRestrictionMIB=wwpEgressPortRestrictionMIB, PortList=PortList)
