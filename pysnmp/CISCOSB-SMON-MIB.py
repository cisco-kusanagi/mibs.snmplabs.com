#
# PySNMP MIB module CISCOSB-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Bits, Unsigned32, ModuleIdentity, NotificationType, Counter32, MibIdentifier, TimeTicks, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Bits", "Unsigned32", "ModuleIdentity", "NotificationType", "Counter32", "MibIdentifier", "TimeTicks", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
class CopyModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSmon.setOrganization('Cisco Small Business')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3), )
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
rlPortCopySessionsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopySessionsEnabled.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SMON-MIB", rlSmon=rlSmon, rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, rlPortCopySessionsEnabled=rlPortCopySessionsEnabled, rlPortCopySupport=rlPortCopySupport, PYSNMP_MODULE_ID=rlSmon, rlPortCopyMode=rlPortCopyMode, rlPortCopyMibVersion=rlPortCopyMibVersion, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable, CopyModeType=CopyModeType)
