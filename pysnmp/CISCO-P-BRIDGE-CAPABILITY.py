#
# PySNMP MIB module CISCO-P-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-P-BRIDGE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType, IpAddress, TimeTicks, Gauge32, ObjectIdentity, Counter64, Unsigned32, Integer32, Counter32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "Bits")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
ciscoPBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 385))
ciscoPBridgeCapability.setRevisions(('2004-01-14 00:00',))
if mibBuilder.loadTexts: ciscoPBridgeCapability.setLastUpdated('200401140000Z')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setOrganization('Cisco Systems, Inc.')
ciscoPBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 385, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setStatus('current')
mibBuilder.exportSymbols("CISCO-P-BRIDGE-CAPABILITY", ciscoPBridgeCapability=ciscoPBridgeCapability, PYSNMP_MODULE_ID=ciscoPBridgeCapability, ciscoPBridgeCapCatOSV08R0301=ciscoPBridgeCapCatOSV08R0301)
