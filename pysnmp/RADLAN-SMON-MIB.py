#
# PySNMP MIB module RADLAN-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, iso, Unsigned32, Bits, Integer32, Gauge32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "iso", "Unsigned32", "Bits", "Integer32", "Gauge32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
class CopyModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSmon.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 84, 3), )
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 84, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 84, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
rlPortCopySessionsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopySessionsEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SMON-MIB", rlPortCopySupport=rlPortCopySupport, PYSNMP_MODULE_ID=rlSmon, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, CopyModeType=CopyModeType, rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable, rlPortCopyMibVersion=rlPortCopyMibVersion, rlPortCopySessionsEnabled=rlPortCopySessionsEnabled, rlSmon=rlSmon, rlPortCopyMode=rlPortCopyMode)
