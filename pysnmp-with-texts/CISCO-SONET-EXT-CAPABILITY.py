#
# PySNMP MIB module CISCO-SONET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SONET-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, NotificationType, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Gauge32, TimeTicks, iso, MibIdentifier, ModuleIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Gauge32", "TimeTicks", "iso", "MibIdentifier", "ModuleIdentity", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSonetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 261))
ciscoSonetExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-13 00:00', '2002-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSonetExtCapability.setRevisionsDescriptions(('Added ciscoSonetExtCapabilityV5R00.', 'Added ciscoSonetExtCapabilityV4R00 for modules: ATM Switch Service Module(AXSM), 10 Gig. ATM Switch Service Module(AXSM-XG), Enhanced ATM Switch Service Module(AXSM-E) and Processor Switch Module Enhanced (PXM1E).', 'Initial Version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSonetExtCapability.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setDescription('The Agent Capabilities for CISCO-SONET-MIB. - ciscoSonetExtAxsmCapabilityV2R00 is for ATM Switch Service Module(AXSM). - ciscoSonetExtAxsmCapabilityV2R11 is for ATM Switch Service Module(AXSM). - ciscoSonetExtAxsmeCapabilityV21R60 is for Enhanced ATM Switch Service Module(AXSM-E). - ciscoSonetExtCapabilityV5R000 is for Service Resource Module(SRM-E). - ciscoSonetExtSrmeCapabilityV3R00 is for Voice Switch Service Module(VXSM) - ciscoSonetExtSrmeCapabilityV3R00 is for Service Resource Module(SRM-E). - ciscoSonetExtCapabilityV4R00 is for 10 Gig. ATM Switch Service Module(AXSM-XG) and Enhanced ATM Switch Service Module(AXSM-E). - ciscoSonetExtCapabilityV5R000 is for Voice Switch Service Module(VXSM) and MPSM.')
ciscoSonetExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmCapabilityV2R00.setDescription('CISCO-SONET-MIB Capabilities for ATM Switch Service Module(AXSM).')
ciscoSonetExtAxsmCapabilityV2R11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setProductRelease('MGX8850 Release 2.0.11')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmCapabilityV2R11.setDescription('CISCO-SONET-MIB Capabilities for ATM Switch Service Module(AXSM).')
ciscoSonetExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmeCapabilityV21R60.setDescription('CISCO-SONET-MIB Capabilities for AXSM-E Service Modules.')
ciscoSonetExtSrmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setProductRelease('MGX8800 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtSrmeCapabilityV3R00.setDescription('CISCO-SONET-MIB Capabilities of Enhanced Service Resource Module(SRM-E).')
ciscoSonetExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setProductRelease('MGX8850, MGX8950 Release 4.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtCapabilityV4R00.setDescription('CISCO-SONET-MIB Capabilities for AXSM, AXSM-E, AXSM-XG and PXM1E Modules.')
ciscoSonetExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtCapabilityV5R00.setDescription('Cisco Sonet Ext MIB capabilities for Voice Switch Service Module(VXSM) and MPSM in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-SONET-EXT-CAPABILITY", ciscoSonetExtAxsmCapabilityV2R11=ciscoSonetExtAxsmCapabilityV2R11, ciscoSonetExtCapabilityV4R00=ciscoSonetExtCapabilityV4R00, ciscoSonetExtSrmeCapabilityV3R00=ciscoSonetExtSrmeCapabilityV3R00, ciscoSonetExtAxsmeCapabilityV21R60=ciscoSonetExtAxsmeCapabilityV21R60, ciscoSonetExtCapabilityV5R00=ciscoSonetExtCapabilityV5R00, PYSNMP_MODULE_ID=ciscoSonetExtCapability, ciscoSonetExtAxsmCapabilityV2R00=ciscoSonetExtAxsmCapabilityV2R00, ciscoSonetExtCapability=ciscoSonetExtCapability)
