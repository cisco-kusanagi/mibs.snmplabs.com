#
# PySNMP MIB module CISCO-STP-EXTENSIONS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-STP-EXTENSIONS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Unsigned32, Bits, iso, NotificationType, Gauge32, Counter64, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "NotificationType", "Gauge32", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoStpExtensionsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 360))
ciscoStpExtensionsCapability.setRevisions(('2014-03-27 00:00', '2013-09-30 00:00', '2011-09-30 00:00', '2007-02-23 00:00', '2005-09-15 00:00', '2005-06-15 00:00', '2004-11-20 00:00', '2004-06-02 00:00', '2004-04-02 00:00', '2004-01-21 00:00', '2003-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setRevisionsDescriptions(('Added capability statement cstpxCapNxOSV05R0201PN7k.', 'Added capability statement cstpxCapV15R0102SYPCat6k and cstpxCapV15R0102SYPCat6kSup2T. Added VARIATION clause on stpxFastStartPortMode to the following capability statements: cstpxCapCatOSV08R0101 cstpxCapV12R0113E cstpxCapV12R0214SX cstpxCapCatOSV08R0301 cstpxCapV12R0217bSXACat6k cstpxCapCatOSV08R0401 cstpxCapV12R0218SXEPCat6k cstpxCapCatOSV08R0501 cstpxCapV12R0218SXFPCat6k cstpxCapV15R0001SYPCat6kSup2T', 'Added capability statement cstpxCapV15R0001SYPCat6kSup2T.', 'Added VARIATION clause for stpxUplinkStationLearningGenRate in agent capability statements of cstpxCapV12R0113E, cstpxCapV12R0214SX, cstpxCapV12R0217bSXACat6k, cstpxCapV12R0218SXEPCat6k, and cstpxCapV12R0218SXFPCat6k.', 'Added cstpxCapV12R0218SXFPCat6k for Cisco IOS 12.2(18)SXF.', 'Added cstpxCapCatOSV08R0501 for Cisco CatOS 8.5(1).', 'Added cstpxCapV12R0218SXEPCat6k for Cisco IOS 12.2(18)SXE.', 'Added cstpxCapCatOSV08R0401 for Cisco CatOS 8.4(1).', 'Added cstpxCapV12R0217bSXACat6k for Cisco IOS 12.2(17b)SXA.', 'Added cstpxCapCatOSV08R0301 for Cisco CatOS 8.3(1).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setLastUpdated('201403270000Z')
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setDescription('The capabilities description of CISCO-STP-EXTENSIONS-MIB.')
cstpxCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0101 = cstpxCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0101 = cstpxCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cstpxCapCatOSV08R0101.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV12R0113E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0113E = cstpxCapV12R0113E.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0113E = cstpxCapV12R0113E.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV12R0113E.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV12R0214SX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0214SX = cstpxCapV12R0214SX.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0214SX = cstpxCapV12R0214SX.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV12R0214SX.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0301 = cstpxCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0301 = cstpxCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: cstpxCapCatOSV08R0301.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV12R0217bSXACat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0217bSXACat6k = cstpxCapV12R0217bSXACat6k.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0217bSXACat6k = cstpxCapV12R0217bSXACat6k.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV12R0217bSXACat6k.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0401 = cstpxCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0401 = cstpxCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cstpxCapCatOSV08R0401.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV12R0218SXEPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXEPCat6k = cstpxCapV12R0218SXEPCat6k.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXEPCat6k = cstpxCapV12R0218SXEPCat6k.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV12R0218SXEPCat6k.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0501 = cstpxCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0501 = cstpxCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cstpxCapCatOSV08R0501.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXFPCat6k = cstpxCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXFPCat6k = cstpxCapV12R0218SXFPCat6k.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV12R0218SXFPCat6k.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0001SYPCat6kSup2T = cstpxCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0001SYPCat6kSup2T = cstpxCapV15R0001SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV15R0001SYPCat6kSup2T.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV15R0102SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6k = cstpxCapV15R0102SYPCat6k.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6k = cstpxCapV15R0102SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV15R0102SYPCat6k.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapV15R0102SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6kSup2T = cstpxCapV15R0102SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6kSup2T = cstpxCapV15R0102SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: cstpxCapV15R0102SYPCat6kSup2T.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
cstpxCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapNxOSV05R0201PN7k = cstpxCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapNxOSV05R0201PN7k = cstpxCapNxOSV05R0201PN7k.setStatus('current')
if mibBuilder.loadTexts: cstpxCapNxOSV05R0201PN7k.setDescription('CISCO-STP-EXTENSIONS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-STP-EXTENSIONS-CAPABILITY", cstpxCapNxOSV05R0201PN7k=cstpxCapNxOSV05R0201PN7k, cstpxCapV12R0113E=cstpxCapV12R0113E, ciscoStpExtensionsCapability=ciscoStpExtensionsCapability, cstpxCapV12R0217bSXACat6k=cstpxCapV12R0217bSXACat6k, cstpxCapCatOSV08R0401=cstpxCapCatOSV08R0401, cstpxCapCatOSV08R0301=cstpxCapCatOSV08R0301, cstpxCapCatOSV08R0501=cstpxCapCatOSV08R0501, cstpxCapV15R0102SYPCat6kSup2T=cstpxCapV15R0102SYPCat6kSup2T, cstpxCapV12R0218SXEPCat6k=cstpxCapV12R0218SXEPCat6k, cstpxCapV12R0214SX=cstpxCapV12R0214SX, cstpxCapV15R0102SYPCat6k=cstpxCapV15R0102SYPCat6k, cstpxCapV12R0218SXFPCat6k=cstpxCapV12R0218SXFPCat6k, cstpxCapCatOSV08R0101=cstpxCapCatOSV08R0101, cstpxCapV15R0001SYPCat6kSup2T=cstpxCapV15R0001SYPCat6kSup2T, PYSNMP_MODULE_ID=ciscoStpExtensionsCapability)
