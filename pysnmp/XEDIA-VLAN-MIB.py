#
# PySNMP MIB module XEDIA-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ModuleIdentity, Counter64, NotificationType, Integer32, ObjectIdentity, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "iso")
TruthValue, DisplayString, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeInterval", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 34))
if mibBuilder.loadTexts: xediaVlanMIB.setLastUpdated('9905212155Z')
if mibBuilder.loadTexts: xediaVlanMIB.setOrganization('Xedia Corp.')
xVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 34, 1))
xVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 34, 2))
class Unsigned32(Gauge32):
    pass

xVlanIDTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1), )
if mibBuilder.loadTexts: xVlanIDTable.setStatus('current')
xVlanIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xVlanIDEntry.setStatus('current')
xVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xVlanID.setStatus('current')
xVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2), )
if mibBuilder.loadTexts: xVlanConfigTable.setStatus('current')
xVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xVlanConfigEntry.setStatus('current')
xVlanConfigAdmitTaggedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVlanConfigAdmitTaggedFrames.setStatus('current')
xVlanConfigAdmitConfiguredVlansOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVlanConfigAdmitConfiguredVlansOnly.setStatus('current')
xVlanConfigStripBridgedTags = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVlanConfigStripBridgedTags.setStatus('current')
xVlanConfigGVRP = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVlanConfigGVRP.setStatus('current')
xVlanConfigGARPJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 34, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 21474800)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVlanConfigGARPJoinTime.setStatus('current')
xVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 1))
xVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 2))
xVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 1, 1)).setObjects(("XEDIA-VLAN-MIB", "xVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xVlanCompliance = xVlanCompliance.setStatus('current')
xVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 34, 2, 2, 1)).setObjects(("XEDIA-VLAN-MIB", "xVlanID"), ("XEDIA-VLAN-MIB", "xVlanConfigAdmitTaggedFrames"), ("XEDIA-VLAN-MIB", "xVlanConfigAdmitConfiguredVlansOnly"), ("XEDIA-VLAN-MIB", "xVlanConfigStripBridgedTags"), ("XEDIA-VLAN-MIB", "xVlanConfigGVRP"), ("XEDIA-VLAN-MIB", "xVlanConfigGARPJoinTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xVlanGroup = xVlanGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-VLAN-MIB", xVlanCompliance=xVlanCompliance, xVlanConformance=xVlanConformance, xVlanID=xVlanID, Unsigned32=Unsigned32, xVlanIDEntry=xVlanIDEntry, xVlanObjects=xVlanObjects, xVlanCompliances=xVlanCompliances, xVlanConfigGARPJoinTime=xVlanConfigGARPJoinTime, xVlanConfigEntry=xVlanConfigEntry, xediaVlanMIB=xediaVlanMIB, xVlanConfigTable=xVlanConfigTable, xVlanConfigAdmitConfiguredVlansOnly=xVlanConfigAdmitConfiguredVlansOnly, xVlanGroup=xVlanGroup, xVlanConfigGVRP=xVlanConfigGVRP, xVlanGroups=xVlanGroups, xVlanIDTable=xVlanIDTable, PYSNMP_MODULE_ID=xediaVlanMIB, xVlanConfigAdmitTaggedFrames=xVlanConfigAdmitTaggedFrames, xVlanConfigStripBridgedTags=xVlanConfigStripBridgedTags)
