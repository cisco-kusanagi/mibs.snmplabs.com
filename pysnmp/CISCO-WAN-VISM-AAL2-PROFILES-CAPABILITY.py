#
# PySNMP MIB module CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, Counter32, Counter64, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Counter64", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismAal2ProfilesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 334))
ciscoWanVismAal2ProfilesCapability.setRevisions(('2000-12-18 00:00',))
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setLastUpdated('200012180000Z')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanVismAal2ProfilesCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 334, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY", ciscoWanVismAal2ProfilesCapability=ciscoWanVismAal2ProfilesCapability, ciscoWanVismAal2ProfilesCapabilityV2R00=ciscoWanVismAal2ProfilesCapabilityV2R00, PYSNMP_MODULE_ID=ciscoWanVismAal2ProfilesCapability)
