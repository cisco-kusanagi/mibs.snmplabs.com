#
# PySNMP MIB module CISCO-POWER-ETHERNET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POWER-ETHERNET-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, Gauge32, IpAddress, Integer32, NotificationType, MibIdentifier, Counter32, iso, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "iso", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPowerEthernetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 406))
ciscoPowerEthernetExtCapability.setRevisions(('2013-07-16 00:00', '2012-12-12 00:00', '2012-04-04 00:00', '2009-05-29 00:00', '2008-10-28 00:00', '2007-06-29 00:00', '2007-06-27 00:00', '2007-02-08 00:00', '2006-12-20 00:00', '2006-10-19 00:00', '2004-06-15 00:00', '2004-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setRevisionsDescriptions(('Added capability statement cPowerEthExtCapV15R0102SYPCat6K.', 'Added capability statement cPowerEthExtCapV15R0101SYPCat6K.', 'Added capability statement cPowerEthExtCapV12R0233SXJ2PCat6K and cPowerEthExtCapV15R0101SGCat4K. Added VARIATION of cpeExtPdStatsClass to capability statement cPowerEthExtCapV12R0233SXIPCat6K.', 'Added capability statement cPowerEthExtCapV12R0252SGPCat4K. Modified VARIATION of cpeExtPsePortPwrMax in capability statement cPowerEthExtCapCatOSV08R0401, cPowerEthExtCapCatOSV08R0501, cPowerEthExtCapCatOSV08R0601, cPowerEthExtCapV12R0233SXHPCat6K, cPowerEthExtCapV12R0233SXIPCat6K. Modified VARIATION of cpeExtDefaultAllocation in capability statement cPowerEthExtCapCatOSV08R0501, cPowerEthExtCapCatOSV08R0601.', 'Added capability statement cPowerEthExtCapV12R0233SXIPCat6K.', 'Added capability statement cPowerEthExtCapV12R0233SXHPCat6K.', 'Added capability statement cPowerEthExtCapC3kV122SU040', 'Added Agent Capability for c3550 in cPowerEthExtCapC3kV122SR035', 'Added capability statement cPowerEthExtCapCatOSV08R0601.', 'Added capability statement cPowerEthExtCapC3kV122SR035.', 'Added capability statement cPowerEthExtCapCatOSV08R0501.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setLastUpdated('201307160000Z')
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setDescription('The capabilities description of CISCO-POWER-ETHERNET-EXT-MIB.')
cPowerEthExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0401 = cPowerEthExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0401 = cPowerEthExtCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapCatOSV08R0401.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0501 = cPowerEthExtCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0501 = cPowerEthExtCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapCatOSV08R0501.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapC3kV122SR035 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SR035 = cPowerEthExtCapC3kV122SR035.setProductRelease('CISCO IOS 12.2S(0.35) for Cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SR035 = cPowerEthExtCapC3kV122SR035.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapC3kV122SR035.setDescription('CISCO-POWER-ETHERNET-EXT-MIB Capabilities')
cPowerEthExtCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0601 = cPowerEthExtCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0601 = cPowerEthExtCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapCatOSV08R0601.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapC3kV122SU040 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SU040 = cPowerEthExtCapC3kV122SU040.setProductRelease('CISCO IOS 12.2S(0.40) for Cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SU040 = cPowerEthExtCapC3kV122SU040.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapC3kV122SU040.setDescription('CISCO-POWER-ETHERNET-EXT-MIB Capabilities')
cPowerEthExtCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXHPCat6K = cPowerEthExtCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXHPCat6K = cPowerEthExtCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV12R0233SXHPCat6K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXIPCat6K = cPowerEthExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXIPCat6K = cPowerEthExtCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV12R0233SXIPCat6K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0252SGPCat4K = cPowerEthExtCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0252SGPCat4K = cPowerEthExtCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV12R0252SGPCat4K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV12R0233SXJ2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXJ2PCat6K = cPowerEthExtCapV12R0233SXJ2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXJ2PCat6K = cPowerEthExtCapV12R0233SXJ2PCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV12R0233SXJ2PCat6K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV15R0101SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SGCat4K = cPowerEthExtCapV15R0101SGCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SGCat4K = cPowerEthExtCapV15R0101SGCat4K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV15R0101SGCat4K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SYPCat6K = cPowerEthExtCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SYPCat6K = cPowerEthExtCapV15R0101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV15R0101SYPCat6K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
cPowerEthExtCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0102SYPCat6K = cPowerEthExtCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0102SYPCat6K = cPowerEthExtCapV15R0102SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cPowerEthExtCapV15R0102SYPCat6K.setDescription('CISCO-POWER-ETHERNET-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-EXT-CAPABILITY", cPowerEthExtCapV12R0252SGPCat4K=cPowerEthExtCapV12R0252SGPCat4K, cPowerEthExtCapC3kV122SR035=cPowerEthExtCapC3kV122SR035, cPowerEthExtCapV12R0233SXHPCat6K=cPowerEthExtCapV12R0233SXHPCat6K, cPowerEthExtCapV15R0101SGCat4K=cPowerEthExtCapV15R0101SGCat4K, cPowerEthExtCapC3kV122SU040=cPowerEthExtCapC3kV122SU040, cPowerEthExtCapV12R0233SXJ2PCat6K=cPowerEthExtCapV12R0233SXJ2PCat6K, cPowerEthExtCapV15R0102SYPCat6K=cPowerEthExtCapV15R0102SYPCat6K, cPowerEthExtCapV12R0233SXIPCat6K=cPowerEthExtCapV12R0233SXIPCat6K, cPowerEthExtCapV15R0101SYPCat6K=cPowerEthExtCapV15R0101SYPCat6K, cPowerEthExtCapCatOSV08R0401=cPowerEthExtCapCatOSV08R0401, cPowerEthExtCapCatOSV08R0501=cPowerEthExtCapCatOSV08R0501, cPowerEthExtCapCatOSV08R0601=cPowerEthExtCapCatOSV08R0601, ciscoPowerEthernetExtCapability=ciscoPowerEthernetExtCapability, PYSNMP_MODULE_ID=ciscoPowerEthernetExtCapability)
