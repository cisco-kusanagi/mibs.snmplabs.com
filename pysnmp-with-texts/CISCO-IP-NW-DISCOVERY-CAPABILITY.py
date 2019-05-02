#
# PySNMP MIB module CISCO-IP-NW-DISCOVERY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-NW-DISCOVERY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, iso, TimeTicks, Bits, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "TimeTicks", "Bits", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpNwDiscoveryCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 523))
ciscoIpNwDiscoveryCapability.setRevisions(('2006-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setLastUpdated('200611070000Z')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setDescription('The capabilities description of CISCO-IP-NW-DISCOVERY-MIB.')
cIpNwDiscoverCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 523, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIpNwDiscoverCapSanOSV30R1MDS9000.setDescription('Cisco IP NW Discovery MIB capabilities')
mibBuilder.exportSymbols("CISCO-IP-NW-DISCOVERY-CAPABILITY", ciscoIpNwDiscoveryCapability=ciscoIpNwDiscoveryCapability, cIpNwDiscoverCapSanOSV30R1MDS9000=cIpNwDiscoverCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIpNwDiscoveryCapability)
