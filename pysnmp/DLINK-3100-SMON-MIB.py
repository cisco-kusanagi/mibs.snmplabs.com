#
# PySNMP MIB module DLINK-3100-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-SMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:34:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, ObjectIdentity, Counter32, Counter64, Unsigned32, IpAddress, Gauge32, ModuleIdentity, Bits, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
class CopyModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSmon.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3), )
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-SMON-MIB", PYSNMP_MODULE_ID=rlSmon, rlSmon=rlSmon, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopySupport=rlPortCopySupport, rlPortCopyMibVersion=rlPortCopyMibVersion, CopyModeType=CopyModeType, rlPortCopyMode=rlPortCopyMode, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable)
