#
# PySNMP MIB module CISCO-DS3-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS3-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, TimeTicks, ObjectIdentity, NotificationType, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, Integer32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDs3ExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 262))
ciscoDs3ExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-20 00:00', '2002-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs3ExtCapability.setRevisionsDescriptions(('Added ciscoDs3Ext155CapabilityV5R00.', 'Added ciscoDs3ExtCapabilityV4R00 for 10 Gig. AXSM Module (AXSM-XG) and Processor Switch Module Enhanced(PXM1E) controller card.', 'Initial version of the MIB Module.',))
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setLastUpdated('200312230000Z')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setDescription('The Agent Capabilities for CISCO-DS3-MIB. - The ciscoDs3ExtAxsmCapabilityV2R00 is for ATM Switch Service Module(AXSM). - The ciscoDs3ExtAxsmeCapabilityV21R60 is for Enhanced AXSM(AXSM-E) Module. - The ciscoDs3ExtSrmCapabilityV3R00 is for Service Resource Module(SRM). - The ciscoDs3ExtFrsm12CapabilityV3R00 is for Frame Relay Service Module(FRSM-12). - The ciscoDs3ExtAxsmxgCapabilityV4R00 is for 10 Gig. AXSM Module (AXSM-XG). - The ciscoDs3ExtCapabilityV5R00 is for Voice Switch Service (VXSM) and MPSM Modules.')
ciscoDs3ExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtAxsmCapabilityV2R00.setDescription('CISCO-DS3-MIB Capabilities for ATM Switch Service Module(AXSM).')
ciscoDs3ExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtAxsmeCapabilityV21R60.setDescription('CISCO-DS3-MIB Capabilities for Enhanced AXSM Module(AXSM-E).')
ciscoDs3ExtSrmCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtSrmCapabilityV3R00.setDescription('CISCO-DS3-MIB Capabilities for Service Resource Module(SRM).')
ciscoDs3ExtFrsm12CapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtFrsm12CapabilityV3R00.setDescription('CISCO-DS3-MIB Capabilities for Frame Relay Service Module(FRSM-12).')
ciscoDs3ExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release \n                         4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtCapabilityV4R00.setDescription('CISCO-DS3-MIB Capabilities for 10 Gig. AXSM Module(AXSM-XG) and Processor Switch Module Enhanced- (PXM1E) controller card.')
ciscoDs3ExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtCapabilityV5R00.setDescription('CISCO-DS3-MIB capabilities Voice Switch Service Module(VXSM) and MPSM in release 5.0.0')
mibBuilder.exportSymbols("CISCO-DS3-EXT-CAPABILITY", ciscoDs3ExtCapabilityV5R00=ciscoDs3ExtCapabilityV5R00, PYSNMP_MODULE_ID=ciscoDs3ExtCapability, ciscoDs3ExtCapabilityV4R00=ciscoDs3ExtCapabilityV4R00, ciscoDs3ExtSrmCapabilityV3R00=ciscoDs3ExtSrmCapabilityV3R00, ciscoDs3ExtAxsmeCapabilityV21R60=ciscoDs3ExtAxsmeCapabilityV21R60, ciscoDs3ExtCapability=ciscoDs3ExtCapability, ciscoDs3ExtFrsm12CapabilityV3R00=ciscoDs3ExtFrsm12CapabilityV3R00, ciscoDs3ExtAxsmCapabilityV2R00=ciscoDs3ExtAxsmCapabilityV2R00)
