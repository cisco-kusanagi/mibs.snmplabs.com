#
# PySNMP MIB module CISCO-SONET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SONET-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, ModuleIdentity, iso, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Counter32, IpAddress, Counter64, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "Counter64", "Gauge32", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSonetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 261))
ciscoSonetExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-13 00:00', '2002-02-17 00:00',))
if mibBuilder.loadTexts: ciscoSonetExtCapability.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSonetExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setStatus('current')
ciscoSonetExtAxsmCapabilityV2R11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setProductRelease('MGX8850 Release 2.0.11')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setStatus('current')
ciscoSonetExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setStatus('current')
ciscoSonetExtSrmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setProductRelease('MGX8800 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setStatus('current')
ciscoSonetExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setProductRelease('MGX8850, MGX8950 Release 4.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setStatus('current')
ciscoSonetExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-SONET-EXT-CAPABILITY", ciscoSonetExtSrmeCapabilityV3R00=ciscoSonetExtSrmeCapabilityV3R00, ciscoSonetExtCapabilityV5R00=ciscoSonetExtCapabilityV5R00, ciscoSonetExtAxsmeCapabilityV21R60=ciscoSonetExtAxsmeCapabilityV21R60, ciscoSonetExtAxsmCapabilityV2R11=ciscoSonetExtAxsmCapabilityV2R11, ciscoSonetExtCapabilityV4R00=ciscoSonetExtCapabilityV4R00, ciscoSonetExtCapability=ciscoSonetExtCapability, PYSNMP_MODULE_ID=ciscoSonetExtCapability, ciscoSonetExtAxsmCapabilityV2R00=ciscoSonetExtAxsmCapabilityV2R00)
