#
# PySNMP MIB module CISCO-IETF-IPMROUTE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-IPMROUTE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, NotificationType, IpAddress, ModuleIdentity, Bits, iso, Gauge32, Counter64, Unsigned32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "iso", "Gauge32", "Counter64", "Unsigned32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfIpMrouteCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 442))
ciscoIetfIpMrouteCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setDescription('The capabilities description of CISCO-IETF-IPMROUTE-MIB')
cIetfIpMrouteCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 442, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfIpMrouteCapV320CRS1.setDescription('CISCO-IETF-IPMROUTE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-IPMROUTE-CAPABILITY", cIetfIpMrouteCapV320CRS1=cIetfIpMrouteCapV320CRS1, PYSNMP_MODULE_ID=ciscoIetfIpMrouteCapability, ciscoIetfIpMrouteCapability=ciscoIetfIpMrouteCapability)
