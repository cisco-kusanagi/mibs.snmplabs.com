#
# PySNMP MIB module CISCO-STACK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-STACK-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Counter64, Counter32, Integer32, Bits, ModuleIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter64", "Counter32", "Integer32", "Bits", "ModuleIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoStackCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 378))
ciscoStackCapability.setRevisions(('2008-03-19 00:00', '2006-03-15 00:00', '2005-01-19 00:00', '2003-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoStackCapability.setRevisionsDescriptions(('Added ciscoStackCapCatOSV08R0701PCat6k for Cisco CatOS 8.7(1).', 'Add VARIATIONs for notifications chassisAlarmOff, chassisAlarmOn, moduleDown and moduleUp, in ciscoStackCapCatOSV08R0101Cat6k.', 'Added ciscoStackCapV12R0112cE01PCat6k for Cisco IOS 12.1(12c)E1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoStackCapability.setLastUpdated('200803190000Z')
if mibBuilder.loadTexts: ciscoStackCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoStackCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoStackCapability.setDescription('The capabilities description of CISCO-STACK-MIB.')
ciscoStackCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapCatOSV08R0101Cat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapV12R0111bEXCat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapV12R0112cE01PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setProductRelease('Cisco IOS 12.1(12c)E1 on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapV12R0112cE01PCat6k.setDescription('CISCO-STACK-MIB capabilities.')
ciscoStackCapCatOSV08R0701PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoStackCapCatOSV08R0701PCat6k.setDescription('CISCO-STACK-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-STACK-CAPABILITY", ciscoStackCapCatOSV08R0101Cat6k=ciscoStackCapCatOSV08R0101Cat6k, ciscoStackCapability=ciscoStackCapability, PYSNMP_MODULE_ID=ciscoStackCapability, ciscoStackCapCatOSV08R0701PCat6k=ciscoStackCapCatOSV08R0701PCat6k, ciscoStackCapV12R0112cE01PCat6k=ciscoStackCapV12R0112cE01PCat6k, ciscoStackCapV12R0111bEXCat6k=ciscoStackCapV12R0111bEXCat6k)
