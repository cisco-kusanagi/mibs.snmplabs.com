#
# PySNMP MIB module CISCO-PING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, TimeTicks, Gauge32, MibIdentifier, ObjectIdentity, Counter32, ModuleIdentity, NotificationType, Bits, iso, Unsigned32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter32", "ModuleIdentity", "NotificationType", "Bits", "iso", "Unsigned32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 36))
ciscoPingCapability.setRevisions(('2006-03-15 00:00', '2004-06-14 00:00', '2004-01-19 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoPingCapability.setLastUpdated('200603150000Z')
if mibBuilder.loadTexts: ciscoPingCapability.setOrganization('Cisco Systems, Inc.')
ciscoPingCapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setStatus('current')
ciscoPingCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setStatus('current')
mibBuilder.exportSymbols("CISCO-PING-CAPABILITY", ciscoPingCapabilityV10R02=ciscoPingCapabilityV10R02, ciscoPingCapability=ciscoPingCapability, ciscoPingCapabilityCatOSV08R0301=ciscoPingCapabilityCatOSV08R0301, PYSNMP_MODULE_ID=ciscoPingCapability)
