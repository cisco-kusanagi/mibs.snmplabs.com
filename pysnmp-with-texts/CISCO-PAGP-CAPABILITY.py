#
# PySNMP MIB module CISCO-PAGP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PAGP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Bits, Counter64, Gauge32, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "Counter64", "Gauge32", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPagpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 391))
ciscoPagpCapability.setRevisions(('2011-09-27 00:00', '2010-11-17 00:00', '2010-05-06 00:00', '2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPagpCapability.setRevisionsDescriptions(('Add ciscoPagpCapV15R0001SYPCat6k agent capability statement. Added VARIATION for pagpDistributionProtocol object in ciscoPagpCapCatOSV08R0101 agent capabilty statement.', 'Added capability statement ciscoPagpCapV12R0250SYPCat6K.', 'Add ciscoPagpCapV12R0254SGPCat4K agent capability statement. Add VARIATION for pagpDistributionProtocol object in ciscoPagpCapV12R0217aSXCat6k agent capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPagpCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoPagpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPagpCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-etherchan@cisco.com')
if mibBuilder.loadTexts: ciscoPagpCapability.setDescription('The capabilities description of CISCO-PAGP-MIB.')
ciscoPagpCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapV12R0111bEXCat6k.setDescription('CISCO-PAGP-MIB capabilities.')
ciscoPagpCapV12R0217aSXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setProductRelease('Cisco IOS 12.2(17a)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapV12R0217aSXCat6k.setDescription('CISCO-PAGP-MIB capabilities.')
ciscoPagpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapCatOSV08R0101.setDescription('CISCO-PAGP-MIB capabilities.')
ciscoPagpCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapV12R0254SGPCat4K.setDescription('CISCO-PAGP-MIB capabilities.')
ciscoPagpCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapV12R0250SYPCat6K.setDescription('CISCO-PAGP-MIB capabilities.')
ciscoPagpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoPagpCapV15R0001SYPCat6k.setDescription('CISCO-PAGP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PAGP-CAPABILITY", ciscoPagpCapability=ciscoPagpCapability, ciscoPagpCapV12R0111bEXCat6k=ciscoPagpCapV12R0111bEXCat6k, ciscoPagpCapCatOSV08R0101=ciscoPagpCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoPagpCapability, ciscoPagpCapV12R0254SGPCat4K=ciscoPagpCapV12R0254SGPCat4K, ciscoPagpCapV12R0217aSXCat6k=ciscoPagpCapV12R0217aSXCat6k, ciscoPagpCapV12R0250SYPCat6K=ciscoPagpCapV12R0250SYPCat6K, ciscoPagpCapV15R0001SYPCat6k=ciscoPagpCapV15R0001SYPCat6k)
