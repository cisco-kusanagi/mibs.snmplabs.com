#
# PySNMP MIB module H3C-QOS-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-QOS-CAPABILITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
h3cSNMPAgCpb, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cSNMPAgCpb")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Gauge32, Counter32, Counter64, Integer32, Unsigned32, iso, TimeTicks, IpAddress, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Gauge32", "Counter32", "Counter64", "Integer32", "Unsigned32", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1))
if mibBuilder.loadTexts: h3cQosCapability.setLastUpdated('200508300000Z')
if mibBuilder.loadTexts: h3cQosCapability.setOrganization('Huawei 3Com Technologies Co.,Ltd.')
h3cQoSCapabilityMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1))
class CapabilityPhysicalType(TextualConvention, Integer32):
    reference = 'rfc2737 ENTITY-MIB '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("stack", 1), ("chassis", 2), ("module", 3), ("port", 4))

h3cQoSCapabilityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1))
h3cQoSCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1), )
if mibBuilder.loadTexts: h3cQoSCapabilityTable.setStatus('current')
h3cQoSCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1), ).setIndexNames((0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalType"), (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalIndex"), (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSModuleIndex"), (0, "H3C-QOS-CAPABILITY-MIB", "h3cQoSCharacteristicsIndex"))
if mibBuilder.loadTexts: h3cQoSCapabilityEntry.setStatus('current')
h3cQoSCapabilityPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 1), CapabilityPhysicalType())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalType.setStatus('current')
h3cQoSCapabilityPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalIndex.setStatus('current')
h3cQoSModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: h3cQoSModuleIndex.setStatus('current')
h3cQoSCharacteristicsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: h3cQoSCharacteristicsIndex.setStatus('current')
h3cQoSCharacteristicsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 7, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSCharacteristicsValue.setStatus('current')
mibBuilder.exportSymbols("H3C-QOS-CAPABILITY-MIB", PYSNMP_MODULE_ID=h3cQosCapability, h3cQoSCharacteristicsValue=h3cQoSCharacteristicsValue, h3cQoSCapabilityMibObjects=h3cQoSCapabilityMibObjects, h3cQoSCapabilityTable=h3cQoSCapabilityTable, h3cQoSCapabilityEntry=h3cQoSCapabilityEntry, h3cQoSCapabilityPhysicalType=h3cQoSCapabilityPhysicalType, h3cQoSCapabilityPhysicalIndex=h3cQoSCapabilityPhysicalIndex, h3cQoSModuleIndex=h3cQoSModuleIndex, h3cQoSCharacteristicsIndex=h3cQoSCharacteristicsIndex, h3cQoSCapabilityGroup=h3cQoSCapabilityGroup, h3cQosCapability=h3cQosCapability, CapabilityPhysicalType=CapabilityPhysicalType)
