#
# PySNMP MIB module DLINK-3100-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-SMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:48:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, NotificationType, Unsigned32, Gauge32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter64, Integer32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "Bits", "ModuleIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
class CopyModeType(TextualConvention, Integer32):
    description = 'copy destination mode type: 1- monitor-only 2- network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSmon.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSmon.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
if mibBuilder.loadTexts: rlSmon.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlSmon.setDescription('This private MIB module defines SMON private MIBs.')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyMibVersion.setDescription("MIB's version, the current version is 1.")
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
if mibBuilder.loadTexts: rlPortCopySupport.setDescription('supported - The standard portCopy is supported. notSupported - the standard portCopy is not supported. only basic portCopy operation is supported. ')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3), )
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setDescription('A supplementing table for portCopyTable. For every portCopyDest a vlan-tagging option is available.')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setDescription('Each entry specify how mirrored packets will transmit from the portCopyDest: Tagged or unTagged. The values in this entry will be valid only when the dot1dBasePort will be configured as a portCopyDest in the portCopyTable.')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setDescription('TRUE - Mirrored packets will transmit from portCopyDest - Tagged FALSE - Mirrored packets will transmit from portCopyDest - unTagged')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
if mibBuilder.loadTexts: rlPortCopyMode.setDescription('This scalar defined a mode of the copy destination port')
mibBuilder.exportSymbols("DLINK-3100-SMON-MIB", PYSNMP_MODULE_ID=rlSmon, rlPortCopyMibVersion=rlPortCopyMibVersion, rlSmon=rlSmon, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable, rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopyMode=rlPortCopyMode, CopyModeType=CopyModeType, rlPortCopySupport=rlPortCopySupport)
