#
# PySNMP MIB module Dell-VRTX-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-SMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:57:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Integer32, NotificationType, Bits, Unsigned32, Gauge32, IpAddress, ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Integer32", "NotificationType", "Bits", "Unsigned32", "Gauge32", "IpAddress", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "MibIdentifier")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
class CopyModeType(TextualConvention, Integer32):
    description = 'copy destination mode type: 1- monitor-only 2- network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSmon.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSmon.setOrganization('Dell')
if mibBuilder.loadTexts: rlSmon.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlSmon.setDescription('This private MIB module defines SMON private MIBs.')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyMibVersion.setDescription("MIB's version, the current version is 1.")
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
if mibBuilder.loadTexts: rlPortCopySupport.setDescription('supported - The standard portCopy is supported. notSupported - the standard portCopy is not supported. only basic portCopy operation is supported. ')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 84, 3), )
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setDescription('A supplementing table for portCopyTable. For every portCopyDest a vlan-tagging option is available.')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 84, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setDescription('Each entry specify how mirrored packets will transmit from the portCopyDest: Tagged or unTagged. The values in this entry will be valid only when the dot1dBasePort will be configured as a portCopyDest in the portCopyTable.')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 84, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setDescription('TRUE - Mirrored packets will transmit from portCopyDest - Tagged FALSE - Mirrored packets will transmit from portCopyDest - unTagged')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyMode.setDescription('This scalar defines a mode of the copy destination port')
rlPortCopySessionsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 84, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopySessionsEnabled.setStatus('current')
if mibBuilder.loadTexts: rlPortCopySessionsEnabled.setDescription('This scalar enables globaly port monitoring sessions ')
mibBuilder.exportSymbols("Dell-VRTX-SMON-MIB", rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable, rlPortCopyMode=rlPortCopyMode, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, rlPortCopyMibVersion=rlPortCopyMibVersion, rlPortCopySessionsEnabled=rlPortCopySessionsEnabled, rlPortCopySupport=rlPortCopySupport, rlSmon=rlSmon, CopyModeType=CopyModeType, PYSNMP_MODULE_ID=rlSmon)
