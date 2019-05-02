#
# PySNMP MIB module CISCO-AUTH-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AUTH-FRAMEWORK-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, MibIdentifier, Bits, NotificationType, Unsigned32, ObjectIdentity, TimeTicks, Gauge32, Integer32, Counter32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "MibIdentifier", "Bits", "NotificationType", "Unsigned32", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "Counter32", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAuthFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 573))
ciscoAuthFrameworkCapability.setRevisions(('2012-09-04 00:00', '2012-04-02 00:00', '2011-03-29 00:00', '2011-03-24 00:00', '2010-05-06 00:00', '2010-04-05 00:00', '2010-03-09 00:00', '2009-05-18 00:00', '2008-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setRevisionsDescriptions(('Added capability statement cafCapV15R0101SYPCat6K.', 'Added capability statement cafCapV15R0101SGPCat4K.', 'Added capability statement cafCapV15R0002SGPCat4K. Updated VARIATION of cafPortViolationAction for cafCapV12R0254SGPCat4K.', 'Added capability statement cafCapV12R0233SXJPCat6K. Updated VARIATION of cafPortViolationAction for cafCapV12R0233SXI4PCat6K.', 'Added capability statement cafCapV12R0254SGPCat4K.', 'Added capability statement cafCapV12R0233SXI4PCat6K.', 'Added capability statement cafCapV12R0252SGPCat4K.', 'Added capability statement cafCapV12R0233SXI2PCat6K. Updated cafCapV12R0233SXIPCat6K with additional VARIATION clauses.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ibns@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setDescription('The capabilities description of CISCO-AUTH-FRAMEWORK-MIB.')
cafCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0233SXIPCat6K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0233SXI2PCat6K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0252SGPCat4K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0233SXI4PCat6K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0254SGPCat4K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setStatus('current')
if mibBuilder.loadTexts: cafCapV12R0233SXJPCat6K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cafCapV15R0002SGPCat4K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV15R0101SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cafCapV15R0101SGPCat4K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
cafCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cafCapV15R0101SYPCat6K.setDescription('CISCO-AUTH-FRAMEWORK-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-AUTH-FRAMEWORK-CAPABILITY", cafCapV12R0233SXIPCat6K=cafCapV12R0233SXIPCat6K, cafCapV15R0101SYPCat6K=cafCapV15R0101SYPCat6K, cafCapV12R0252SGPCat4K=cafCapV12R0252SGPCat4K, cafCapV15R0002SGPCat4K=cafCapV15R0002SGPCat4K, ciscoAuthFrameworkCapability=ciscoAuthFrameworkCapability, PYSNMP_MODULE_ID=ciscoAuthFrameworkCapability, cafCapV12R0233SXJPCat6K=cafCapV12R0233SXJPCat6K, cafCapV12R0233SXI2PCat6K=cafCapV12R0233SXI2PCat6K, cafCapV15R0101SGPCat4K=cafCapV15R0101SGPCat4K, cafCapV12R0254SGPCat4K=cafCapV12R0254SGPCat4K, cafCapV12R0233SXI4PCat6K=cafCapV12R0233SXI4PCat6K)
