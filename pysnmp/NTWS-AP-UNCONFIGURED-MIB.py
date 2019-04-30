#
# PySNMP MIB module NTWS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-UNCONFIGURED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
NtwsPhysPortNumber, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ObjectIdentity, ModuleIdentity, Unsigned32, Gauge32, NotificationType, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Gauge32", "NotificationType", "Counter64", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15))
ntwsApUnconfiguredMib.setRevisions(('2008-11-14 00:04',))
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setLastUpdated('200811140004Z')
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setOrganization('Nortel Networks')
class NtwsApUnconfiguredOrphanReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

ntwsApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1))
ntwsApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2), )
if mibBuilder.loadTexts: ntwsApUnconfOrphanTable.setStatus('current')
ntwsApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1), ).setIndexNames((0, "NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: ntwsApUnconfOrphanEntry.setStatus('current')
ntwsApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApUnconfOrphanApSerialNum.setStatus('current')
ntwsApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanApModelName.setStatus('current')
ntwsApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanIpAddress.setStatus('current')
ntwsApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 6), NtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanPhysPortNum.setStatus('current')
ntwsApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanVLANName.setStatus('current')
ntwsApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 8), NtwsApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanReason.setStatus('current')
ntwsApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2))
ntwsApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1))
ntwsApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2))
ntwsApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfCompliance = ntwsApUnconfCompliance.setStatus('current')
ntwsApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApModelName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanIpAddress"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanPhysPortNum"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanVLANName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfOrphanBasicGroup = ntwsApUnconfOrphanBasicGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-AP-UNCONFIGURED-MIB", PYSNMP_MODULE_ID=ntwsApUnconfiguredMib, ntwsApUnconfGroups=ntwsApUnconfGroups, ntwsApUnconfMibObjects=ntwsApUnconfMibObjects, ntwsApUnconfOrphanPhysPortNum=ntwsApUnconfOrphanPhysPortNum, ntwsApUnconfOrphanReason=ntwsApUnconfOrphanReason, ntwsApUnconfCompliances=ntwsApUnconfCompliances, ntwsApUnconfOrphanBasicGroup=ntwsApUnconfOrphanBasicGroup, ntwsApUnconfConformance=ntwsApUnconfConformance, ntwsApUnconfCompliance=ntwsApUnconfCompliance, ntwsApUnconfOrphanTable=ntwsApUnconfOrphanTable, ntwsApUnconfOrphanIpAddress=ntwsApUnconfOrphanIpAddress, ntwsApUnconfOrphanVLANName=ntwsApUnconfOrphanVLANName, ntwsApUnconfOrphanApModelName=ntwsApUnconfOrphanApModelName, ntwsApUnconfiguredMib=ntwsApUnconfiguredMib, ntwsApUnconfOrphanEntry=ntwsApUnconfOrphanEntry, ntwsApUnconfOrphanApSerialNum=ntwsApUnconfOrphanApSerialNum, NtwsApUnconfiguredOrphanReason=NtwsApUnconfiguredOrphanReason)
