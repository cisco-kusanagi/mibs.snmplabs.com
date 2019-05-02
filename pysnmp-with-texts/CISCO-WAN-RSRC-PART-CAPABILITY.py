#
# PySNMP MIB module CISCO-WAN-RSRC-PART-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-RSRC-PART-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:20:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, ModuleIdentity, ObjectIdentity, iso, MibIdentifier, IpAddress, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "iso", "MibIdentifier", "IpAddress", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanRsrcPartCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 260))
ciscoWanRsrcPartCapability.setRevisions(('2005-04-26 00:00', '2004-09-29 00:00', '2003-11-13 00:00', '2002-11-11 00:00', '2002-03-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setRevisionsDescriptions(('Added the agent capabilities cwRsrcPartCapabilityAxsmeV2R00, cwRsrcPartCapabilityAxsmeV4R00 & cwRsrcPartCapabilityAxsmeV5R00 for AXSME to add the variations for OIDs cwRsrcPartVciLo, cwRsrcPartVciHigh & cwRsrcPartMaxCon.', 'Updated cwRsrcPartCapabilityV5R00,cwRsrcPartCapabilityV4R00 and cwRsrcPartCapabilityV2R00 with variations for the OIDs cwRsrcPartEgrPctBwUsed,cwRsrcPartIngPctBwUsed, cwRsrcPartEgrPctBwAvail and cwRsrcPartIngPctBwAvail for AXSM,AXSME,AXSM-XG and PXM1E service modules.', 'Added the capability cwRsrcPartCapabilityV5R00 for MGX8850 Release 5.0.0', 'Added ciscoWanRsrcPartCapability(4) for version 4.0.0 for AXSM, AXSME, AXSM-XG and PXM1E service modules.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setLastUpdated('200504260000Z')
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setDescription('The Agent Capabilities for CISCO-WAN-RSRC-PART-MIB.')
cwRsrcPartCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityV2R00.setDescription('CISCO-WAN-RSRC-PART-MIB Capabilities for ATM Switch Service Module(AXSM).')
cwRsrcPartCapabilityRpmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityRpmV2R0160.setDescription('Agent Capabilities for CISCO-WAN-RSRC-PART-MIB for RPM-PR Module.')
cwRsrcPartCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2.\n                          MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityRpmxfV12R02.setDescription('Agent Capabilities for CISCO-WAN-RSRC-PART-MIB for RPM-XF Module.')
cwRsrcPartCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityV4R00.setDescription('CISCO-WAN-RSRC-PART-MIB Capabilities for ATM Switch Service Module(AXSM), AXSM-XG and PXM1E')
cwRsrcPartCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityV5R00.setDescription('Agent capabilities for VXSM module in Release 5.0.0.')
cwRsrcPartCapabilityAxsmeV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityAxsmeV2R00.setDescription('CISCO-WAN-RSRC-PART-MIB Capabilities for Enhanced AXSM(AXSM-E).')
cwRsrcPartCapabilityAxsmeV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityAxsmeV4R00.setDescription('CISCO-WAN-RSRC-PART-MIB Capabilities for Enhanced AXSM(AXSM-E)')
cwRsrcPartCapabilityAxsmeV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setProductRelease('MGX8850 Release 5.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setStatus('current')
if mibBuilder.loadTexts: cwRsrcPartCapabilityAxsmeV5R00.setDescription('CISCO-WAN-RSRC-PART-MIB Capabilities for Enhanced AXSM(AXSM-E).')
mibBuilder.exportSymbols("CISCO-WAN-RSRC-PART-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanRsrcPartCapability, cwRsrcPartCapabilityRpmV2R0160=cwRsrcPartCapabilityRpmV2R0160, cwRsrcPartCapabilityRpmxfV12R02=cwRsrcPartCapabilityRpmxfV12R02, cwRsrcPartCapabilityV2R00=cwRsrcPartCapabilityV2R00, cwRsrcPartCapabilityAxsmeV5R00=cwRsrcPartCapabilityAxsmeV5R00, cwRsrcPartCapabilityV4R00=cwRsrcPartCapabilityV4R00, cwRsrcPartCapabilityAxsmeV4R00=cwRsrcPartCapabilityAxsmeV4R00, ciscoWanRsrcPartCapability=ciscoWanRsrcPartCapability, cwRsrcPartCapabilityAxsmeV2R00=cwRsrcPartCapabilityAxsmeV2R00, cwRsrcPartCapabilityV5R00=cwRsrcPartCapabilityV5R00)
