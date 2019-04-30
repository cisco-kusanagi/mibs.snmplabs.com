#
# PySNMP MIB module CISCO-VLAN-BRIDGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-BRIDGING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, Counter64, Bits, Counter32, IpAddress, Integer32, Unsigned32, ModuleIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "Counter32", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanBridgingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 339))
ciscoVlanBridgingCapability.setRevisions(('2004-06-11 00:00',))
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setLastUpdated('200406110000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setOrganization('Cisco Systems, Inc.')
cVlanBridgingCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setStatus('current')
cVlanBridgingCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-CAPABILITY", ciscoVlanBridgingCapability=ciscoVlanBridgingCapability, PYSNMP_MODULE_ID=ciscoVlanBridgingCapability, cVlanBridgingCapCatOSV08R0201=cVlanBridgingCapCatOSV08R0201, cVlanBridgingCapCatOSV08R0101=cVlanBridgingCapCatOSV08R0101)
