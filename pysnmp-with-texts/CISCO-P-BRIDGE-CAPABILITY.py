#
# PySNMP MIB module CISCO-P-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-P-BRIDGE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32, TimeTicks, Integer32, iso, IpAddress, NotificationType, Gauge32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "iso", "IpAddress", "NotificationType", "Gauge32", "Counter32", "ModuleIdentity")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
ciscoPBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 385))
ciscoPBridgeCapability.setRevisions(('2004-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPBridgeCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPBridgeCapability.setLastUpdated('200401140000Z')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setDescription('The agent capabilities description of P-BRIDGE-MIB.')
ciscoPBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 385, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPBridgeCapCatOSV08R0301.setDescription('P-BRIDGE-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-P-BRIDGE-CAPABILITY", ciscoPBridgeCapCatOSV08R0301=ciscoPBridgeCapCatOSV08R0301, PYSNMP_MODULE_ID=ciscoPBridgeCapability, ciscoPBridgeCapability=ciscoPBridgeCapability)
