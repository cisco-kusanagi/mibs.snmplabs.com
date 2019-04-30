#
# PySNMP MIB module IEEE8021-MVRPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-MVRPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Unsigned32, TimeTicks, NotificationType, Counter64, Gauge32, Counter32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "Counter32", "iso", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ieee8021MvrpxMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 22))
ieee8021MvrpxMib.setRevisions(('2014-12-15 00:00', '2011-04-05 00:00',))
if mibBuilder.loadTexts: ieee8021MvrpxMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021MvrpxMib.setOrganization('IEEE 802.1 Working Group')
ieee8021MvrpxMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 1))
ieee8021MvrpxConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2))
ieee8021MvrpxPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 22, 1, 1), )
if mibBuilder.loadTexts: ieee8021MvrpxPortTable.setStatus('current')
ieee8021MvrpxPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortEntry"))
ieee8021MvrpxPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MvrpxPortEntry.setStatus('current')
ieee8021MvrpxPortNewOnly = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortNewOnly.setStatus('current')
ieee8021MvrpxPortMvrpNewPropagated = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortMvrpNewPropagated.setStatus('current')
ieee8021MvrpxPortXmitZero = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortXmitZero.setStatus('current')
ieee8021MvrpxCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 1))
ieee8021MvrpxGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 2))
ieee8021MvrpxReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 22, 2, 2, 1)).setObjects(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortNewOnly"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortMvrpNewPropagated"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortXmitZero"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxReqdGroup = ieee8021MvrpxReqdGroup.setStatus('current')
ieee8021MvrpxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 22, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxCompliance = ieee8021MvrpxCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-MVRPX-MIB", ieee8021MvrpxCompliance=ieee8021MvrpxCompliance, PYSNMP_MODULE_ID=ieee8021MvrpxMib, ieee8021MvrpxMIBObjects=ieee8021MvrpxMIBObjects, ieee8021MvrpxPortTable=ieee8021MvrpxPortTable, ieee8021MvrpxPortEntry=ieee8021MvrpxPortEntry, ieee8021MvrpxPortXmitZero=ieee8021MvrpxPortXmitZero, ieee8021MvrpxGroups=ieee8021MvrpxGroups, ieee8021MvrpxReqdGroup=ieee8021MvrpxReqdGroup, ieee8021MvrpxConformance=ieee8021MvrpxConformance, ieee8021MvrpxMib=ieee8021MvrpxMib, ieee8021MvrpxPortNewOnly=ieee8021MvrpxPortNewOnly, ieee8021MvrpxPortMvrpNewPropagated=ieee8021MvrpxPortMvrpNewPropagated, ieee8021MvrpxCompliances=ieee8021MvrpxCompliances)
