#
# PySNMP MIB module CISCO-VTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VTP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibIdentifier, ModuleIdentity, iso, TimeTicks, Gauge32, Integer32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ModuleIdentity", "iso", "TimeTicks", "Gauge32", "Integer32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "NotificationType", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 329))
ciscoVtpCapability.setRevisions(('2013-09-27 00:00', '2013-08-27 00:00', '2011-09-30 00:00', '2011-07-31 00:00', '2011-04-06 00:00', '2011-03-30 00:00', '2010-11-10 00:00', '2010-03-22 00:00', '2010-03-10 00:00', '2008-10-28 00:00', '2008-05-28 00:00', '2007-07-18 00:00', '2006-03-15 00:00', '2005-03-09 00:00', '2004-04-15 00:00', '2003-12-01 00:00', '2003-09-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVtpCapability.setRevisionsDescriptions(('Added capability statement ciscoVtpCapV15R0102SYPCat6k.', 'Added capability statement ciscoVtpCapNxOSV06R0101PN7K.', 'Added capability statement ciscoVtpCapV15R0001SYPCat6kSup2T.', 'Added capability statement ciscoVtpCapNxOSV05R0201PN7K.', 'Added capability statement ciscoVtpCapNxOSV05R0002PN5k.', 'Added capability statement ciscoVtpCapV12R0233SXJPCat6k.', 'Added capability statement ciscoVtpCapNxOSV05R0101PN7K.', 'Added capability statement ciscoVtpCapV12R0254SGPCat4K.', 'Added capability statement ciscoVtpCapV12R0233SXI4PCat6K. Removed vtpVlanInfoEditGroup2 and added VARIATION on vtpVlanEditRowStatus to the following capability statements: ciscoVtpCapCatOSV08R0101, ciscoVtpCapCatOSV08R0301, ciscoVtpCapCatOSV08R0701 Removed vtpVlanInfoEditGroup2 and vtpDot1qTunnelGroup, added vtpDot1qTunnelGroup2, and added VARIATION on vtpVlanEditRowStatus to the following capability statements: ciscoVtpCapV12R0119ECat6K, ciscoVtpCapV12R0217SXCat6K, ciscoVtpCapV12R0217SXACat6K, ciscoVtpCapV12R0218SXECat6K, ciscoVtpCapV12R0233SXHPCat6K, ciscoVtpCapV12R0233SXIPCat6K.', 'Added capability statement ciscoVtpCapV12R0233SXIPCat6K.', 'Added capability statement ciscoVtpCapCatOSV08R0701.', 'Added capability statement ciscoVtpCapV12R0233SXHPCat6K.', 'Added VARIATION clause for managementDomainLocalMode in capability statement ciscoVtpCapV12R0119ECat6K, ciscoVtpCapV12R0217SXCat6K,ciscoVtpCapV12R0217SXACat6K and ciscoVtpCapV12R0218SXECat6K.', 'Added capability statement ciscoVtpCapV12R0218SXECat6K. Added VARIATION clause for vtpVlanTypeExt and vtpVlanEditTypeExt2 in capability statement ciscoVtpCapV12R0119ECat6K, ciscoVtpCapV12R0217SXCat6K and ciscoVtpCapV12R0217SXACat6K.', 'Added capability statement ciscoVtpCapV12R0217SXACat6K. Added a VARIATION statement for the object vlanTrunkPortDynamicStatus in capability statement ciscoVtpCapV12R0119ECat6K and ciscoVtpCapV12R0217SXCat6K.', 'Added capability statement ciscoVtpCapCatOSV08R0301.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVtpCapability.setLastUpdated('201309270000Z')
if mibBuilder.loadTexts: ciscoVtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVtpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVtpCapability.setDescription('The capabilities description of CISCO-VTP-MIB.')
ciscoVtpCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0119ECat6K = ciscoVtpCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0119ECat6K = ciscoVtpCapV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0119ECat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0217SXCat6K = ciscoVtpCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0217SXCat6K = ciscoVtpCapV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0217SXCat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0101 = ciscoVtpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0101 = ciscoVtpCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapCatOSV08R0101.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0301 = ciscoVtpCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0301 = ciscoVtpCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapCatOSV08R0301.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0217SXACat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0217SXACat6K = ciscoVtpCapV12R0217SXACat6K.setProductRelease('Cisco IOS 12.2(17)SXA on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0217SXACat6K = ciscoVtpCapV12R0217SXACat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0217SXACat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0218SXECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0218SXECat6K = ciscoVtpCapV12R0218SXECat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0218SXECat6K = ciscoVtpCapV12R0218SXECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0218SXECat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXHPCat6K = ciscoVtpCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXHPCat6K = ciscoVtpCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0233SXHPCat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0701 = ciscoVtpCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapCatOSV08R0701 = ciscoVtpCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapCatOSV08R0701.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXIPCat6K = ciscoVtpCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXIPCat6K = ciscoVtpCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0233SXIPCat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXI4PCat6K = ciscoVtpCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXI4PCat6K = ciscoVtpCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0233SXI4PCat6K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0254SGPCat4K = ciscoVtpCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0254SGPCat4K = ciscoVtpCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0254SGPCat4K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapNxOSV05R0101PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0101PN7K = ciscoVtpCapNxOSV05R0101PN7K.setProductRelease('Cisco NX-OS 5.1(1) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0101PN7K = ciscoVtpCapNxOSV05R0101PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapNxOSV05R0101PN7K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXJPCat6k = ciscoVtpCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV12R0233SXJPCat6k = ciscoVtpCapV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV12R0233SXJPCat6k.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapNxOSV05R0002PN5k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0002PN5k = ciscoVtpCapNxOSV05R0002PN5k.setProductRelease('Cisco NX-OS 5.0(2) on Nexus 5000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0002PN5k = ciscoVtpCapNxOSV05R0002PN5k.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapNxOSV05R0002PN5k.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapNxOSV05R0201PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0201PN7K = ciscoVtpCapNxOSV05R0201PN7K.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV05R0201PN7K = ciscoVtpCapNxOSV05R0201PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapNxOSV05R0201PN7K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV15R0001SYPCat6kSup2T = ciscoVtpCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV15R0001SYPCat6kSup2T = ciscoVtpCapV15R0001SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV15R0001SYPCat6kSup2T.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapNxOSV06R0101PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV06R0101PN7K = ciscoVtpCapNxOSV06R0101PN7K.setProductRelease('Cisco NX-OS 6.1(1) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapNxOSV06R0101PN7K = ciscoVtpCapNxOSV06R0101PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapNxOSV06R0101PN7K.setDescription('CISCO-VTP-MIB capabilities.')
ciscoVtpCapV15R0102SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 329, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV15R0102SYPCat6k = ciscoVtpCapV15R0102SYPCat6k.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVtpCapV15R0102SYPCat6k = ciscoVtpCapV15R0102SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoVtpCapV15R0102SYPCat6k.setDescription('CISCO-VTP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VTP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVtpCapability, ciscoVtpCapV12R0217SXCat6K=ciscoVtpCapV12R0217SXCat6K, ciscoVtpCapV12R0233SXHPCat6K=ciscoVtpCapV12R0233SXHPCat6K, ciscoVtpCapV15R0102SYPCat6k=ciscoVtpCapV15R0102SYPCat6k, ciscoVtpCapNxOSV06R0101PN7K=ciscoVtpCapNxOSV06R0101PN7K, ciscoVtpCapNxOSV05R0101PN7K=ciscoVtpCapNxOSV05R0101PN7K, ciscoVtpCapV12R0119ECat6K=ciscoVtpCapV12R0119ECat6K, ciscoVtpCapV12R0254SGPCat4K=ciscoVtpCapV12R0254SGPCat4K, ciscoVtpCapCatOSV08R0701=ciscoVtpCapCatOSV08R0701, ciscoVtpCapNxOSV05R0002PN5k=ciscoVtpCapNxOSV05R0002PN5k, ciscoVtpCapNxOSV05R0201PN7K=ciscoVtpCapNxOSV05R0201PN7K, ciscoVtpCapV12R0233SXI4PCat6K=ciscoVtpCapV12R0233SXI4PCat6K, ciscoVtpCapV15R0001SYPCat6kSup2T=ciscoVtpCapV15R0001SYPCat6kSup2T, ciscoVtpCapV12R0233SXJPCat6k=ciscoVtpCapV12R0233SXJPCat6k, ciscoVtpCapV12R0233SXIPCat6K=ciscoVtpCapV12R0233SXIPCat6K, ciscoVtpCapV12R0218SXECat6K=ciscoVtpCapV12R0218SXECat6K, ciscoVtpCapCatOSV08R0101=ciscoVtpCapCatOSV08R0101, ciscoVtpCapCatOSV08R0301=ciscoVtpCapCatOSV08R0301, ciscoVtpCapability=ciscoVtpCapability, ciscoVtpCapV12R0217SXACat6K=ciscoVtpCapV12R0217SXACat6K)
