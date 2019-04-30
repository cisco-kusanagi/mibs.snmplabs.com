#
# PySNMP MIB module HH3C-QOS-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-QOS-CAPABILITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hh3cSNMPAgCpb, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cSNMPAgCpb")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Gauge32, ObjectIdentity, Integer32, Counter32, Unsigned32, MibIdentifier, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Gauge32", "ObjectIdentity", "Integer32", "Counter32", "Unsigned32", "MibIdentifier", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 7, 1))
if mibBuilder.loadTexts: hh3cQosCapability.setLastUpdated('200508300000Z')
if mibBuilder.loadTexts: hh3cQosCapability.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cQoSCapabilityMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1))
class CapabilityPhysicalType(TextualConvention, Integer32):
    reference = 'rfc2737 ENTITY-MIB '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("stack", 1), ("chassis", 2), ("module", 3), ("port", 4))

hh3cQoSCapabilityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1))
hh3cQoSCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cQoSCapabilityTable.setStatus('current')
hh3cQoSCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalType"), (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalIndex"), (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSModuleIndex"), (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCharacteristicsIndex"))
if mibBuilder.loadTexts: hh3cQoSCapabilityEntry.setStatus('current')
hh3cQoSCapabilityPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 1), CapabilityPhysicalType())
if mibBuilder.loadTexts: hh3cQoSCapabilityPhysicalType.setStatus('current')
hh3cQoSCapabilityPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: hh3cQoSCapabilityPhysicalIndex.setStatus('current')
hh3cQoSModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: hh3cQoSModuleIndex.setStatus('current')
hh3cQoSCharacteristicsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: hh3cQoSCharacteristicsIndex.setStatus('current')
hh3cQoSCharacteristicsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cQoSCharacteristicsValue.setStatus('current')
mibBuilder.exportSymbols("HH3C-QOS-CAPABILITY-MIB", hh3cQoSCharacteristicsValue=hh3cQoSCharacteristicsValue, hh3cQoSCharacteristicsIndex=hh3cQoSCharacteristicsIndex, hh3cQoSCapabilityMibObjects=hh3cQoSCapabilityMibObjects, hh3cQoSCapabilityEntry=hh3cQoSCapabilityEntry, PYSNMP_MODULE_ID=hh3cQosCapability, CapabilityPhysicalType=CapabilityPhysicalType, hh3cQoSCapabilityTable=hh3cQoSCapabilityTable, hh3cQoSCapabilityPhysicalType=hh3cQoSCapabilityPhysicalType, hh3cQosCapability=hh3cQosCapability, hh3cQoSModuleIndex=hh3cQoSModuleIndex, hh3cQoSCapabilityPhysicalIndex=hh3cQoSCapabilityPhysicalIndex, hh3cQoSCapabilityGroup=hh3cQoSCapabilityGroup)
