#
# PySNMP MIB module CISCO-IPV6-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPV6-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Counter32, Integer32, TimeTicks, Bits, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, MibIdentifier, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "TimeTicks", "Bits", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "MibIdentifier", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cipv6Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 503))
cipv6Capability.setRevisions(('2006-05-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cipv6Capability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cipv6Capability.setLastUpdated('200605170000Z')
if mibBuilder.loadTexts: cipv6Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cipv6Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: cipv6Capability.setDescription('The capabilities description of RFC 2465 Based IPV6-MIB.')
ciscoIpv6CapCRS1V3R3R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 503, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setProductRelease('Cisco IOS XR 3.3.1 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpv6CapCRS1V3R3R1.setDescription('IPV6-MIB capabilities for IOS XR release 3.3.1')
mibBuilder.exportSymbols("CISCO-IPV6-CAPABILITY", cipv6Capability=cipv6Capability, ciscoIpv6CapCRS1V3R3R1=ciscoIpv6CapCRS1V3R3R1, PYSNMP_MODULE_ID=cipv6Capability)
