#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-DISPLAY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:56:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, NotificationType, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ModuleIdentity, Integer32, IpAddress, MibIdentifier, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "Bits", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDisplayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 379))
ciscoEntityDisplayCapability.setRevisions(('2010-11-09 00:00', '2007-07-16 00:00', '2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setRevisionsDescriptions(('Added the agent capabilities statement cEntDisplayCapV12R0250SYPCat6k.', 'Added the agent capabilities statement cEntDisplayCapV12R0233SXHPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setLastUpdated('201011090000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-displaymib@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setDescription('The capabilities description of CISCO-ENTITY-DISPLAY-MIB.')
cEntDisplayCapCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapCatOSV08R0301Cat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
cEntDisplayCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapV12R0233SXHPCat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
cEntDisplayCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapV12R0250SYPCat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-CAPABILITY", cEntDisplayCapV12R0233SXHPCat6k=cEntDisplayCapV12R0233SXHPCat6k, PYSNMP_MODULE_ID=ciscoEntityDisplayCapability, ciscoEntityDisplayCapability=ciscoEntityDisplayCapability, cEntDisplayCapV12R0250SYPCat6k=cEntDisplayCapV12R0250SYPCat6k, cEntDisplayCapCatOSV08R0301Cat6k=cEntDisplayCapCatOSV08R0301Cat6k)
