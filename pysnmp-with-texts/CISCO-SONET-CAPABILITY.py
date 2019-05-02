#
# PySNMP MIB module CISCO-SONET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SONET-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, iso, Counter32, Integer32, NotificationType, ObjectIdentity, Bits, Gauge32, Counter64, Unsigned32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter32", "Integer32", "NotificationType", "ObjectIdentity", "Bits", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSonetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 266))
ciscoSonetCapability.setRevisions(('2004-02-19 00:00', '2003-03-11 00:00', '2002-03-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSonetCapability.setRevisionsDescriptions(('Added ciscoSonetCapabilityV5R00.', 'Added ciscoSonetCapabilityV4R00 for modules: 10 Gig. ATM Switch Service Module(AXSM-XG), AXSM Service Module Enhanced(AXSM-E) and Processor Switch Module Enhanced(PXM1E) controller card.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSonetCapability.setLastUpdated('200402190000Z')
if mibBuilder.loadTexts: ciscoSonetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSonetCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSonetCapability.setDescription('Agent capabilities for SONET-MIB(RFC 2558). ciscoSonetCapabilityAxsmV2R01 for AXSM module. ciscoSonetCapabilitySrmeV3R00 for SRME module. ciscoSonetCapabilityAxsmxgV4R00 for AXSM-XG module. ciscoSonetCapabilityV5R00 for VXSM, SRME and MPSM module.')
ciscoSonetCapabilityAxsmV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityAxsmV2R0100.setDescription('Sonet MIB Capabilities for Following Service Modules: ATM Switch Service Module(AXSM) AXSM Enhanced(AXSM-E).')
ciscoSonetCapabilitySrmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilitySrmeV3R00.setDescription('Sonet MIB Capabilities for Service Resource Module Enhanced(SRME) module.')
ciscoSonetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setProductRelease('MGX8950  and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityV4R00.setDescription('Sonet MIB Capabilities for Service Module: 10 Gig. ATM Switch Service Module(AXSM-XG), AXSM Service Module Enhanced(AXSM-E) and Processor Switch Module Enhanced(PXM1E) controller card.')
ciscoSonetCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityV5R00.setDescription('Sonet MIB capabilities for Voice Switch Service Module(VXSM), SRME and MPSM in release 5.0.0')
mibBuilder.exportSymbols("CISCO-SONET-CAPABILITY", ciscoSonetCapabilityV5R00=ciscoSonetCapabilityV5R00, ciscoSonetCapabilityV4R00=ciscoSonetCapabilityV4R00, ciscoSonetCapabilityAxsmV2R0100=ciscoSonetCapabilityAxsmV2R0100, ciscoSonetCapabilitySrmeV3R00=ciscoSonetCapabilitySrmeV3R00, PYSNMP_MODULE_ID=ciscoSonetCapability, ciscoSonetCapability=ciscoSonetCapability)
