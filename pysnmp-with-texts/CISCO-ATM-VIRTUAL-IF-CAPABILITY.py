#
# PySNMP MIB module CISCO-ATM-VIRTUAL-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-VIRTUAL-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, iso, Gauge32, TimeTicks, IpAddress, Integer32, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "iso", "Gauge32", "TimeTicks", "IpAddress", "Integer32", "Counter32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmVirtualIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 279))
ciscoAtmVirtualIfCapability.setRevisions(('2005-11-14 00:00', '2003-09-10 00:00', '2003-03-24 00:00', '2002-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setRevisionsDescriptions(('Updated the imports such that Unsigned32 is imported from SNMPv2-SMI instead of CISCO-TC.', 'Added cavIfCapabilityV5R00 for MPSM155 service module in Release 5.0.00', 'Added cavIfCapabilityV4R00 for : Service Modules AXSM-XG, AXSM-E and Processor Switch Module PXM1E in Release 4.0.00', 'Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setDescription('The Agent Capabilities for CISCO-ATM-VIRTUAL-IF-MIB. - cavIfCapmVirtualIfCapabilityV2R00 is for AXSM module in Release 2.0. - cavIfCapabilityAxsmV2R0010 is for AXSM Service Module in Release 2.0.10. - cavIfCapabilityAxsmeV2R0160 is for AXSM-E Service Module in Release 2.1.60.')
cavIfCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmV2R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for AXSM Service Module.')
cavIfCapabilityAxsmV2R0010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setProductRelease('MGX8850 Release 2.0.10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmV2R0010.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for AXSM Service Module.')
cavIfCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityAxsmeV2R0160.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for Enhanced AXSM (AXSM-E)module.')
cavIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityV4R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for 10 Gig. AXSM module (AXSM-XG), Enhanced AXSM module (AXSM-E) and Processor Switch Module Enhanced(PXM1E) controller card.')
cavIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setProductRelease('MGX8950, MGX8850 Release 5.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: cavIfCapabilityV5R00.setDescription('CISCO-ATM-VIRTUAL-IF-MIB Capabilities for MPSM155 service module.')
mibBuilder.exportSymbols("CISCO-ATM-VIRTUAL-IF-CAPABILITY", cavIfCapabilityV5R00=cavIfCapabilityV5R00, cavIfCapabilityAxsmV2R0010=cavIfCapabilityAxsmV2R0010, ciscoAtmVirtualIfCapability=ciscoAtmVirtualIfCapability, cavIfCapabilityAxsmeV2R0160=cavIfCapabilityAxsmeV2R0160, cavIfCapabilityV4R00=cavIfCapabilityV4R00, cavIfCapabilityAxsmV2R00=cavIfCapabilityAxsmV2R00, PYSNMP_MODULE_ID=ciscoAtmVirtualIfCapability)
