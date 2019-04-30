#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Unsigned32, Gauge32, NotificationType, ObjectIdentity, Counter64, iso, TimeTicks, Counter32, IpAddress, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "iso", "TimeTicks", "Counter32", "IpAddress", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
TrpzPhysPortNumber, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumber")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 15))
trpzApUnconfiguredMib.setRevisions(('2011-06-15 00:11', '2008-11-14 00:04',))
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setLastUpdated('201106150011Z')
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setOrganization('Trapeze Networks')
class TrpzApUnconfiguredOrphanReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

trpzApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1))
trpzApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2), )
if mibBuilder.loadTexts: trpzApUnconfOrphanTable.setStatus('current')
trpzApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: trpzApUnconfOrphanEntry.setStatus('current')
trpzApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApUnconfOrphanApSerialNum.setStatus('current')
trpzApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanApModelName.setStatus('current')
trpzApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanIpAddress.setStatus('current')
trpzApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 6), TrpzPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanPhysPortNum.setStatus('current')
trpzApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanVLANName.setStatus('current')
trpzApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 8), TrpzApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanReason.setStatus('current')
trpzApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2))
trpzApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1))
trpzApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2))
trpzApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfCompliance = trpzApUnconfCompliance.setStatus('current')
trpzApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApModelName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanIpAddress"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanPhysPortNum"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanVLANName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfOrphanBasicGroup = trpzApUnconfOrphanBasicGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", trpzApUnconfGroups=trpzApUnconfGroups, trpzApUnconfOrphanEntry=trpzApUnconfOrphanEntry, trpzApUnconfOrphanApSerialNum=trpzApUnconfOrphanApSerialNum, trpzApUnconfOrphanPhysPortNum=trpzApUnconfOrphanPhysPortNum, trpzApUnconfOrphanTable=trpzApUnconfOrphanTable, trpzApUnconfConformance=trpzApUnconfConformance, trpzApUnconfOrphanApModelName=trpzApUnconfOrphanApModelName, trpzApUnconfCompliances=trpzApUnconfCompliances, trpzApUnconfMibObjects=trpzApUnconfMibObjects, TrpzApUnconfiguredOrphanReason=TrpzApUnconfiguredOrphanReason, trpzApUnconfOrphanReason=trpzApUnconfOrphanReason, trpzApUnconfOrphanBasicGroup=trpzApUnconfOrphanBasicGroup, trpzApUnconfOrphanVLANName=trpzApUnconfOrphanVLANName, trpzApUnconfCompliance=trpzApUnconfCompliance, PYSNMP_MODULE_ID=trpzApUnconfiguredMib, trpzApUnconfiguredMib=trpzApUnconfiguredMib, trpzApUnconfOrphanIpAddress=trpzApUnconfOrphanIpAddress)
