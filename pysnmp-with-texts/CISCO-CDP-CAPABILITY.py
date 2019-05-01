#
# PySNMP MIB module CISCO-CDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:52:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, TimeTicks, ModuleIdentity, Counter32, Bits, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity", "Counter32", "Bits", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 43))
ciscoCdpCapability.setRevisions(('2007-07-18 00:00', '2006-10-26 00:00', '2006-02-06 00:00', '2005-05-24 00:00', '2003-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdpCapability.setRevisionsDescriptions(('Added capability statement ciscoCdpCapV12R0233SXHPCat6K.', 'Added capability for Cisco TelePresence System (CTS) and Cisco TelePresence Manager (CTM) platforms.', 'Added capability for IOS-XR 2.0 CRS-1.', 'Added capability for MDS platform.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdpCapability.setLastUpdated('200707180000Z')
if mibBuilder.loadTexts: ciscoCdpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCdpCapability.setDescription('The capabilities description of CISCO-CDP-MIB.')
ciscoCdpCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0111bEXCat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0217SXCat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCatOSV08R0101Cat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCatOSV08R0101Cat4K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapSanOSV03R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setProductRelease('Cisco SAN-OS 3.0(1) on MDS platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapSanOSV03R0001.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapIOSXRV2R0CRS1.setDescription('CISCO-CDP-MIB capabilities for IOS XR release 2.0')
ciscoCdpCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCTSV100.setDescription('CISCO-CDP-MIB capabilities for CTS 1.0.0')
ciscoCdpCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCTMV1000.setDescription('CISCO-CDP-MIB capabilities for CTM 1.0.0.0')
ciscoCdpCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0233SXHPCat6K.setDescription('CISCO-CDP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CDP-CAPABILITY", ciscoCdpCapCatOSV08R0101Cat4K=ciscoCdpCapCatOSV08R0101Cat4K, ciscoCdpCapIOSXRV2R0CRS1=ciscoCdpCapIOSXRV2R0CRS1, ciscoCdpCapCTMV1000=ciscoCdpCapCTMV1000, ciscoCdpCapCatOSV08R0101Cat6K=ciscoCdpCapCatOSV08R0101Cat6K, ciscoCdpCapV12R0217SXCat6K=ciscoCdpCapV12R0217SXCat6K, ciscoCdpCapability=ciscoCdpCapability, ciscoCdpCapV12R0111bEXCat6K=ciscoCdpCapV12R0111bEXCat6K, PYSNMP_MODULE_ID=ciscoCdpCapability, ciscoCdpCapSanOSV03R0001=ciscoCdpCapSanOSV03R0001, ciscoCdpCapCTSV100=ciscoCdpCapCTSV100, ciscoCdpCapV12R0233SXHPCat6K=ciscoCdpCapV12R0233SXHPCat6K)
