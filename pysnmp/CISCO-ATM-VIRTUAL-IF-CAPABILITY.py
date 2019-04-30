#
# PySNMP MIB module CISCO-ATM-VIRTUAL-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-VIRTUAL-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter32, NotificationType, TimeTicks, Gauge32, Unsigned32, Counter64, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "Counter64", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmVirtualIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 279))
ciscoAtmVirtualIfCapability.setRevisions(('2005-11-14 00:00', '2003-09-10 00:00', '2003-03-24 00:00', '2002-05-14 00:00',))
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setOrganization('Cisco Systems, Inc.')
cavIfCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setStatus('current')
cavIfCapabilityAxsmV2R0010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setProductRelease('MGX8850 Release 2.0.10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setStatus('current')
cavIfCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setStatus('current')
cavIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setStatus('current')
cavIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setProductRelease('MGX8950, MGX8850 Release 5.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-VIRTUAL-IF-CAPABILITY", cavIfCapabilityV5R00=cavIfCapabilityV5R00, cavIfCapabilityAxsmeV2R0160=cavIfCapabilityAxsmeV2R0160, cavIfCapabilityAxsmV2R00=cavIfCapabilityAxsmV2R00, ciscoAtmVirtualIfCapability=ciscoAtmVirtualIfCapability, PYSNMP_MODULE_ID=ciscoAtmVirtualIfCapability, cavIfCapabilityAxsmV2R0010=cavIfCapabilityAxsmV2R0010, cavIfCapabilityV4R00=cavIfCapabilityV4R00)
