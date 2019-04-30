#
# PySNMP MIB module CISCO-POLICY-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POLICY-GROUP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, IpAddress, Unsigned32, Counter32, Gauge32, ModuleIdentity, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter32", "Gauge32", "ModuleIdentity", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPolicyGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 512))
ciscoPolicyGroupCapability.setRevisions(('2006-06-26 00:00',))
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setLastUpdated('200606260000Z')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setOrganization('Cisco Systems, Inc.')
ciscoPolicyGroupCapV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 512, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-CAPABILITY", ciscoPolicyGroupCapV08R0601=ciscoPolicyGroupCapV08R0601, ciscoPolicyGroupCapability=ciscoPolicyGroupCapability, PYSNMP_MODULE_ID=ciscoPolicyGroupCapability)
