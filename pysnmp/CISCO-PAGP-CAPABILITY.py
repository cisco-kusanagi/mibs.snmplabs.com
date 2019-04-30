#
# PySNMP MIB module CISCO-PAGP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PAGP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Bits, ObjectIdentity, Unsigned32, MibIdentifier, TimeTicks, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "IpAddress", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPagpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 391))
ciscoPagpCapability.setRevisions(('2011-09-27 00:00', '2010-11-17 00:00', '2010-05-06 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoPagpCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoPagpCapability.setOrganization('Cisco Systems, Inc.')
ciscoPagpCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setStatus('current')
ciscoPagpCapV12R0217aSXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setProductRelease('Cisco IOS 12.2(17a)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setStatus('current')
ciscoPagpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setStatus('current')
ciscoPagpCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setStatus('current')
ciscoPagpCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setStatus('current')
ciscoPagpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-PAGP-CAPABILITY", ciscoPagpCapCatOSV08R0101=ciscoPagpCapCatOSV08R0101, ciscoPagpCapV12R0254SGPCat4K=ciscoPagpCapV12R0254SGPCat4K, PYSNMP_MODULE_ID=ciscoPagpCapability, ciscoPagpCapV12R0111bEXCat6k=ciscoPagpCapV12R0111bEXCat6k, ciscoPagpCapV12R0250SYPCat6K=ciscoPagpCapV12R0250SYPCat6K, ciscoPagpCapV12R0217aSXCat6k=ciscoPagpCapV12R0217aSXCat6k, ciscoPagpCapV15R0001SYPCat6k=ciscoPagpCapV15R0001SYPCat6k, ciscoPagpCapability=ciscoPagpCapability)
