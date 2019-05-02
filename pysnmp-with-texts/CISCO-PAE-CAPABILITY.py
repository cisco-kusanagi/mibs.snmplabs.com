#
# PySNMP MIB module CISCO-PAE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PAE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, Bits, Counter32, ObjectIdentity, Integer32, iso, NotificationType, IpAddress, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "Integer32", "iso", "NotificationType", "IpAddress", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPaeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 319))
ciscoPaeCapability.setRevisions(('2010-11-01 00:00', '2010-03-22 00:00', '2010-03-15 00:00', '2009-12-31 00:00', '2008-11-06 00:00', '2008-11-04 00:00', '2008-10-20 00:00', '2008-04-24 00:00', '2007-07-09 00:00', '2007-04-26 00:00', '2007-02-27 00:00', '2005-09-05 00:00', '2004-01-16 00:00', '2003-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPaeCapability.setRevisionsDescriptions(('Added capability statement ciscoPaeCapV12R0250SYPCat6K.', 'Added capability statement ciscoPaeCapV12R0233SXI4PCat6K.', 'Added capability statement ciscoPaeCapV120252SGPCat4K. Added VARIATIONs for cpaePortEntry, cpaeAuthConfigEntry, and cpaeMacAuthBypassPortEntry in capability statement ciscoPaeCapV12R0233SXIPCat6K.', 'Removed cpaePortAuthFailUserInfoGroup from capability statement ciscoPaeCapV12R0233SXIPCat6K.', 'Added capability statement ciscoPaeCapV12R0233SXIPCat6K.', 'Added capability statement ciscoPaeCapCatOSV08R0702.', 'Added capability statement ciscoPaeCapV12R0246SECat3K.', 'Added capability statement ciscoPaeCapCatOSV08R0701. Added VARIATION for cpaePortMode in capability statement ciscoPaeCapV12R0233SXHPCat6K.', 'Added capability statement ciscoPaeCapV12R0233SXHPCat6K.', 'Added capability statement ciscoPaeCapCatOSV08R0602.', 'Added capability statement ciscoPaeCapCatOSV08R0601.', 'Added capability statement ciscoPaeCapCatOSV08R0501. Added VARIATION for cpaeGuestVlanNumber in capability statement ciscoPaeCapCatOSV08R0101Cat6K. Added VARIATION for cpaeGuestVlanNumber in capability statement ciscoPaeCapCatOSV08R0101Cat4K. Added VARIATION for cpaeGuestVlanNumber in capability statement ciscoPaeCapCatOSV08R0301', 'Added capability statement ciscoPaeCapCatOSV08R0301.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPaeCapability.setLastUpdated('201011010000Z')
if mibBuilder.loadTexts: ciscoPaeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPaeCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ibns@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPaeCapability.setDescription('The capabilities description of CISCO-PAE-MIB.')
ciscoPaeCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0111bEXCat6K = ciscoPaeCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0111bEXCat6K = ciscoPaeCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0111bEXCat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV07R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0101 = ciscoPaeCapCatOSV07R0101.setProductRelease('Cisco CatOS 7.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0101 = ciscoPaeCapCatOSV07R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV07R0101.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV07R0501Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0501Cat6K = ciscoPaeCapCatOSV07R0501Cat6K.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0501Cat6K = ciscoPaeCapCatOSV07R0501Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV07R0501Cat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV07R0601Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0601Cat6K = ciscoPaeCapCatOSV07R0601Cat6K.setProductRelease('Cisco CatOS 7.6(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV07R0601Cat6K = ciscoPaeCapCatOSV07R0601Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV07R0601Cat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0101Cat6K = ciscoPaeCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0101Cat6K = ciscoPaeCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0101Cat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0101Cat4K = ciscoPaeCapCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                    devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0101Cat4K = ciscoPaeCapCatOSV08R0101Cat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0101Cat4K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0301 = ciscoPaeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0301 = ciscoPaeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0301.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0501 = ciscoPaeCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0501 = ciscoPaeCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0501.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0601 = ciscoPaeCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0601 = ciscoPaeCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0601.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0602 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0602 = ciscoPaeCapCatOSV08R0602.setProductRelease('Cisco CatOS 8.6(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0602 = ciscoPaeCapCatOSV08R0602.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0602.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXHPCat6K = ciscoPaeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXHPCat6K = ciscoPaeCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0233SXHPCat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0701 = ciscoPaeCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0701 = ciscoPaeCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0701.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV12R0246SECat3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0246SECat3K = ciscoPaeCapV12R0246SECat3K.setProductRelease('Cisco IOS 12.2(46)SE.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0246SECat3K = ciscoPaeCapV12R0246SECat3K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0246SECat3K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0702 = ciscoPaeCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapCatOSV08R0702 = ciscoPaeCapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapCatOSV08R0702.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXIPCat6K = ciscoPaeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXIPCat6K = ciscoPaeCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0233SXIPCat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV120252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV120252SGPCat4K = ciscoPaeCapV120252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV120252SGPCat4K = ciscoPaeCapV120252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV120252SGPCat4K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXI4PCat6K = ciscoPaeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0233SXI4PCat6K = ciscoPaeCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0233SXI4PCat6K.setDescription('CISCO-PAE-MIB capabilities.')
ciscoPaeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 319, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0250SYPCat6K = ciscoPaeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPaeCapV12R0250SYPCat6K = ciscoPaeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPaeCapV12R0250SYPCat6K.setDescription('CISCO-PAE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PAE-CAPABILITY", ciscoPaeCapCatOSV08R0101Cat6K=ciscoPaeCapCatOSV08R0101Cat6K, ciscoPaeCapV120252SGPCat4K=ciscoPaeCapV120252SGPCat4K, ciscoPaeCapCatOSV08R0601=ciscoPaeCapCatOSV08R0601, ciscoPaeCapCatOSV08R0602=ciscoPaeCapCatOSV08R0602, ciscoPaeCapV12R0250SYPCat6K=ciscoPaeCapV12R0250SYPCat6K, ciscoPaeCapV12R0233SXHPCat6K=ciscoPaeCapV12R0233SXHPCat6K, ciscoPaeCapCatOSV08R0702=ciscoPaeCapCatOSV08R0702, ciscoPaeCapCatOSV08R0501=ciscoPaeCapCatOSV08R0501, ciscoPaeCapCatOSV07R0101=ciscoPaeCapCatOSV07R0101, ciscoPaeCapability=ciscoPaeCapability, PYSNMP_MODULE_ID=ciscoPaeCapability, ciscoPaeCapCatOSV08R0301=ciscoPaeCapCatOSV08R0301, ciscoPaeCapCatOSV07R0501Cat6K=ciscoPaeCapCatOSV07R0501Cat6K, ciscoPaeCapV12R0111bEXCat6K=ciscoPaeCapV12R0111bEXCat6K, ciscoPaeCapV12R0233SXIPCat6K=ciscoPaeCapV12R0233SXIPCat6K, ciscoPaeCapCatOSV07R0601Cat6K=ciscoPaeCapCatOSV07R0601Cat6K, ciscoPaeCapV12R0246SECat3K=ciscoPaeCapV12R0246SECat3K, ciscoPaeCapCatOSV08R0101Cat4K=ciscoPaeCapCatOSV08R0101Cat4K, ciscoPaeCapCatOSV08R0701=ciscoPaeCapCatOSV08R0701, ciscoPaeCapV12R0233SXI4PCat6K=ciscoPaeCapV12R0233SXI4PCat6K)
