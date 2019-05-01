#
# PySNMP MIB module CISCO-IEEE8023-LAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IEEE8023-LAG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, iso, TimeTicks, Unsigned32, Integer32, ObjectIdentity, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, IpAddress, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "Integer32", "ObjectIdentity", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8023LagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 337))
ciscoIeee8023LagCapability.setRevisions(('2006-04-19 00:00', '2004-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setRevisionsDescriptions(('Added cIeee8023LagCapCatOSV08R0601.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setLastUpdated('200604190000Z')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setDescription('The capabilities description of IEEE8023-LAG-MIB.')
cIeee8023LagCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapV12R0111bEXCat6K.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapV12R0214SXCat6K.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapCatOSV08R0101.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapCatOSV08R0601.setDescription('IEEE8023-LAG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8023-LAG-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8023LagCapability, cIeee8023LagCapCatOSV08R0601=cIeee8023LagCapCatOSV08R0601, cIeee8023LagCapV12R0111bEXCat6K=cIeee8023LagCapV12R0111bEXCat6K, cIeee8023LagCapCatOSV08R0101=cIeee8023LagCapCatOSV08R0101, ciscoIeee8023LagCapability=ciscoIeee8023LagCapability, cIeee8023LagCapV12R0214SXCat6K=cIeee8023LagCapV12R0214SXCat6K)
