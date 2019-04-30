#
# PySNMP MIB module CISCO-ATM-CELL-LAYER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-CELL-LAYER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, Unsigned32, iso, TimeTicks, Counter32, Counter64, Bits, ModuleIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "iso", "TimeTicks", "Counter32", "Counter64", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAtmCellLayerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 275))
ciscoAtmCellLayerCapability.setRevisions(('2003-01-30 00:00', '2002-05-14 00:00',))
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setLastUpdated('200301300000Z')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setOrganization('Cisco Systems, Inc.')
cacLayerCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setStatus('current')
cacLayerCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setStatus('current')
cacLayerCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-CELL-LAYER-CAPABILITY", cacLayerCapabilityAxsmeV2R0160=cacLayerCapabilityAxsmeV2R0160, cacLayerCapabilityAxsmxgV4R00=cacLayerCapabilityAxsmxgV4R00, cacLayerCapabilityAxsmV2R00=cacLayerCapabilityAxsmV2R00, PYSNMP_MODULE_ID=ciscoAtmCellLayerCapability, ciscoAtmCellLayerCapability=ciscoAtmCellLayerCapability)
