#
# PySNMP MIB module CISCO-PING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, MibIdentifier, TimeTicks, Gauge32, Counter64, iso, Unsigned32, IpAddress, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Gauge32", "Counter64", "iso", "Unsigned32", "IpAddress", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 36))
ciscoPingCapability.setRevisions(('2006-03-15 00:00', '2004-06-14 00:00', '2004-01-19 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPingCapability.setRevisionsDescriptions(('Add VARIATION for notification ciscoPingCompletion in ciscoPingCapabilityCatOSV08R0301.', 'Fix the typo in the supporting for the CatOS platform for this MIB module.', 'Add supporting for the CatOS platform for this MIB module.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPingCapability.setLastUpdated('200603150000Z')
if mibBuilder.loadTexts: ciscoPingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPingCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPingCapability.setDescription('Agent capabilities for CISCO-PING-MIB.')
ciscoPingCapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoPingCapabilityV10R02.setDescription('Cisco Ping MIB capabilities.')
ciscoPingCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPingCapabilityCatOSV08R0301.setDescription('CISCO-PING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PING-CAPABILITY", ciscoPingCapabilityCatOSV08R0301=ciscoPingCapabilityCatOSV08R0301, ciscoPingCapabilityV10R02=ciscoPingCapabilityV10R02, PYSNMP_MODULE_ID=ciscoPingCapability, ciscoPingCapability=ciscoPingCapability)
