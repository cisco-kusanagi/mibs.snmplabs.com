#
# PySNMP MIB module CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, Counter32, Bits, ObjectIdentity, Integer32, NotificationType, iso, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter32", "Bits", "ObjectIdentity", "Integer32", "NotificationType", "iso", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismAal2ProfilesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 334))
ciscoWanVismAal2ProfilesCapability.setRevisions(('2000-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setLastUpdated('200012180000Z')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setDescription('The Agent Capabilities for CISCO-WAN-AAL2-PROFILES-MIB.')
ciscoWanVismAal2ProfilesCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 334, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapabilityV2R00.setDescription('CISCO-WAN-AAL2-PROFILES-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY", ciscoWanVismAal2ProfilesCapabilityV2R00=ciscoWanVismAal2ProfilesCapabilityV2R00, PYSNMP_MODULE_ID=ciscoWanVismAal2ProfilesCapability, ciscoWanVismAal2ProfilesCapability=ciscoWanVismAal2ProfilesCapability)
