#
# PySNMP MIB module CISCO-ATM-CELL-LAYER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-CELL-LAYER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:50:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Counter64, Bits, Gauge32, ModuleIdentity, iso, IpAddress, MibIdentifier, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "iso", "IpAddress", "MibIdentifier", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAtmCellLayerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 275))
ciscoAtmCellLayerCapability.setRevisions(('2003-01-30 00:00', '2002-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setRevisionsDescriptions(('Added cacLayerCapabilityAxsmxgV4R00.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setLastUpdated('200301300000Z')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setDescription('The Agent Capabilities for CISCO-ATM-CELL-LAYER-MIB. - cacLayerCapabilityAxsmV2R00 is for ATM Switch Service Module(AXSM). - cacLayerCapabilityAxsmeV2R0160 is for Enhanced AXSM(AXSM-E). - cacLayerCapabilityAxsmxgV4R00 is for 10 Gig. AXSM(AXSM-XG).')
cacLayerCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmV2R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for AXSM Service Module.')
cacLayerCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmeV2R0160.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for Enhanced AXSM(AXSM-E) Service Module.')
cacLayerCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmxgV4R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for 10 Gig. AXSM Service Module (AXSM-XG).')
mibBuilder.exportSymbols("CISCO-ATM-CELL-LAYER-CAPABILITY", ciscoAtmCellLayerCapability=ciscoAtmCellLayerCapability, cacLayerCapabilityAxsmeV2R0160=cacLayerCapabilityAxsmeV2R0160, PYSNMP_MODULE_ID=ciscoAtmCellLayerCapability, cacLayerCapabilityAxsmV2R00=cacLayerCapabilityAxsmV2R00, cacLayerCapabilityAxsmxgV4R00=cacLayerCapabilityAxsmxgV4R00)
