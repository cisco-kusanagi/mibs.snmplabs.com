#
# PySNMP MIB module A3COM-HUAWEI-QOS-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-QOS-CAPABILITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cSNMPAgCpb, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cSNMPAgCpb")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, MibIdentifier, Gauge32, NotificationType, Integer32, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1))
if mibBuilder.loadTexts: h3cQosCapability.setLastUpdated('200508300000Z')
if mibBuilder.loadTexts: h3cQosCapability.setOrganization('Huawei 3Com Technologies Co.,Ltd.')
h3cQoSCapabilityMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1))
class CapabilityPhysicalType(TextualConvention, Integer32):
    reference = 'rfc2737 ENTITY-MIB '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("stack", 1), ("chassis", 2), ("module", 3), ("port", 4))

h3cQoSCapabilityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1))
h3cQoSCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1), )
if mibBuilder.loadTexts: h3cQoSCapabilityTable.setStatus('current')
h3cQoSCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalType"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalIndex"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSModuleIndex"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCharacteristicsIndex"))
if mibBuilder.loadTexts: h3cQoSCapabilityEntry.setStatus('current')
h3cQoSCapabilityPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 1), CapabilityPhysicalType())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalType.setStatus('current')
h3cQoSCapabilityPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalIndex.setStatus('current')
h3cQoSModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: h3cQoSModuleIndex.setStatus('current')
h3cQoSCharacteristicsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: h3cQoSCharacteristicsIndex.setStatus('current')
h3cQoSCharacteristicsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSCharacteristicsValue.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-QOS-CAPABILITY-MIB", h3cQoSCapabilityGroup=h3cQoSCapabilityGroup, h3cQoSCapabilityPhysicalIndex=h3cQoSCapabilityPhysicalIndex, h3cQosCapability=h3cQosCapability, PYSNMP_MODULE_ID=h3cQosCapability, h3cQoSCharacteristicsIndex=h3cQoSCharacteristicsIndex, h3cQoSCapabilityMibObjects=h3cQoSCapabilityMibObjects, h3cQoSCharacteristicsValue=h3cQoSCharacteristicsValue, CapabilityPhysicalType=CapabilityPhysicalType, h3cQoSCapabilityEntry=h3cQoSCapabilityEntry, h3cQoSCapabilityPhysicalType=h3cQoSCapabilityPhysicalType, h3cQoSCapabilityTable=h3cQoSCapabilityTable, h3cQoSModuleIndex=h3cQoSModuleIndex)
