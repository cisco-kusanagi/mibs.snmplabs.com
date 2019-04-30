#
# PySNMP MIB module IF-CAP-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IF-CAP-STACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifInvStackGroup, = mibBuilder.importSymbols("IF-INVERTED-STACK-MIB", "ifInvStackGroup")
ifStackHigherLayer, ifStackLowerLayer, ifStackGroup2 = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifStackLowerLayer", "ifStackGroup2")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, mib_2, TimeTicks, Gauge32, Counter32, MibIdentifier, iso, Counter64, ObjectIdentity, Bits, Unsigned32, IpAddress, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "mib-2", "TimeTicks", "Gauge32", "Counter32", "MibIdentifier", "iso", "Counter64", "ObjectIdentity", "Bits", "Unsigned32", "IpAddress", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ifCapStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 166))
ifCapStackMIB.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: ifCapStackMIB.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: ifCapStackMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
ifCapStackObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 1))
ifCapStackConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2))
ifCapStackTable = MibTable((1, 3, 6, 1, 2, 1, 166, 1, 1), )
if mibBuilder.loadTexts: ifCapStackTable.setStatus('current')
ifCapStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 166, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifStackHigherLayer"), (0, "IF-MIB", "ifStackLowerLayer"))
if mibBuilder.loadTexts: ifCapStackEntry.setStatus('current')
ifCapStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 166, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCapStackStatus.setStatus('current')
ifInvCapStackTable = MibTable((1, 3, 6, 1, 2, 1, 166, 1, 2), )
if mibBuilder.loadTexts: ifInvCapStackTable.setStatus('current')
ifInvCapStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 166, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvCapStackEntry.setStatus('current')
ifInvCapStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 166, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvCapStackStatus.setStatus('current')
ifCapStackGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2, 1))
ifCapStackCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 166, 2, 2))
ifCapStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 166, 2, 1, 1)).setObjects(("IF-CAP-STACK-MIB", "ifCapStackStatus"), ("IF-CAP-STACK-MIB", "ifInvCapStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCapStackGroup = ifCapStackGroup.setStatus('current')
ifCapStackCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 166, 2, 2, 1)).setObjects(("IF-CAP-STACK-MIB", "ifCapStackGroup"), ("IF-MIB", "ifStackGroup2"), ("IF-INVERTED-STACK-MIB", "ifInvStackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCapStackCompliance = ifCapStackCompliance.setStatus('current')
mibBuilder.exportSymbols("IF-CAP-STACK-MIB", ifCapStackCompliance=ifCapStackCompliance, ifCapStackEntry=ifCapStackEntry, ifCapStackGroups=ifCapStackGroups, ifCapStackObjects=ifCapStackObjects, PYSNMP_MODULE_ID=ifCapStackMIB, ifCapStackMIB=ifCapStackMIB, ifInvCapStackTable=ifInvCapStackTable, ifInvCapStackEntry=ifInvCapStackEntry, ifCapStackTable=ifCapStackTable, ifCapStackCompliances=ifCapStackCompliances, ifCapStackStatus=ifCapStackStatus, ifInvCapStackStatus=ifInvCapStackStatus, ifCapStackGroup=ifCapStackGroup, ifCapStackConformance=ifCapStackConformance)
