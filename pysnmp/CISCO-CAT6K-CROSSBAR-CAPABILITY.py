#
# PySNMP MIB module CISCO-CAT6K-CROSSBAR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAT6K-CROSSBAR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Counter32, NotificationType, ObjectIdentity, Integer32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "Integer32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCat6kCrossbarCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 356))
ciscoCat6kCrossbarCapability.setRevisions(('2013-07-25 00:00', '2010-11-24 00:00', '2010-03-11 00:00', '2008-10-22 00:00', '2008-03-24 00:00', '2008-03-14 00:00', '2007-11-19 00:00', '2007-06-28 00:00', '2007-01-03 00:00', '2005-06-22 00:00', '2005-05-03 00:00', '2004-10-19 00:00', '2004-04-19 00:00', '2004-04-02 00:00',))
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setLastUpdated('201307250000Z')
if mibBuilder.loadTexts: ciscoCat6kCrossbarCapability.setOrganization('Cisco Systems, Inc.')
ccXbarCapV12R0108aEXCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0108aEXCat6KSup2 = ccXbarCapV12R0108aEXCat6KSup2.setProductRelease('Cisco IOS 12.1(8a)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0108aEXCat6KSup2 = ccXbarCapV12R0108aEXCat6KSup2.setStatus('current')
ccXbarCapV12R0214SXCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0214SXCat6KSup720 = ccXbarCapV12R0214SXCat6KSup720.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0214SXCat6KSup720 = ccXbarCapV12R0214SXCat6KSup720.setStatus('current')
ccXbarCapCatOSV06R0301Cat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV06R0301Cat6KSup2 = ccXbarCapCatOSV06R0301Cat6KSup2.setProductRelease('Cisco CatOS 6.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices\n                         with Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV06R0301Cat6KSup2 = ccXbarCapCatOSV06R0301Cat6KSup2.setStatus('current')
ccXbarCapCatOSV08R0101Cat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup2 = ccXbarCapCatOSV08R0101Cat6KSup2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices\n                         with Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup2 = ccXbarCapCatOSV08R0101Cat6KSup2.setStatus('current')
ccXbarCapCatOSV08R0101Cat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup720 = ccXbarCapCatOSV08R0101Cat6KSup720.setProductRelease('Cisco CatOS 8.1(1) on  Catalyst 6500\n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0101Cat6KSup720 = ccXbarCapCatOSV08R0101Cat6KSup720.setStatus('current')
ccXbarCapV12R0218SXDCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup720 = ccXbarCapV12R0218SXDCat6KSup720.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup720 = ccXbarCapV12R0218SXDCat6KSup720.setStatus('current')
ccXbarCapV12R0218SXDCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup2 = ccXbarCapV12R0218SXDCat6KSup2.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXDCat6KSup2 = ccXbarCapV12R0218SXDCat6KSup2.setStatus('current')
ccXbarCapV12R0119EPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0119EPCat6KSup2 = ccXbarCapV12R0119EPCat6KSup2.setProductRelease('Cisco IOS 12.1(19)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0119EPCat6KSup2 = ccXbarCapV12R0119EPCat6KSup2.setStatus('current')
ccXbarCapV12R0123E01PCat6KSup1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup1 = ccXbarCapV12R0123E01PCat6KSup1.setProductRelease('Cisco IOS 12.1(23)E1 on Catalyst 6000/6500 \n                        series devices with Supervisor 1 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup1 = ccXbarCapV12R0123E01PCat6KSup1.setStatus('current')
ccXbarCapV12R0123E01PCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup2 = ccXbarCapV12R0123E01PCat6KSup2.setProductRelease('Cisco IOS 12.1(23)E1 on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0123E01PCat6KSup2 = ccXbarCapV12R0123E01PCat6KSup2.setStatus('current')
ccXbarCapV12R012504EPCat6KSup1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup1 = ccXbarCapV12R012504EPCat6KSup1.setProductRelease('Cisco IOS 12.1(25.04)E on Catalyst 6000/6500 \n                        series devices with Supervisor 1 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup1 = ccXbarCapV12R012504EPCat6KSup1.setStatus('current')
ccXbarCapV12R012504EPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup2 = ccXbarCapV12R012504EPCat6KSup2.setProductRelease('Cisco IOS 12.1(25.04)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with \n                         Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R012504EPCat6KSup2 = ccXbarCapV12R012504EPCat6KSup2.setStatus('current')
ccXbarCapV12R0218SXFPCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup2 = ccXbarCapV12R0218SXFPCat6KSup2.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup2 = ccXbarCapV12R0218SXFPCat6KSup2.setStatus('current')
ccXbarCapV12R0218SXFPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup720 = ccXbarCapV12R0218SXFPCat6KSup720.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup720 = ccXbarCapV12R0218SXFPCat6KSup720.setStatus('current')
ccXbarCapV12R0218SXFPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup32 = ccXbarCapV12R0218SXFPCat6KSup32.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500 \n                        and Cisco 7600 series devices with \n                        Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0218SXFPCat6KSup32 = ccXbarCapV12R0218SXFPCat6KSup32.setStatus('current')
ccXbarCapCatOSV08R0601Cat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0601Cat6KSup32 = ccXbarCapCatOSV08R0601Cat6KSup32.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6500\n                        series devices with Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0601Cat6KSup32 = ccXbarCapCatOSV08R0601Cat6KSup32.setStatus('current')
ccXbarCapV12R0233SXHPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup720 = ccXbarCapV12R0233SXHPCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                        series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup720 = ccXbarCapV12R0233SXHPCat6KSup720.setStatus('current')
ccXbarCapV12R0233SXHPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup32 = ccXbarCapV12R0233SXHPCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXHPCat6KSup32 = ccXbarCapV12R0233SXHPCat6KSup32.setStatus('current')
ccXbarCapV12R0233SXH01PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXH01PCat6KSup720 = ccXbarCapV12R0233SXH01PCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                        series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXH01PCat6KSup720 = ccXbarCapV12R0233SXH01PCat6KSup720.setStatus('current')
ccXbarCapCatOSV08R0701PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup720 = ccXbarCapCatOSV08R0701PCat6KSup720.setProductRelease('Cisco CatOS 8.7(1) on  Catalyst 6000/6500\n                        and Cisco 7600 series devices with \n                        Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup720 = ccXbarCapCatOSV08R0701PCat6KSup720.setStatus('current')
ccXbarCapCatOSV08R0701PCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup32 = ccXbarCapCatOSV08R0701PCat6KSup32.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6500\n                     series devices with Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup32 = ccXbarCapCatOSV08R0701PCat6KSup32.setStatus('current')
ccXbarCapCatOSV08R0701PCat6KSup2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup2 = ccXbarCapCatOSV08R0701PCat6KSup2.setProductRelease('Cisco CatOS 8.7(1) on  Catalyst 6000/6500\n                     and Cisco 7600 series devices with \n                     Supervisor 2 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapCatOSV08R0701PCat6KSup2 = ccXbarCapCatOSV08R0701PCat6KSup2.setStatus('current')
ccXbarCapV12R0233SXIPCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup720 = ccXbarCapV12R0233SXIPCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup720 = ccXbarCapV12R0233SXIPCat6KSup720.setStatus('current')
ccXbarCapV12R0233SXIPCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup32 = ccXbarCapV12R0233SXIPCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXIPCat6KSup32 = ccXbarCapV12R0233SXIPCat6KSup32.setStatus('current')
ccXbarCapV12R0233SXI4PCat6KSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup720 = ccXbarCapV12R0233SXI4PCat6KSup720.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup720 = ccXbarCapV12R0233SXI4PCat6KSup720.setStatus('current')
ccXbarCapV12R0233SXI4PCat6KSup32 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup32 = ccXbarCapV12R0233SXI4PCat6KSup32.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices with Supervisor 32 present\n                     and ME-C65xx series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0233SXI4PCat6KSup32 = ccXbarCapV12R0233SXI4PCat6KSup32.setStatus('current')
ccXbarCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0250SYPCat6K = ccXbarCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV12R0250SYPCat6K = ccXbarCapV12R0250SYPCat6K.setStatus('current')
ccXbarCapV15R0102SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup2T = ccXbarCapV15R0102SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup2T = ccXbarCapV15R0102SYPCat6kSup2T.setStatus('current')
ccXbarCapV15R0102SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 356, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup720 = ccXbarCapV15R0102SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccXbarCapV15R0102SYPCat6kSup720 = ccXbarCapV15R0102SYPCat6kSup720.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAT6K-CROSSBAR-CAPABILITY", ccXbarCapV12R0233SXIPCat6KSup32=ccXbarCapV12R0233SXIPCat6KSup32, ccXbarCapV12R012504EPCat6KSup1=ccXbarCapV12R012504EPCat6KSup1, ccXbarCapCatOSV08R0701PCat6KSup2=ccXbarCapCatOSV08R0701PCat6KSup2, ccXbarCapV12R0119EPCat6KSup2=ccXbarCapV12R0119EPCat6KSup2, ccXbarCapV15R0102SYPCat6kSup2T=ccXbarCapV15R0102SYPCat6kSup2T, PYSNMP_MODULE_ID=ciscoCat6kCrossbarCapability, ccXbarCapV12R0218SXDCat6KSup2=ccXbarCapV12R0218SXDCat6KSup2, ccXbarCapV12R012504EPCat6KSup2=ccXbarCapV12R012504EPCat6KSup2, ccXbarCapV12R0218SXFPCat6KSup32=ccXbarCapV12R0218SXFPCat6KSup32, ccXbarCapCatOSV06R0301Cat6KSup2=ccXbarCapCatOSV06R0301Cat6KSup2, ccXbarCapCatOSV08R0701PCat6KSup720=ccXbarCapCatOSV08R0701PCat6KSup720, ccXbarCapCatOSV08R0601Cat6KSup32=ccXbarCapCatOSV08R0601Cat6KSup32, ccXbarCapV12R0250SYPCat6K=ccXbarCapV12R0250SYPCat6K, ccXbarCapV12R0218SXDCat6KSup720=ccXbarCapV12R0218SXDCat6KSup720, ccXbarCapV12R0123E01PCat6KSup2=ccXbarCapV12R0123E01PCat6KSup2, ccXbarCapV15R0102SYPCat6kSup720=ccXbarCapV15R0102SYPCat6kSup720, ccXbarCapV12R0108aEXCat6KSup2=ccXbarCapV12R0108aEXCat6KSup2, ccXbarCapV12R0233SXIPCat6KSup720=ccXbarCapV12R0233SXIPCat6KSup720, ccXbarCapCatOSV08R0101Cat6KSup720=ccXbarCapCatOSV08R0101Cat6KSup720, ccXbarCapV12R0218SXFPCat6KSup720=ccXbarCapV12R0218SXFPCat6KSup720, ccXbarCapV12R0233SXHPCat6KSup720=ccXbarCapV12R0233SXHPCat6KSup720, ccXbarCapCatOSV08R0701PCat6KSup32=ccXbarCapCatOSV08R0701PCat6KSup32, ccXbarCapCatOSV08R0101Cat6KSup2=ccXbarCapCatOSV08R0101Cat6KSup2, ciscoCat6kCrossbarCapability=ciscoCat6kCrossbarCapability, ccXbarCapV12R0233SXI4PCat6KSup32=ccXbarCapV12R0233SXI4PCat6KSup32, ccXbarCapV12R0123E01PCat6KSup1=ccXbarCapV12R0123E01PCat6KSup1, ccXbarCapV12R0214SXCat6KSup720=ccXbarCapV12R0214SXCat6KSup720, ccXbarCapV12R0233SXH01PCat6KSup720=ccXbarCapV12R0233SXH01PCat6KSup720, ccXbarCapV12R0233SXHPCat6KSup32=ccXbarCapV12R0233SXHPCat6KSup32, ccXbarCapV12R0233SXI4PCat6KSup720=ccXbarCapV12R0233SXI4PCat6KSup720, ccXbarCapV12R0218SXFPCat6KSup2=ccXbarCapV12R0218SXFPCat6KSup2)
