#
# PySNMP MIB module CISCO-IPV6-MLD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPV6-MLD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, TimeTicks, iso, Gauge32, Bits, Counter64, NotificationType, MibIdentifier, Unsigned32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "iso", "Gauge32", "Bits", "Counter64", "NotificationType", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cipv6mldCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 470))
cipv6mldCapability.setRevisions(('2006-01-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cipv6mldCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cipv6mldCapability.setLastUpdated('200601070000Z')
if mibBuilder.loadTexts: cipv6mldCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cipv6mldCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: cipv6mldCapability.setDescription('The capabilities description of IPV6-MLD-MIB.')
ciscoIpv6MldCapCRS1V3R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 470, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setStatus('current')
if mibBuilder.loadTexts: ciscoIpv6MldCapCRS1V3R02.setDescription('IPV6-MLD-MIB capabilities for IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-IPV6-MLD-CAPABILITY", ciscoIpv6MldCapCRS1V3R02=ciscoIpv6MldCapCRS1V3R02, cipv6mldCapability=cipv6mldCapability, PYSNMP_MODULE_ID=cipv6mldCapability)
