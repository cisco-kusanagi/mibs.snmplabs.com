#
# PySNMP MIB module CISCO-IETF-IPMROUTE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-IPMROUTE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, ObjectIdentity, MibIdentifier, IpAddress, iso, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Gauge32, ModuleIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfIpMrouteCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 442))
ciscoIetfIpMrouteCapability.setRevisions(('2005-07-27 00:00',))
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setOrganization('Cisco Systems, Inc.')
cIetfIpMrouteCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 442, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-IPMROUTE-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfIpMrouteCapability, cIetfIpMrouteCapV320CRS1=cIetfIpMrouteCapV320CRS1, ciscoIetfIpMrouteCapability=ciscoIetfIpMrouteCapability)
