#
# PySNMP MIB module CISCO-BULK-FILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BULK-FILE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Bits, IpAddress, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, ModuleIdentity, Counter32, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Bits", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBulkFileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 188))
ciscoBulkFileCapability.setRevisions(('2006-02-06 00:00', '2003-11-13 00:00', '2002-02-17 00:00', '2000-12-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBulkFileCapability.setRevisionsDescriptions(('Added ciscoBulkFileCapCRS1V2R0 Agent Capabilities for IOS XR 2.0', 'Added VXSM 5.0.0 PRODUCT-RELEASE of ciscoBulkFileCapabilityV3R00', 'Added following capabilities for MGX8850/SES Products: - ciscoBulkFileCapabilityV2R00 - ciscoBulkFileCapabilityV3R00.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBulkFileCapability.setLastUpdated('200602060000Z')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setDescription('Agent capabilities for CISCO-BULK-FILE-MIB')
ciscoBulkFileCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setProductRelease('Cisco IOS mc 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV1R0.setDescription('Cisco Bulk File MIB capabilities')
ciscoBulkFileCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                          BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV2R00.setDescription('CISCO-BULK-FILE-MIB Capabilities.')
ciscoBulkFileCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,\n                          BPX SES Release 3.00,\n                          VXSM  Release 5.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV3R00.setDescription('CISCO-BULK-FILE-MIB Capabilities.')
ciscoBulkFileCapCRS1V2R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapCRS1V2R0.setDescription('CISCO-BULK-FILE-MIB Capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-BULK-FILE-CAPABILITY", ciscoBulkFileCapabilityV2R00=ciscoBulkFileCapabilityV2R00, ciscoBulkFileCapCRS1V2R0=ciscoBulkFileCapCRS1V2R0, ciscoBulkFileCapabilityV3R00=ciscoBulkFileCapabilityV3R00, ciscoBulkFileCapabilityV1R0=ciscoBulkFileCapabilityV1R0, PYSNMP_MODULE_ID=ciscoBulkFileCapability, ciscoBulkFileCapability=ciscoBulkFileCapability)
