#
# PySNMP MIB module CISCO-DS1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS1-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, TimeTicks, Counter64, IpAddress, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "IpAddress", "MibIdentifier", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 273))
ciscoDs1Capability.setRevisions(('2007-10-31 00:00', '2007-09-10 00:00', '2007-05-11 00:00', '2006-06-16 00:00', '2005-07-11 00:00', '2003-12-22 00:00', '2002-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs1Capability.setRevisionsDescriptions(('Added VARIATION for dsx1LineStatusChangeTrapEnable to agent capability statement ciscoDs1CapabilityMARsV12R5T and ciscoDs1CapabilityAS5xxxV12R5T', 'Added ciscoDs1CapabilityV5R500 for defining capability for VXSM support in MGX8880 release 5.5.0.', 'Added ciscoDs1CapabilityMARsV12R5T for 2800, 3800, 3700 series routers and IAD2430 platforms. Added ciscoDs1CapabilityAS5xxxV12R5T for AS5xxx platforms.', 'Added ciscoDs1CapabilityV5R310 for VXSM support in MGX8880 release 5.3.1.', 'Added ciscoDs1CapabilityV5R100 for MPSM and VXSM support in MGX8880 release 5.1.0.', 'ciscoDs1CapabilityV5R00 added for MPSM and VXSM support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDs1Capability.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: ciscoDs1Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs1Capability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs1Capability.setDescription('The agent capabilities for DS1-MIB for Cisco Products Series. - ciscoDs1AxsmeCapabilityV3R00 is for Enhanced ATM Switch Service Module(AXSM-E), and Enhanced Processor Switch Module 1(PXM1E) uplink. - ciscoDs1CapabilityV5R00 is for Voice Switch Service Module(VXSM) and MPSM Module Release 5.0.0.')
ciscoDs1AxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1AxsmeCapabilityV3R00.setDescription('DS1-MIB Capabilities.')
ciscoDs1CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R00.setDescription('DS1 MIB capabilities for VXSM and MPSM in release 5.0.0')
ciscoDs1CapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setProductRelease('MGX8880 Release 5.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R100.setDescription('DS1 MIB capabilities for VXSM and MPSM in release 5.1.0')
ciscoDs1CapabilityV5R310 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setProductRelease('MGX8880 Release 5.3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R310.setDescription('DS1 MIB capabilities for VXSM in release 5.3.1')
ciscoDs1CapabilityMARsV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setProductRelease('IOS 12.5T for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityMARsV12R5T.setDescription('Agent capabilities for Cisco 3700 series routers, IAD2430 and 2800, 3800 Series Integrated Services Routers.')
ciscoDs1CapabilityAS5xxxV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setProductRelease('IOS 12.5T for Cisco Access Servers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityAS5xxxV12R5T.setDescription('Agent capabilities for Cisco AS5xxx routers.')
ciscoDs1CapabilityV5R500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setProductRelease('MGX8880 Release 5.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R500.setDescription('DS1 MIB capabilities for VXSM in release 5.5.0.')
mibBuilder.exportSymbols("CISCO-DS1-CAPABILITY", ciscoDs1CapabilityMARsV12R5T=ciscoDs1CapabilityMARsV12R5T, PYSNMP_MODULE_ID=ciscoDs1Capability, ciscoDs1CapabilityV5R500=ciscoDs1CapabilityV5R500, ciscoDs1Capability=ciscoDs1Capability, ciscoDs1CapabilityV5R100=ciscoDs1CapabilityV5R100, ciscoDs1CapabilityV5R00=ciscoDs1CapabilityV5R00, ciscoDs1AxsmeCapabilityV3R00=ciscoDs1AxsmeCapabilityV3R00, ciscoDs1CapabilityAS5xxxV12R5T=ciscoDs1CapabilityAS5xxxV12R5T, ciscoDs1CapabilityV5R310=ciscoDs1CapabilityV5R310)
