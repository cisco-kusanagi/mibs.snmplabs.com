#
# PySNMP MIB module CISCO-IPV6-MLD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPV6-MLD-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Unsigned32, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter64, NotificationType, ModuleIdentity, Gauge32, TimeTicks, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cipv6mldCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 470))
cipv6mldCapability.setRevisions(('2006-01-07 00:00',))
if mibBuilder.loadTexts: cipv6mldCapability.setLastUpdated('200601070000Z')
if mibBuilder.loadTexts: cipv6mldCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpv6MldCapCRS1V3R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 470, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPV6-MLD-CAPABILITY", cipv6mldCapability=cipv6mldCapability, ciscoIpv6MldCapCRS1V3R02=ciscoIpv6MldCapCRS1V3R02, PYSNMP_MODULE_ID=cipv6mldCapability)
